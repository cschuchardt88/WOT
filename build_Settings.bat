@echo off
del mod_Settings.pyc
C:\Python27\python.exe -m py_compile mod_Settings.py
copy mod_Settings.pyc C:\Games\World_of_Tanks\res_mods\0.9.21.0.2\scripts\client\gui\mods