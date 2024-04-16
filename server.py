from flask import Flask, request
import json
from config import dev, sum
from data import catalog
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #Warning, this disables CORS policy


@app.get("/")
def hello():
    return "Hello from Flask"


@app.get("/test")
def test():
    return "Test page!" 


@app.get("/about")
def about_me():
    return "Jen Navarro"


#######################################
############# API METHODS #############
#######################################


@app.get('/api/developer')
def developer():
    return json.dumps(dev)


@app.get("/api/sum")
def simple_sum():
    answ = sum(21,21)
    return json.dumps(answ)



@app.get("/api/products")
def get_catalog():
    return json.dumps(catalog)

@app.post("/api/products")
def save_product():
    prod = request.get_json() #read the payload
    catalog.append(prod)

    return json.dumps(prod)



# This will start server
# This must be the last line of code!
app.run(debug=True)


#Backend
# source venv\bin\activate
# python3 server.py

#Front end
# npm start