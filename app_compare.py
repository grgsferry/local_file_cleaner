import csv

def read_csv(filename, encoding='utf-8'):
    """ Read a CSV file and return a set of filenames """
    filenames = set()
    with open(filename, 'r', newline='', encoding=encoding) as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                filenames.add(row[0])
    return filenames

def write_csv(filename, data, encoding='utf-8'):
    """ Write a list of data to a CSV file """
    with open(filename, 'w', newline='', encoding=encoding) as file:
        writer = csv.writer(file)
        writer.writerows(data)

def find_not_in_google(local_file, google_file, not_in_google_file, is_in_google_file):
    """ Compare local.csv to google.csv and write the differences to respective CSV files """
    local_filenames = read_csv(local_file)
    google_filenames = read_csv(google_file)

    not_in_google = sorted([filename for filename in local_filenames if filename not in google_filenames])

    is_in_google = sorted([filename for filename in local_filenames if filename in google_filenames])

    write_csv(not_in_google_file, [(filename,) for filename in not_in_google])
    write_csv(is_in_google_file, [(filename,) for filename in is_in_google])

if __name__ == "__main__":
    local_csv = "local.csv"
    google_csv = "../google_photos_filenames_script/google.csv"
    not_in_google_csv = "not_in_google.csv"
    is_in_google_csv = "is_in_google.csv"

    find_not_in_google(local_csv, google_csv, not_in_google_csv, is_in_google_csv)
    print(f"Successfully generated '{not_in_google_csv}' and '{is_in_google_csv}' files.")