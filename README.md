PDF to Word Converter

This is a simple Streamlit web application that converts PDF files into Word documents (.docx). The app allows users to upload a PDF file, convert it into a Word format, and download the resulting document.
Features

-Upload any PDF file for conversion.
-Converts PDF files to Word format (.docx) quickly and efficiently.
 -Provides a download link for the converted Word document.

Installation

Clone this repository:

git clone https://github.com/Garikaindt/pdf-to-word-converter.git
cd pdf-to-word-converter

Install the required dependencies:

    pip install -r requirements.txt

Usage

Run the Streamlit app:

    streamlit run app.py

In the browser, upload your PDF file and click Convert to Word.

After successful conversion, a download button will appear to download the Word file.

Dependencies

    Streamlit: For creating the web interface.
    pdf2docx: For PDF to Word conversion.
    PyMuPDF: A dependency of pdf2docx used for handling PDF files.

Directory Structure

    app.py: Main Streamlit application.
    uploads/: Directory to store the uploaded and converted files.


