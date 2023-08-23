import requests
import sys
def fetch_and_write(doi, output_file):
    try:
        response = requests.get(f"https://doi.org/{doi}", headers={"Accept": "text/bibliography; style=bibtex"})
        if response.status_code == 200:
            with open(output_file, "a", encoding="utf-8") as file:
                file.write(response.text + "\n")
                print(f"{doi} f∂und :)")
        else:
            print(f"{doi} not dound :(")
    except Exception as e:
        print(f"Error {doi}: {e}")

def process_doi_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        dois = file.readlines()
        
    for doi in dois:
        doi = doi.strip()
        fetch_and_write(doi, output_file)

def main():
    while True:
        if len(sys.argv) != 3:
            print("Usage: python zotero.py <PATH> <.txt Name>")
            sys.exit(1)
        else:
            break
    
    path = sys.argv[1]
    txt = sys.argv[2]
    bib = sys.argv[2]
    input_file = f"{path}/{txt}.txt"
    output_file = f"{path}/{bib}.bib"
    
    process_doi_file(input_file, output_file)
    
    print("Done! ∂")

if __name__ == "__main__":
    main()
