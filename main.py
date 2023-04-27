from enum import Enum
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

application = FastAPI()

# tipe enum
class Tipe(str,Enum):
    def __str__(self):
        return str(self.value)
    INCOME = "INCOME"
    PURCHASE = "PURCHASE"
    INVEST = "INVEST"

# tipe enum
class Method(str,Enum):
    def __str__(self):
        return str(self.value)
    CASH = "CASH"
    EWALLET = "EWALLET"
    BANK = "BANK"

# class request body
class InputTransaction(BaseModel):
    tipe:Tipe
    amount:int
    notes:Optional[str]
    mehthod:Method

transaction = []

# start main ------------------------------------------

# endpoint Get - query paramameter
@application.get("/transaction")
def get_transaction(tipe:str,amount:int):
    return f"balikan transaksi dengan tipe {tipe} & jumlah {amount}"

# endpoint Get - Path paramameter
@application.get("/transaction/{tipe}")
def get_transaction(tipe:str):
    return f"balikan transaksi dengan tipe {tipe}"

# endpoint Post - Request body
@application.post("/transaction")
def insert_transaction(input_transaction:InputTransaction):

    transaction.append(input_transaction)
    return transaction

# end main ------------------------------------------
