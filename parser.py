import os
from PyPDF2 import PdfReader

DATA_DIR = 'data'
TXT_DIR = 'datatxt'
os.makedirs(TXT_DIR, exist_ok=True)

def pdf_to_txt(pdf_path, txt_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    for fname in os.listdir(DATA_DIR):
        if fname.lower().endswith('.pdf'):
            pdf_path = os.path.join(DATA_DIR, fname)
            txt_path = os.path.join(TXT_DIR, os.path.splitext(fname)[0] + '.txt')
            pdf_to_txt(pdf_path, txt_path)
            print(f'Converti: {fname} -> {txt_path}') 