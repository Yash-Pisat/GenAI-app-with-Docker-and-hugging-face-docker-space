from fastapi import fastapi
from transformers import pipeline


## create a new FASTAPI app instance
app = fastapi()

## Initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")


@app.get()
def home():
    return{"message":"Hello World"}

# Define a function to handle the GET request at '/generate'


@app.get("/generate")
def generate(text:str):
    