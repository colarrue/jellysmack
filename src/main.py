import uvicorn
from fastapi import FastAPI

import src.api.router

app = FastAPI()

app.include_router(src.api.router.api_router)


@app.get("/")
def root():
    return {"Hello Jellysmack"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
