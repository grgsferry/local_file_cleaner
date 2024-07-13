import os
import csv

def find_image_files(directory):
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_files.append(os.path.join(root, file))
    return image_files

def save_to_csv(file_list, csv_filename):
    file_list_sorted = sorted(file_list)
    
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ImageFileName'])
        for filepath in file_list_sorted:
            filename = os.path.basename(filepath) 
            writer.writerow([filename])

def main():
    # directory = input("Enter the directory path to search for images: ").strip()
    directory = 'C:\FERRY\Backup Note 10'
    image_files = find_image_files(directory)
    csv_filename = 'local.csv'
    save_to_csv(image_files, csv_filename)
    print(f"List of sorted image file names saved to {csv_filename}")

if __name__ == "__main__":
    main()
