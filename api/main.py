from fastapi import FASTAPI

app = FASTAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}