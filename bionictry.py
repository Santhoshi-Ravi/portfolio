import api_keys
import PyPDF2
import convertapi
import io
import requests

def bionic_api_conversion(pdfFileObj):
    """
    This performs the conversion of any file into to the bionic format using the API
    
    Arguments: the uploaded file
    Returns: return the path of the file that contains the converted pdf into the bionic html format.
    
    """
    para = ""
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num = pdfReader.numPages
    for page_no in range(0,num):
        pageObj = pdfReader.getPage(page_no)
        para += "\n"*3+ pageObj.extractText()

    url = "https://bionic-reading1.p.rapidapi.com/convert"
    para = para.encode('latin-1', 'replace').decode('latin-1')
    payload = "content=" + para +"&response_type=html&request_type=html&fixation=1&saccade=10"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": api_keys.bionic_api_key,
        "X-RapidAPI-Host": "bionic-reading1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    with io.open('output.html', "w", encoding="utf-8") as f:
        f.write(response.text)
    return 'output.html'


def converting_bionic_html_to_pdf(path):
    convertapi.api_secret = api_keys.convert_api_key
    convertapi.convert('pdf', {
        'File': path
    }, from_format = 'html').save_files('PDF/')
    return "PDF/output.pdf"
