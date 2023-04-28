from fastapi import FastAPI
from router.router_transaction import router_transaction

application = FastAPI()

application.include_router(router_transaction)
