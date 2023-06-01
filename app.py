from flask import Flask, render_template, request

from converter import converter

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            error = 'No selected file'
            return render_template('index.html', error=error)
        if file.filename.rsplit('.', 1)[1].lower() != 'pdf':
            error = "It's not .pdf file"
            return render_template('index.html', error=error)
        mp3 = converter(file)

    return render_template('index.html', error=error)


if __name__ == "__main__":
    app.debug = True
    app.run()
