# Resume Skill Gap Analyzer

A web application that analyzes a resume and identifies missing 
skills required for a target job role.

## What it does
Upload your resume as a PDF, select a target role (Data Analyst, 
Software Engineer, or ML Engineer), and get a gap report showing 
which required skills you have and which you're missing, along 
with a match percentage.

## Tech Stack
- Python
- pdfplumber (PDF text extraction)
- Flask (REST API)
- HTML, CSS, JavaScript (frontend)

## How to run locally

1. Clone the repo
   git clone https://github.com/yourusername/resume-analyzer

2. Install dependencies
   pip install -r requirements.txt

3. Start the server
   python app.py

4. Open browser
   http://127.0.0.1:5000

## What I learned
- Extracting text from PDFs, and why different libraries 
  handle complex layouts differently — PyPDF2 failed on 
  resumes with sidebar designs while pdfplumber handled 
  them correctly
- Basic NLP-style text matching — using regex word boundaries 
  for single-word skills and substring matching for multi-word 
  skills like "power bi", since a naive approach either missed 
  matches or gave false positives
- Handling file uploads in Flask using request.files and 
  reading files in memory with io.BytesIO instead of saving 
  to disk
- Sending files from JavaScript using FormData instead of 
  JSON, since files can't be serialized the same way as text

## Screenshots
<img width="1917" height="967" alt="Screenshot 2026-07-16 091140" src="https://github.com/user-attachments/assets/6e4fd81c-0317-4228-b1d6-2e8a4b899552" />
<img width="1917" height="970" alt="Screenshot 2026-07-16 091220" src="https://github.com/user-attachments/assets/da818a74-fb2f-43fa-9371-61d577a53f59" />
