@echo off
title Campus Pulse - Hackathon Web App
echo ========================================================
echo   Starting Campus Pulse Web Application...
echo ========================================================
python server.py
if errorlevel 1 (
    echo.
    echo Python not found in path, opening index.html directly...
    start index.html
)
pause
