import csv

def filter_filenames(input_csv, output_csv, encoding='utf-8'):
    with open(input_csv, mode='r', newline='', encoding=encoding, errors='ignore') as infile, \
         open(output_csv, mode='w', newline='', encoding=encoding) as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        headers = next(reader, None)
        if headers:
            writer.writerow(headers)
        
        for row in reader:
            filename = row[0]
            if "WA0" not in filename:
                writer.writerow(row)

input_csv = 'not_in_google.csv'
output_csv = 'not_in_google_wa_clean.csv'
filter_filenames(input_csv, output_csv, encoding='utf-8')
