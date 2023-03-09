import uvicorn
from controller import apiController

if __name__== "__main__":
    uvicorn.run(apiController.app, host="localhost", port=8086)