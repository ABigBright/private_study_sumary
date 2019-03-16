from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        for inx,iny in request.form.items():
            print(inx,iny)
    return render_template('/index.html')

if __name__ == '__main__':
    app.run()
