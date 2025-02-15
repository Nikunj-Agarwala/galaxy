from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configure the upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def frontpage():
    return render_template('frontpage.html')

@app.route('/classifier')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    # Save file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return f"File {file.filename} uploaded successfully!"

if __name__ == "__main__":
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)