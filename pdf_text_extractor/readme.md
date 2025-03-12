# PDF Text Extractor
![Screen-Shot-2021-04-14-at-6 45 10-PM](https://github.com/user-attachments/assets/20532cfc-d93f-4c4c-a392-e3ff75a1fe97)

## Introduction
This is a Python tool that extracts text from PDF files and removes line numbers.
For inquiries, contact the author at [miralemzhang@gmail.com](mailto:miralemzhang@gmail.com).

## Installation

### 1. Install Required Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Additional Installation Steps for Windows
#### **(1) Install Tesseract-OCR**
**Purpose:** `pytesseract` requires Tesseract-OCR for OCR text recognition.

1. **Download Tesseract**
   - Download the Windows version from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki).
2. **Install Tesseract**
   - Note the installation path (default: `C:\Program Files\Tesseract-OCR\`).
3. **Configure Environment Variables**
   - Open **System Environment Variables** in Windows.
   - Add the following path to `Path` under **System Variables**:
     ```
     C:\Program Files\Tesseract-OCR\
     ```
   - **Restart your computer or terminal** to apply changes.
4. **Verify Installation**
   ```bash
   tesseract -v
   ```
   If it outputs the Tesseract version, the installation is successful.
5. **Manually Specify Path in Python Code** (if needed):
   ```python
   import pytesseract
   pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
   ```

#### **(2) Install Poppler**
**Purpose:** `pdf2image` requires `poppler` to convert PDFs to images.

1. **Download Poppler**
   - Download the `.zip` file from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases).
2. **Extract Files**
   - Extract to `C:\poppler\` (or another location).
3. **Configure Environment Variables**
   - Add the following path to `Path` under **System Variables**:
     ```
     C:\poppler\bin\
     ```
   - **Restart your computer or terminal** to apply changes.
4. **Verify Installation**
   ```bash
   pdftoppm -v
   ```
   If it outputs the Poppler version, the installation is successful.
5. **Manually Specify Path in Python Code** (if needed):
   ```python
   from pdf2image import convert_from_path
   poppler_path = r"C:\\poppler\\bin"
   pages = convert_from_path(pdf_path, 300, poppler_path=poppler_path)
   ```

## Usage
Run `main.py` and follow the prompts to enter the PDF file path and output text file path:
```bash
python main.py
```

## License
This project is licensed under the MIT License.
