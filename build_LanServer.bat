@echo off
del mod_LanServer.pyc
C:\Python27.14\python.exe -m py_compile mod_LanServer.py
copy mod_LanServer.pyc C:\Games\World_of_Tanks\res_mods\0.9.21.0.3\scripts\client\gui\mods