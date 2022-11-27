from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print("GET")
    if request.method == 'POST':
        rq = request
        print("POST")
        print(rq.data)
        # file = request.files['u_img']
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
