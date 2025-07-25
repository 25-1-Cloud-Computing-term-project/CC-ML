import os
import numpy as np
from fastapi import FastAPI
import uvicorn

from dependencies import lifespan
from routers import router

app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)  
