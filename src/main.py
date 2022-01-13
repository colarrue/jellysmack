from fastapi import FastAPI

import src.api.router

app = FastAPI()

app.include_router(src.api.router.api_router)


@app.get("/")
def root():
    return {"Hello Jellysmack"}
