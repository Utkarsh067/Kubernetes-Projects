from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return (
        "<h1>Hello I am Utkarsh Jain<br>"
        "and this is my Flask app, containerized with Docker</h1>"
    )


if __name__ == "__main__":
    app.run(debug=True)
