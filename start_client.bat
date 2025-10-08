@echo off
echo installing libraries...
pip install -r requirement.txt
cls
echo starting server
python game/serv/server.py
pause