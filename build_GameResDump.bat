@echo off
del mod_GameResDump.pyc
C:\Python27.14\python.exe -m py_compile mod_GameResDump.py
copy mod_GameResDump.pyc C:\Games\World_of_Tanks\res_mods\0.9.21.0.3\scripts\client\gui\mods