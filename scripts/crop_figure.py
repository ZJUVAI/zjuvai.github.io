#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 PDF 中自动裁取指定编号的图（Figure N），保存为 PNG。

策略：
- 下载或读取 PDF
- 遍历每页，解析 text dict，找到包含 `Figure 2` / `Fig. 2` 的文本块，拿到其 bbox（caption）
- 同页寻找图像块（type=1），选取位于 caption 上方且距离最近的图像 bbox
- 以该图像 bbox 为主，四周扩 10-20 像素边距，裁成 PNG

用法：
  python scripts/crop_figure.py \
     --pdf-url "https://arxiv.org/pdf/2412.02205" \
     --figure 2 \
     --out "content/publications/DataLab/figure2.png"
"""

import re
import io
import sys
import fitz  # PyMuPDF
import argparse
from pathlib import Path
import requests
from PIL import Image


FIG_PATTERNS = [
    r"figure\s*{n}\b",
    r"fig\.\s*{n}\b",
    r"fig\s*{n}\b",
    r"图\s*{n}\b",
]


def download_pdf(url: str) -> bytes:
    # 允许不带 .pdf 后缀
    if not url.lower().endswith('.pdf') and 'arxiv.org/pdf/' in url:
        url = url.rstrip('/') + '.pdf'
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    return resp.content


def find_figure_bbox(doc: fitz.Document, fig_num: int):
    patterns = [re.compile(pat.format(n=fig_num), re.IGNORECASE) for pat in FIG_PATTERNS]

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        info = page.get_text('dict')
        blocks = info.get('blocks', [])

        # 收集图像块
        image_blocks = []
        for b in blocks:
            if b.get('type') == 1:  # image block
                bbox = b.get('bbox')
                if bbox:
                    image_blocks.append(tuple(bbox))

        if not image_blocks:
            continue

        # 找到包含 Figure 2 的文本块
        caption_boxes = []
        for b in blocks:
            if b.get('type') != 0:
                continue
            # 拼接文本
            text = ''.join(span.get('text', '') for line in b.get('lines', []) for span in line.get('spans', []))
            norm = text.lower().strip()
            if not norm:
                continue
            for pat in patterns:
                if pat.search(norm):
                    bbox = b.get('bbox')
                    if bbox:
                        caption_boxes.append(tuple(bbox))
                        break

        if not caption_boxes:
            continue

        # 以每个 caption，匹配最接近的上方图像
        for cap in caption_boxes:
            cx0, cy0, cx1, cy1 = cap
            best = None
            best_gap = 1e9
            for ib in image_blocks:
                x0, y0, x1, y1 = ib
                # 要求图像在标题上方一定范围（图通常在下方 caption 的上方）
                if y1 <= cy0 + 5:  # 图像底部在 caption 顶部之上或附近
                    gap = cy0 - y1
                    if 0 <= gap < best_gap:
                        best_gap = gap
                        best = ib
            if best:
                return page_index, best

    return None, None


def crop_image_from_pdf(pdf_bytes: bytes, bbox, page_index: int, out_path: Path, margin: int = 12):
    doc = fitz.open(stream=pdf_bytes, filetype='pdf')
    page = doc.load_page(page_index)
    x0, y0, x1, y1 = bbox

    # 扩展一点边距
    rect = fitz.Rect(max(0, x0 - margin), max(0, y0 - margin), x1 + margin, y1 + margin)

    # 以矩形截图（更清晰）
    pix = page.get_pixmap(clip=rect, alpha=False)
    img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, format='PNG', optimize=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf-url', required=True)
    parser.add_argument('--figure', type=int, default=2)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()

    pdf_bytes = download_pdf(args.pdf_url)
    doc = fitz.open(stream=pdf_bytes, filetype='pdf')

    page_idx, bbox = find_figure_bbox(doc, args.figure)
    if bbox is None:
        print(f'未找到 Figure {args.figure} 的候选区域，尝试回退：选择包含最多像素的首个图像…')
        # 回退：取第一页最大图像
        best = None
        best_area = 0
        best_idx = 0
        for i in range(len(doc)):
            page = doc.load_page(i)
            info = page.get_text('dict')
            for b in info.get('blocks', []):
                if b.get('type') == 1 and b.get('bbox'):
                    x0,y0,x1,y1 = b['bbox']
                    area = max(0, (x1-x0)*(y1-y0))
                    if area > best_area:
                        best_area = area
                        best = tuple(b['bbox'])
                        best_idx = i
        if best is None:
            print('未检测到任何图像，退出。')
            sys.exit(2)
        bbox = best
        page_idx = best_idx

    out_path = Path(args.out)
    crop_image_from_pdf(pdf_bytes, bbox, page_idx, out_path)
    print(f'Saved: {out_path}')


if __name__ == '__main__':
    main()
