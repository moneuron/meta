import pandas as pd
import os, sys
from tabulate import tabulate

list =[]

while True:
    if len(sys.argv) != 3:
        print("Usage: python meta.py <PATH> <.csv Name>")
        sys.exit(1)
    else:
        break

path = sys.argv[1]
csv = sys.argv[2]
folder = sys.argv[2]
try:
    df = pd.read_csv(f"{path}/{csv}.csv")
    ndf = df[['Title', 'FirstAuthor', 'DOI','PublicationYear']]

except:
    sys.exit("CSV EROR!!")


folder_path = f"{path}/{folder}"

if not os.path.exists(folder_path):
    try:
        os.mkdir(folder_path)
    except OSError as e:
        sys.exit(f"Error: {e}")
else:
    sys.exit("Folder exists!")

id = 1
for index, row in ndf.iterrows():
    if pd.isnull(row['DOI']):
        continue

    file_path = f"{path}/{folder}/{id}.txt"
    with open(file_path, "w") as file:
        try:
            file.write(f"-> {int(row['PublicationYear'])} | {csv}\n\nTitle: {row['Title']}\n\nAuthor(s): {row['FirstAuthor']}\n\n˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙\n{row['DOI']}")
            list.append(["->",row['DOI']])
        except:
            file.write(f"-> {row['PublicationYear']} | {csv}\n\nTitle: {row['Title']}\n\nAuthor(s): {row['FirstAuthor']}\n\n˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙˙\n{row['DOI']}")
            list.append(["->",row['DOI']])
    id += 1
print(tabulate(list, headers=["Found", "DOI"], tablefmt="github"))
print(f"\ncheck ->",f"{path}/{folder}")
