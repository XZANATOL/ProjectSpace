@echo off
@setlocal enableextensions
@cd /d "%~dp0"

color a
title Destreamer Installer
pushd %cd%

echo Copying ffmpeg to C drive.
mkdir C:\ffmpeg\
xcopy .\soft\ffmpeg C:\ffmpeg /E /H
echo Done.
echo .

echo Installing Node.js
echo Wait for the installation to finish then press Enter
.\soft\node-v12.19.0-x64.msi /quiet /norestart /passive
pause
echo Done.
echo .

echo Adding required path to system path env var.
FOR /F "usebackq tokens=3*" %%A IN (`REG QUERY "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH `) DO (
    set appdir=%%A %%B
    )
setx /M path "%appdir%;C:\ffmpeg\bin"
echo Done.
set path=%appdir%
echo .

echo Preparing destreamer
chdir /d .\destreamer-master\
start npm install
pause
start npm run build
pause
echo Done.
echo .

echo Adding user:destreamer
echo username:destreamer password:destreamer
net user destreamer destreamer /add
echo Done.

echo Granting destreamer required permissions
chdir /d ..\
icacls destreamer-master /grant destreamer:(RX,W)
icacls destreamer-master\* /grant destreamer:(RX,W)
icacls C:\ffmpeg /grant destreamer:(RX,W)
icacls C:\ffmpeg\* /grant destreamer:(RX,W)
echo Done.

echo .
echo Everything is ready to go .. launch launcher.bat and go ahead with the video you want to download. :D
pause