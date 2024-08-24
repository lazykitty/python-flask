from flask import Flask 
app = Flask(__name__)

@app.route("/") #Decorator , HP mail page
def home():
    return "This is main page"

@app.route("/test") #sub page
def test():
    return "Test page"

if __name__ == "__main__":
    app.run()   #start server from this main prog
