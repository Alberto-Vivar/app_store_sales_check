import gzip
import csv


def extract(filename):
    txt_content = gzip.open(filename, mode='rt')
    file_reader = csv.DictReader(txt_content, delimiter='\t')
    field_names = file_reader.fieldnames
    rows = [row for row in file_reader]
    return field_names, rows
