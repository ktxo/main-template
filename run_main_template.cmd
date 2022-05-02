@ECHO OFF
SETLOCAL

SET APP_HOME=C:/tmp/main-template

cd /D %APP_HOME%
IF ERRORLEVEL 1 ECHO ERROR

echo Using APP_HOME=%APP_HOME%
.\main_template -c config.json -l logging.json %1 %2 %3 %4 %5 %6 %7 %8 %9


:ERROR
echo.
echo Cannot change to APP_HOME=%APP_HOME%. Aborting
