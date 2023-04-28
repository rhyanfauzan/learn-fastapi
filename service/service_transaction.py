from typing import Optional
from fastapi import Depends
from dto.dto_transaction import InputTransaction
from enums.enum_tipe import Tipe
from repository.repository_transaction import RepositoryTransaction


class ServiceTransaction:
    def __init__(self, repository_transaction: RepositoryTransaction = Depends()) -> None:
        self.repository_transaction = repository_transaction

    def insert_new_transaction(self, input_transaction: InputTransaction):
        return self.repository_transaction.insert_new_transaction(input_transaction)
    
    def get_list_transaction(self, tipe: Optional[Tipe] = None):
        match_filter = {}
        if tipe is not None:
            match_filter["tipe"] = tipe

        return self.repository_transaction.get_list_transaction(match_filter)