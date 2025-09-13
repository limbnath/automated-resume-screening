from flask import Flask, request, render_template, redirect, url_for
import os
from src.parsing import extract_text
from src.scoring import compute_score

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB limit

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # JD: either pasted text or uploaded file
        jd_text = request.form.get('jd_text', '').strip()

        jd_file = request.files.get('jd_file')
        if jd_file and jd_file.filename != '':
            jd_filename = jd_file.filename
            jd_path = os.path.join(app.config['UPLOAD_FOLDER'], jd_filename)
            jd_file.save(jd_path)
            try:
                jd_text = extract_text(jd_path)
            except Exception as e:
                # fallback: keep pasted text or empty
                print("JD parsing error:", e)

        files = request.files.getlist('resumes')
        results = []
        for f in files:
            filename = f.filename
            if filename == '':
                continue
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(filepath)
            try:
                text = extract_text(filepath)
            except Exception as e:
                print("Resume parsing error:", e)
                text = ""
            result = compute_score(text, jd_text)
            result['filename'] = filename
            results.append(result)
        results = sorted(results, key=lambda x: x['score'], reverse=True)
        return render_template('results.html', results=results, jd_text=jd_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
