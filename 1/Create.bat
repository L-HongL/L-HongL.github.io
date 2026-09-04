echo off
chcp 65001 >nul

set /p input=输入博客分区/种类/标题(输入E/e取消):
if /i "%input%"=="E" (
    echo 已取消
    exit /b
)
for /f "tokens=1,2,3 delims=/" %%a in ("%input%") do (
    set "fa=%%a"
    set "cho=%%b"
    set "BL=%%c"
)

set url=content/%fa%/%cho%/%BL%/index.md


hugo new -k %cho% "%url%"

echo =======
echo 分区：%cho%
echo 标题：%BL%
echo 路径：%url%
echo 创建成功！
echo =======

