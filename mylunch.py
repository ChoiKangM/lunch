from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/haedal")
def haedal():
    return "This is Haedal"

# Flask를 쉽게 켜자
if __name__ == '__main__':
  app.run(debug=True)