import pandas as pd
import os
import sys
from tabulate import tabulate

if len(sys.argv) != 3:
    print("Usage: python {} <PATH> <file.csv>".format(sys.argv[0]))
    sys.exit(1)

path, csv = sys.argv[1], sys.argv[2]

csvfile = os.path.join(path, csv)

try:
    df = pd.read_csv(csvfile)
    ndf = df[['Title', 'FirstAuthor', 'DOI', 'PublicationYear']]
except FileNotFoundError:
    sys.exit("CSV not found!")

folder = csv.replace(".csv", "")
folder_path = os.path.join(path, folder)

if os.path.exists(folder_path):
    sys.exit("Folder already exists!")

try:
    os.mkdir(folder_path)
except OSError as e:
    sys.exit(f"Error: {e}")

file_list = []
for id, (index, row) in enumerate(ndf.iterrows(), start=1):
    if pd.isnull(row['DOI']):
        continue

    file_path = os.path.join(folder_path, f"{id}.txt")
    with open(file_path, "w") as file:
        file.write(f"➜ {str(row['PublicationYear'])[:4]} | {csv[:-4]}\n\nTitle: {row['Title']}\n\nAuthors: {row['FirstAuthor']}\n\n{row['DOI']}")
        file_list.append(["➜", row['DOI']])
print(tabulate(file_list, headers=["Found", "DOI"], tablefmt="github"))
print(f"\ncheck -> {folder_path}")
