from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pdfplumber
import io
from extractor import match_skills,extract_text

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/analyze',methods=['POST'])
def analyze():
  file=request.files['resume']
  role=request.form['role']
  if 'resume' not in request.files:
    return jsonify({'error':'No File Uploaded'}), 400
  file_bytes=io.BytesIO(file.read())
  full_text=extract_text(file_bytes)
  if full_text is None:
    return jsonify({'error':'Could not read this PDF. Please use a simple single column resume.'}),400
  found,missing=match_skills(full_text,role)
  return jsonify({
    'role': role,
    'found': found,
    'missing': missing,
    'total_required': len(found) + len(missing),
    'match_percentage': round(len(found) / (len(found) + len(missing)) * 100)
  })

if __name__ == '__main__':
  app.run(debug=True)