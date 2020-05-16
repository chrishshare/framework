@echo on
java  -Dwebdriver.chrome.driver=D:\01_Devspace\03_python\01_projects\02_autotest\framework\drivers\chrome\chromedriver_win32_81.exe -Dwebdriver.firefox.driver=D:\01_Devspace\03_python\01_projects\02_autotest\framework\drivers\firefox\geckodriver-v0.26.0-win64.exe -Dwebdriver.ie.driver=D:\01_Devspace\03_python\01_projects\02_autotest\framework\drivers\ie\IEDriverServer_x64_3.150.1.exe -jar selenium-server-standalone-3.141.59.jar  -role node -host 192.168.1.7 -hub http://192.168.1.7:4444/
@echo off
