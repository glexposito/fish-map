from fastapi import FastAPI
import sys

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello Fish Map! Let's get started!"


@app.get("/python-version")
def get_python_version():
    return {"python_version": sys.version}
