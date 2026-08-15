@echo off
chcp 65001 >nul

echo ==============================
echo       Hugo Blog Publisher
echo ==============================

git add .

git commit -m "Update blog %date% %time%"

git push

echo.
echo ==============================
echo       Push 完成！
echo ==============================

pause