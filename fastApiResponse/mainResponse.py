from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def hello_name(name: str):
    return f"Привет, {name}!"