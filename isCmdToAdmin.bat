@echo off
break > cmdAdminOrNot.txt

goto check_Permissions
:check_Permissions echo Administrative permissions required. Detecting permissions...

net session >nul 2>&1
if %errorLevel% == 0 (
    echo Success: Administrative permissions confirmed.
    echo True > cmdAdminOrNot.txt

) else (
    echo Failure: Current permissions inadequate.
    echo False > cmdAdminOrNot.txt
)