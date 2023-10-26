import streamlit as st

def upload_pdf():
  uploaded_file = st.file_uploader("Choose a file", type=["pdf","png", "JPG"], accept_multiple_files = False)
  if uploaded_file.type == "application/pdf":
    # Proses file PDF dengan Fitz (PyMuPDF)
    doc = fitz.open(uploaded_file)
    text = ''
    for page in doc:
        page_text = page.get_text()
        text += page_text	
  else:
        st.text("Unsupported file format. Please upload a PDF, PNG, or JPG file.")
  # else:
  # doc = fitz.open(uploaded_file)
  #       text = ''
  #       for page in doc:
  #                   page_text = page.get_text()
  #                   text += page_text
  #       pymupdf_test = text
  
  return text

  #show output
  #answers = []
  #answers.append(st.text_area(f'Write answer question {i}', value=str(pymupdf_test) ,height= 300))
