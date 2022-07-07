from flask import Flask

app = Flask(__name__)

@app.route('/leyicui-angel.github.io')
def home():
    return "Here it is!"

if __name__ == "__main__":
    app.run(debug=True)