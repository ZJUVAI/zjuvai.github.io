@echo off
setlocal enabledelayedexpansion

echo === 论文信息爬虫工具 ===
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.6+
    pause
    exit /b 1
)

REM 检查依赖是否安装
echo 检查Python依赖...
pip show requests >nul 2>&1
if errorlevel 1 (
    echo 安装依赖包...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo 错误: 依赖安装失败
        pause
        exit /b 1
    )
)

echo 依赖检查完成
echo.

REM 检查是否有命令行参数
if "%~1"=="" (
    REM 无参数，启动交互模式
    echo 启动交互模式...
    python paper_crawler.py --interactive
) else (
    REM 有参数，直接搜索
    echo 搜索论文: %*
    python paper_crawler.py "%*"
)

echo.
echo 操作完成
pause
