@echo off
echo installing libraries...
pip install -r requirement.txt
cls
echo starting server
python serv/server.py
pause