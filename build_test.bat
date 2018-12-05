@echo off
del mod_test.pyc
C:\Python27\python.exe -m py_compile mod_test.py
copy mod_test.pyc C:\Games\World_of_Tanks\res_mods\0.9.21.0.2\scripts\client\gui\mods