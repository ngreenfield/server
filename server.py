from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"

# @app.post("/")
# @app.put("/")
# @app.patch("/")

@app.get("/test")
def test():
    return "This is another endpoint"

# JSON implementation
@app.get("/api/about")
def about():
    name={"name":"Nick"}
    return json.dumps(name)

app.run(debug=True)

