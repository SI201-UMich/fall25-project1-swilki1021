import csv

# --- Keep your original base reading block exactly as requested ---
with open('SampleSuperstore.csv', 'r') as dataset:
    csv_reader = csv.reader(dataset)
    header = next(csv_reader)
    for row in csv_reader:
        # do stuff
        print(row)

# -----------------------
# Part 1: Read & analyze

with open('SampleSuperstore.csv', 'r', encoding='utf-8') as dataset:
    csv_reader = csv.reader(dataset)
    header = next(csv_reader)

    # 1) List of variables 
    print("\nColumns in dataset:", header)

    # 2) Sample entry 
    try:
        sample_row = next(csv_reader)
        print("\nSample row:", sample_row)
    except StopIteration:
        print("\nDataset has no data rows.")

    # 3) Number of rows 
    row_count = 0
    for _ in csv_reader:
        row_count += 1
    # If we successfully read a sample_row above, add 1 to include it
    try:
        if sample_row:
            row_count += 1
    except NameError:
        pass

    print("\nTotal number of rows (excluding header):", row_count)


