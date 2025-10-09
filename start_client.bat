@echo off
echo installing libraries...
pip install -r requirement.txt
cls
echo starting client
python game/serv/main.py
pause