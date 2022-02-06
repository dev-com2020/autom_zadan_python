
import os
import argparse
import csv
import docx

from PyPDF2 import PdfFileReader
from bs4 import UnicodeDammit


def search_txt(filename, word):
    '''
    Wyszukuje słowo w pliku tekstowym.
    '''
    # Wykrywanie kodowania.
    with open(filename, 'rb') as file:
        content = file.read(1024)

    suggestion = UnicodeDammit(content)
    encoding = suggestion.original_encoding

    # Otwieranie i wczytywanie pliku.
    with open(filename, encoding=encoding) as file:
        for line in file:
            if word in line.lower():
                return True

    return False


def search_csv(filename, word):
    '''
    Wyszukuje słowo w pliku CSV.
    '''
    with open(filename) as file:
        for row in csv.reader(file):
            for column in row:
                if word in column.lower():
                    return True

    return False


def search_pdf(filename, word):
    '''
    Wyszukuje słowo w pliku PDF.
    '''
    with open(filename, 'rb') as file:
        document = PdfFileReader(file)
        if document.isEncrypted:
            return False
        for page in document.pages:
            text = page.extractText()
            if word in text.lower():
                return True

    return False


def search_docx(filename, word):
    '''
    Wyszukuje słowo w dokumencie Worda.
    '''
    doc = docx.Document(filename)
    for paragraph in doc.paragraphs:
        if word in paragraph.text.lower():
            return True

    return False


EXTENSIONS = {
    'txt': search_txt,
    'csv': search_csv,
    'pdf': search_pdf,
    'docx': search_docx,
}


def main(word):
    '''
    Otwiera bieżący katalog i szuka słów we wszystkich plikach.
    '''
    for root, dirs, files in os.walk('.'):
        for file in files:
            # Pobieranie rozszerzenia.
            extension = file.split('.')[-1]
            if extension in EXTENSIONS:
                search_file = EXTENSIONS.get(extension)
                full_file_path = os.path.join(root, file)
                if search_file(full_file_path, word):
                    print(f'>>> Słowo znaleziono w pliku {full_file_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', type=str, help='Szukane słowo', default='the')
    args = parser.parse_args()

    # Zmiana liter na małe.
    main(args.w.lower())
