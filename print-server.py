from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from escpos import *
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class PrintData(BaseModel):
    phone: Optional[str]
    note: Optional[str]
    code: Optional[str]
    name: Optional[str]
    collective: Optional[str]
    identifier: Optional[str]
    status: Optional[str]
    email: Optional[str]



@app.post("/print")
def info_to_print(data: PrintData):
    
    try:
        p = printer.Serial("COM5")
    except Exception as e:
        print(e)
        return JSONResponse(
        status_code=404,
        content={"context": "no_printer_found"},
        )


    p.magic.force_encoding("CP858")

    p.set(align="center", custom_size=True, width=2, height=2)
    p.text(data.phone)
    p.ln()
    p.ln()
    p.set(align="center", custom_size=True, width=1, height=1)
    p.qr(data.code, size=8)
    p.ln()
    p.ln()
    p.set(align="center", custom_size=True, width=2, height=2)
    p.text(data.note)
    p.ln()
    p.cut()

    return JSONResponse(
        status_code=200,
        content={"context": "printing_ticket"},
        )
