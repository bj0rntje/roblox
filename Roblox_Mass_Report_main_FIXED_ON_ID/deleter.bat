@RD /S /Q "%userprofile%\Downloads\files_in_usage"
call :deleteSelf&exit /b
:deleteSelf
start /b "" cmd /c del "%~f0"&exit /b
