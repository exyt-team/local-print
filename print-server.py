from fastapi import FastAPI
from pydantic import BaseModel
from escpos import *

app = FastAPI()

class PrintData(BaseModel):
    name: str
    surname: str
    qr: str

@app.post("/print-data")
def info_to_print(data: PrintData):
    
    p = printer.Serial("COM5")
    p.magic.force_encoding("CP858")

    p.text(data.name)
    p.ln()
    p.text(data.surname)
    p.ln()
    p.text("CODIGO QR")
    p.ln()
    p.qr(data.qr)
    p.ln()
    p.cut()

    return {"Status": "Correct"}
