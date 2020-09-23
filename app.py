import spleeter
import os
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def form_fill():
    # i=request.files['myfile']
    i = request.files['myfile']
    filename = secure_filename(i.filename)
    i.save('input.mp3')
    stream = os.popen('spleeter separate -i input.mp3 -p spleeter:2stems -o static')
    output = stream.readlines()
    print(output)
    return render_template("result.html", fn=filename)


if __name__ == '__main__':
    app.run(debug=True)
