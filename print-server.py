from fastapi import FastAPI
from pydantic import BaseModel
from escpos import *

app = FastAPI()

class PrintData(BaseModel):
    turn: str
    seat: str
    qr: str

@app.post("/print-data")
def info_to_print(data: PrintData):
    
    p = printer.Serial("COM5")
    p.magic.force_encoding("CP858")

    p.set(align="center", custom_size=True, width=2, height=2)
    p.text(data.turn)
    p.ln()
    p.ln()
    p.text(data.seat)
    p.ln()
    p.ln()
    p.set(align="center", custom_size=True, width=1, height=1)
    p.qr(data.qr, size=8)
    p.ln()
    p.cut()

    return {"Status": "Correct"}
