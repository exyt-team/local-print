@ECHO OFF
title localhost-print-server
@ECHO ON
cd C:\Users\AdiDumi\Documents\PythonScripts\impresora\
python -m pip install -r requirements.txt
python -m uvicorn print-server:app
pause
