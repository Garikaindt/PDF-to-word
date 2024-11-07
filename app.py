import streamlit as st
from pdf2docx import Converter
import os

# Set up the Streamlit interface
st.title("PDF to Word Converter")
st.write("Upload a PDF file to convert it into a Word document (.docx).")

# Upload PDF file
pdf_file = st.file_uploader("Choose a PDF file", type="pdf")

# Directory to store files
output_dir = "uploads"
os.makedirs(output_dir, exist_ok=True)  # Ensure the uploads directory exists

# Convert PDF to Word function
def convert_pdf_to_word(pdf_file):
    # Define paths for PDF and output Word file
    pdf_path = os.path.join(output_dir, pdf_file.name)
    word_file_name = os.path.splitext(pdf_file.name)[0] + ".docx"
    word_file_path = os.path.join(output_dir, word_file_name)

    # Save the uploaded PDF to the server
    with open(pdf_path, "wb") as f:
        f.write(pdf_file.getbuffer())

    # Convert PDF to Word
    cv = Converter(pdf_path)
    cv.convert(word_file_path, start=0, end=None)
    cv.close()

    return word_file_path

# Convert and download button
if pdf_file:
    if st.button("Convert to Word"):
        word_file_path = convert_pdf_to_word(pdf_file)
        st.success("Conversion successful!")
        
        # Provide download link
        with open(word_file_path, "rb") as f:
            st.download_button(
                label="Download Word File",
                data=f,
                file_name=os.path.basename(word_file_path),
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

