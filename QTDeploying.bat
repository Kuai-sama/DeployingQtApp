@echo off 
:: The path of QT binaries (get the path via a txt file)
set /p PathQT=<Path_of_Qt_Dlls.txt
:: The path of the user executable (get the path via a txt file)
set /p exePath=<Path_of_exe_to_deploy.txt
:: The path of qtenv2.bat
set "file=%PathQT%qtenv2.bat"
:: Execute qtenv2.bat
call %file%
:: Change directory
cd /d %PathQT%
:: Same as the command "windeploqt your_path" in cmd
start /B "" "windeployqt.exe" %exePath%

echo Prees a key to continue