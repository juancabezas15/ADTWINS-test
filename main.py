from fastapi import FastAPI
from router.routes import router as user

app = FastAPI(
    title="API REST FOR ADTWINS TEST",
    description="API REST with FastAPI and MongoDB library Database",
    version="1.0.0"

)

app.include_router(user)
