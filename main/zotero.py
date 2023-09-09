import requests
import sys
import os

def fetch_and_write(doi, output_file):
    """
    Fetches bibliographic information for a DOI and writes it to the output file.
    """
    try:
        response = requests.get(f"https://doi.org/{doi}", headers={"Accept": "text/bibliography; style=bibtex"})
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 200:
            with open(output_file, "a", encoding="utf-8") as file:
                file.write(response.text + "\n")
                print(f"➜ {doi} found :)")
        else:
            print(f"➜ {doi} not found :(")
    except requests.exceptions.RequestException as e:
        print(f"➜ {doi} not found :(")
    except Exception as e:
        print(f"➜ {doi} not found :(")

def process_doi_file(input_file, output_file):
    """
    Processes a list of DOIs from an input file and fetches bibliographic data for each DOI.
    """
    with open(input_file, "r", encoding="utf-8") as file:
        dois = file.readlines()
        
    for doi in dois:
        doi = doi.strip()
        fetch_and_write(doi, output_file)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <PATH> <file.txt>")
        sys.exit(1)

    path = sys.argv[1]
    input_file_name = sys.argv[2]
    output_file_name = input_file_name.replace(".txt", ".bib")

    input_file = os.path.join(path, input_file_name)
    output_file = os.path.join(path, output_file_name)
    
    process_doi_file(input_file, output_file)
    
    print("Done!")

if __name__ == "__main__":
    main()
