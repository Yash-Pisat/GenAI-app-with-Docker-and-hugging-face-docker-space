from fastapi import FastAPI
from transformers import pipeline


## create a new FastAPI app instance
app = FastAPI()

## Initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")


@app.get("/")
def home():
    return{"message":"Hello World"}

# Define a function to handle the GET request at '/generate'


@app.get("/generate")
def generate(text:str):
    ## use the pipeline to generate text from given input text
    output = pipe(text)

    ## return the generated text in json response
    return {"output":output[0]['Generated_text']}