import uvicorn
from fastapi import FastAPI

import src.api.router
import src.api.exceptions

app = FastAPI()

app.include_router(src.api.router.api_router)
app.add_exception_handler(
    src.api.exceptions.DatabaseException, src.api.exceptions.database_exception_handler
)


@app.get("/")
def root():
    return {"Hello Jellysmack"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
