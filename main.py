from fastapi import FastAPI

application = FastAPI()

# endpoint Get - query paramameter
@application.get("/transaction")
def get_transaction(tipe:str,amount:int):
    return f"balikan transaksi dengan tipe {tipe} & jumlah {amount}"

# endpoint Get - Path paramameter
@application.get("/transaction/{tipe}")
def get_transaction(tipe:str):
    return f"balikan transaksi dengan tipe {tipe}"
