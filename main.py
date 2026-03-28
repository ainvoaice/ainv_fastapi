import fastapi 
app = fastapi.FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World"}
