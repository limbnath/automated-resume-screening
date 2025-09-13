import re
from rapidfuzz import fuzz, process

SKILL_DICT = [
    "python","java","c++","c#","sql","mysql","postgresql","mongodb",
    "docker","kubernetes","aws","azure","gcp","rest api","rest","api","html","css","javascript",
    "react","angular","node.js","express","tensorflow","pytorch","nlp","machine learning",
    "data structures","algorithms","git","linux","bash","ci/cd","jira"
]

def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9\.\+\#\s]', ' ', text)
    return ' '.join(text.split())

def extract_ngrams(text: str, n_min=1, n_max=3):
    tokens = text.split()
    ngrams = set()
    L = len(tokens)
    for n in range(n_min, n_max+1):
        for i in range(L-n+1):
            ngrams.add(' '.join(tokens[i:i+n]))
    return ngrams

def extract_skills_fuzzy(text: str, skill_dict=SKILL_DICT, threshold=85):
    text_norm = normalize_text(text)
    ngrams = extract_ngrams(text_norm, 1, 3)
    matched = set()
    for skill in skill_dict:
        match = process.extractOne(skill, ngrams)
        if match and match[1] >= threshold:
            matched.add(skill)
    # also include direct substring matches
    for skill in skill_dict:
        if skill in text_norm:
            matched.add(skill)
    return sorted(list(matched))
