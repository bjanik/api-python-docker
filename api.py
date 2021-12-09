from fastapi import FastAPI

from Controller import Controller
from Model import Model
from View import  View

app = FastAPI()

@app.get("/")
def root():
    return "This is root"

@app.get("/text/uppercase")
def get_uppercase(source: str = None):
    if source:
        model = Model()
        view = View()
        controller = Controller(model, view)
        model.add_line(source)
        return  { "result": controller.insert_lines()}

@app.get("/text/palindrome")
def is_palindrome(source: str = None):
    if source:
        return {"result": source == source[::-1]}
        
