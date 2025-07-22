@echo off
echo === 论文爬虫工具测试 ===
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.6+
    pause
    exit /b 1
)

echo 运行测试脚本...
python test_paper_crawler.py

echo.
pause
