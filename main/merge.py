import sys
import os

def merge_and_remove_duplicates(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = set(f1.readlines())
        lines2 = set(f2.readlines())

    merged_lines = lines1.union(lines2)

    with open(output_file, 'w') as merged_file:
        merged_file.writelines(sorted(merged_lines))

if len(sys.argv) != 4:
    print("Usage: python {} <PATH> <file1.txt> <file2.txt>".format(sys.argv[0]))
    sys.exit(1)

path = sys.argv[1]
f1 = sys.argv[2]
f2 = sys.argv[3]

file1 = os.path.join(path, f1)
file2 = os.path.join(path, f2)
output_file = os.path.join(path, 'merged.txt')

if not os.path.isfile(file1) or not os.path.isfile(file2):
    print("Both input files must exist.")
    sys.exit(1)

merge_and_remove_duplicates(file1, file2, output_file)
print("Merged {} and {} into {} and removed duplicates.".format(f1, f2, 'merged.txt'))
