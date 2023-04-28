from typing import Optional
from fastapi import APIRouter, Depends
from dto.dto_transaction import InputTransaction
from enums.enum_tipe import Tipe
from models.model_transaction import Transaction
from service.service_transaction import ServiceTransaction

router_transaction = APIRouter(prefix="/api/v1")

@router_transaction.post("/transaction")
def insert_new_transaction(
    input_transaction: InputTransaction,
    service_transaction: ServiceTransaction = Depends(),
):
    service_transaction.insert_new_transaction(input_transaction)
    return input_transaction

@router_transaction.get("/transaction")
def get_list_transaction(
    tipe: Optional[Tipe] = None,
    service_transaction: ServiceTransaction = Depends(),):
    return service_transaction.get_list_transaction(tipe)