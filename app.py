from flask import Flask, request, render_template, send_file
import os
import tempfile
from PyPDF2 import PdfReader
from docx import Document

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def pdf_to_word(pdf_path):
    pdf_reader = PdfReader(pdf_path)
    doc = Document()
    for page in pdf_reader.pages:
        text = page.extract_text()
        doc.add_paragraph(text)
    return doc

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file and file.filename.endswith('.pdf'):
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(pdf_path)
        word_doc = pdf_to_word(pdf_path)
        word_path = os.path.join(tempfile.gettempdir(), 'converted.docx')
        word_doc.save(word_path)
        return send_file(word_path, as_attachment=True, mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    
    return "Unsupported file format"

if __name__ == '__main__':
    app.run(debug=True)
