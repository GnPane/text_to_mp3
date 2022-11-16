import pdfplumber
from pathlib import Path
import mp3


def pdf_to_mp3(file_path, lang='ru'):
    if not Path(file_path).is_file():
        return 'File not exists!'
    else:
        print(f'[-] Файл {file_path} в обработке...')
        if Path(file_path).suffix == '.pdf':
            with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
                pages = [page.extract_text() for page in pdf.pages]
            text = ' '.join(pages)

        if Path(file_path).suffix == '.txt':
            with open(file_path, 'r') as file:
                text = file.read()

        mp3.text_to_mp3(text, file_name=file_path, lang=lang)

        return print(f'[-] File mp3 success done!')


def main(file_name):
    pdf_to_mp3(file_path=file_name, lang='ru')


if __name__ == '__main__':
    main()
