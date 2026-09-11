from datetime import date


from fastapi import FastAPI, HTTPException
from fastapi.openapi.models import Response
from pydantic import BaseModel

from transactions import transactions

app = FastAPI(
    title="API de Finanzas",
    description="Esta API permite gestionar al usuario, cuentas y relizar transacciones",
    version="BETA"
)

class BaseTransaction(BaseModel):
    id: int
    description: str | None
    amount: float | int
    type: str
    date: str
    account: str
    category: str

@app.get("/health", status_code=200)
def check_health():
    return {"message": "success"}

@app.get("/transactions", status_code=200)
def get_transactions():
    return transactions

@app.post("/transactions", status_code=201)
def add_transaction(transaction: BaseTransaction):
    return transaction

@app.get("/transactions/{transaction_id}", status_code=200)
def get_transaction_by_id(transaction_id: int):
    transaction = [transaction for transaction in transactions if transaction.get("id") == transaction_id]
    if transaction:
            return transaction

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )
