# 📝 Automated Resume Screening Tool

A Flask-based web application that automates resume shortlisting for recruiters.  
Upload resumes (PDF/DOCX/TXT) and a Job Description (JD as text or PDF/DOCX), and the system will:

- ✅ Parse documents using NLP  
- ✅ Extract and match technical skills (fuzzy matching with RapidFuzz + spaCy)  
- ✅ Compute a 0–100 match score  
- ✅ Generate a ranked shortlist with matched skills highlighted  

---

## 🚀 Features
- Upload **multiple resumes** (PDF/DOCX/TXT) at once  
- Upload JD as **text or file (PDF/DOCX)**  
- Extract skills using **spaCy + RapidFuzz**  
- Compute a weighted **match score** (Skills 80%, Keywords 10%, Experience 10%)  
- View results in a **ranked Bootstrap table**  
- Extendable for **semantic similarity** with `sentence-transformers`  

---

## 🛠️ Technologies Used
- **Backend:** Python, Flask  
- **NLP & Parsing:** spaCy, pdfplumber, docx2txt, RapidFuzz  
- **Database (optional):** SQLite  
- **Frontend:** HTML, CSS, Bootstrap  
- **Optional (advanced):** scikit-learn (TF-IDF), sentence-transformers (semantic matching)  

---

## 📂 Project Structure
