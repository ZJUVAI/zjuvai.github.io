#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从论文 PDF 生成 featured.png：
- 下载 PDF（如果给的是 URL）
- 使用 PyMuPDF 渲染第一页
- 进行简单的智能裁剪（去掉白边、页眉页脚）
- 居中裁切为 1200x630（常见社交预览比例）
- 保存为 content/publications/<dir>/featured.png

用法：
  python scripts/make_featured_image.py \
      --pdf "https://aclanthology.org/2025.acl-long.1196.pdf" \
      --out-dir "content/publications/feng-2025-instruct-embedding"
"""

import io
import os
import re
import sys
import math
import argparse
import tempfile
from pathlib import Path

import fitz  # PyMuPDF
import requests
from PIL import Image, ImageOps


def download_pdf(url: str) -> bytes:
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    return resp.content


def render_first_page(pdf_bytes: bytes, zoom: float = 2.0) -> Image.Image:
    doc = fitz.open(stream=pdf_bytes, filetype='pdf')
    page = doc.load_page(0)
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img


def auto_crop_whitespace(img: Image.Image, border: int = 8) -> Image.Image:
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        cropped = img.crop(bbox)
        # 额外去掉一点边
        x0, y0, x1, y1 = bbox
        x0 = max(0, x0 + border)
        y0 = max(0, y0 + border)
        x1 = min(img.width, x1 - border)
        y1 = min(img.height, y1 - border)
        return img.crop((x0, y0, x1, y1))
    return img


def heuristic_trim_header_footer(img: Image.Image, header_ratio=0.10, footer_ratio=0.08) -> Image.Image:
    w, h = img.size
    top = int(h * header_ratio)
    bottom = int(h * (1 - footer_ratio))
    if bottom > top:
        return img.crop((0, top, w, bottom))
    return img


def center_crop_aspect(img: Image.Image, target_w=1200, target_h=630) -> Image.Image:
    # 保持中心，按比例裁切
    tw, th = target_w, target_h
    target_ratio = tw / th
    w, h = img.size
    ratio = w / h
    if ratio > target_ratio:
        # 图过宽，裁左右
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        # 图过高，裁上下
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    return img.resize((tw, th), Image.LANCZOS)


def make_featured(pdf_url: str, out_dir: str):
    out_path = Path(out_dir) / "featured.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    pdf_bytes = download_pdf(pdf_url)
    img = render_first_page(pdf_bytes, zoom=2.0)

    # 简单预处理：去白边 -> 去页眉页脚 -> 居中裁切
    try:
        from PIL import ImageChops
        img = ImageOps.autocontrast(img)
        img = auto_crop_whitespace(img, border=10)
    except Exception:
        pass

    img = heuristic_trim_header_footer(img, 0.10, 0.08)
    img = center_crop_aspect(img, 1200, 630)

    img.save(out_path, format="PNG", optimize=True)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True, help="PDF URL or local path")
    parser.add_argument("--out-dir", required=True, help="Output directory (publication folder)")
    args = parser.parse_args()

    pdf = args.pdf
    if pdf.lower().startswith("http"):
        pdf_url = pdf
    else:
        # 本地文件
        with open(pdf, "rb") as f:
            data = f.read()
        # 写临时url方案，这里直接传本地bytes给渲染函数
        img = render_first_page(data, zoom=2.0)
        img = center_crop_aspect(img, 1200, 630)
        out_path = Path(args.out_dir) / "featured.png"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(out_path, format="PNG", optimize=True)
        print(f"Saved: {out_path}")
        sys.exit(0)

    make_featured(pdf_url, args.out_dir)
