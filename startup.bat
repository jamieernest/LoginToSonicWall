@echo off
echo [InternetShortcut] >> "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\sonicwall.url"
echo URL="%cd%\run.bat" >> "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\sonicwall.url"
echo IconFile=C:\WINDOWS\system32\SHELL32.dll >> "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\sonicwall.url"
echo IconIndex=20 >> "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\sonicwall.url"
echo URL="%cd%\run.bat"
PAUSE