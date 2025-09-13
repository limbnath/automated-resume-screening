# Automated Resume Screening Tool (Demo) - JD Upload Enabled

## What it is
A simple Flask web app that accepts resume files (PDF/DOCX/TXT) and a Job Description file (PDF/DOCX) or pasted JD,
extracts text, extracts skills using fuzzy matching, compares against a job description (JD) pasted by the user,
and produces a ranked shortlist with match scores.

## How to run (local)
1. Create and activate a Python 3.10+ virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows use `venv\Scripts\activate`
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser.

## Notes
- The app accepts JD as pasted text or as an uploaded PDF/DOCX file.
- For scanned (image) PDFs, OCR support is not included by default.
