from flask import Flask, render_template, request, redirect, url_for, flash
from model import probe_model_5l_profit
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file:
        try:
            content = file.read()
            data = json.loads(content)
            result = probe_model_5l_profit(data["data"])
            return render_template('results.html', result=result)
        except Exception as e:
            flash(f'Error processing the file: {str(e)}')
            return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
