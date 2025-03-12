import pytesseract
from pdf2image import convert_from_path
import re

def extract_text_from_pdf(pdf_path):
    pages = convert_from_path(pdf_path, 300)
    text = ""  
    for page in pages:
        text += pytesseract.image_to_string(page)    
    return text

def remove_line_numbers(text):
    cleaned_text = re.sub(r'^\d+\s*', '', text, flags=re.MULTILINE)
    return cleaned_text

def process_pdf(pdf_path, output_path):
    extracted_text = extract_text_from_pdf(pdf_path)
    cleaned_text = remove_line_numbers(extracted_text)
    with open(output_path, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(cleaned_text)
    
    print(f"清理后的文本已保存到 {output_path}")

if __name__ == "__main__":
    pdf_file_path = input("请输入 PDF 文件的路径：")
    output_text_path = input("请输入输出 txt 文件的路径：")
    process_pdf(pdf_file_path, output_text_path)
