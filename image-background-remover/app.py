from flask import Flask, request, redirect, url_for, render_template
import os
from remove_background import remove_bg

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PROCESSED_FOLDER'] = 'static/processed'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite de 16 MB

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
if not os.path.exists(app.config['PROCESSED_FOLDER']):
    os.makedirs(app.config['PROCESSED_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Gerar nome do arquivo processado com extensão .png
        processed_filename = os.path.splitext(filename)[0] + '.png'
        processed_file_path = os.path.join(app.config['PROCESSED_FOLDER'], processed_filename)
        remove_bg(file_path, processed_file_path)

        return render_template('result.html', filename=processed_filename)

if __name__ == '__main__':
    app.run(debug=True)
