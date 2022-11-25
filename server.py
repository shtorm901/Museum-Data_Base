from fastapi import FastAPI
from routers import visitor_router

app = FastAPI()
app.include_router(visitor_router, prefix='/visitor')