from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

with app.app_context():
    url_for('static', filename='style.css')
    
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    # return f"Hello {escape(name)}"
    return render_template('hello.html',name=name)

if __name__ == "__main__":
    app.run()