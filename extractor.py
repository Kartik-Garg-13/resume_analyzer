import pdfplumber
import re
from skills import SKILLS

def extract_text(pdf_source):
    pages = []
    with pdfplumber.open(pdf_source) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
    
    full_text = " ".join(pages).lower()
    
    if len(full_text.strip()) < 50:
        return None  # extraction failed
    
    return full_text
        
def match_skills(text, role):
  skill_list=SKILLS[role]
  found=[]
  missing=[]
  for i in skill_list:
    if (len(i.split())) > 1:
      if i.lower() in text.lower():
        found.append(i)
      else:
        missing.append(i)
    else:
      pattern=r'\b'+re.escape(i)+r'\b'
      if (bool(re.search(pattern,text,re.IGNORECASE))):
        found.append(i)
      else:
        missing.append(i)
  return found,missing
      