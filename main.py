from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is live, baby!"}

# test comment to trigger redeployment  
@app.get("/status")
def status():
    return {"status": "OK"}