from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
     return "<h1 style='color:red'>Serhii Zhohno! 25.09.2024</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
