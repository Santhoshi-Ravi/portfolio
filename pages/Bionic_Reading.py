import streamlit as st
import PyPDF2
import base64 
import bionictry
st.title("Bionic api")

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if uploaded_file != None:
    html_output_path = bionictry.bionic_api_conversion(uploaded_file)
    pdf_path = bionictry.converting_bionic_html_to_pdf(html_output_path)
    st.download_button(label="Download Bionic Converted PDF", 
        data = pdf_path,
        file_name = "bionic_converted.pdf",
        mime='application/octet-stream')
else:
    st.write("Please upload a valid PDF")


