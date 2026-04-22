from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from render!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/process")
def process_data(data: dict):
    # Simulate processing the data
    processed_data = {key: value.title() if isinstance(value, str) else value for key, value in data.items()}
    return {"processed_data": processed_data}