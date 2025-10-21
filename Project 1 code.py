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


def calculate_avg_profit_by_category(filename):
    """
    Calculates the average profit for each product category in the dataset.
    Uses 'Category', 'Sales', and 'Profit' columns.
    Returns a dictionary with category names as keys and average profit as values.
    """
    category_data = {}

    with open(filename, 'r', encoding='utf-8') as dataset:
        csv_reader = csv.DictReader(dataset)

        for row in csv_reader:
            category = row['Category']
            try:
                profit = float(row['Profit'])
                sales = float(row['Sales'])
            except ValueError:
                
                continue

            if category not in category_data:
                category_data[category] = {'total_profit': 0.0, 'total_sales': 0.0, 'count': 0}

            category_data[category]['total_profit'] += profit
            category_data[category]['total_sales'] += sales
            category_data[category]['count'] += 1

    
    avg_profit_by_category = {}
    for category, values in category_data.items():
        if values['count'] > 0:
            avg_profit_by_category[category] = round(values['total_profit'] / values['count'], 2)

    return avg_profit_by_category



results = calculate_avg_profit_by_category('SampleSuperstore.csv')
print("\nAverage Profit by Category:")
for cat, avg_profit in results.items():
    print(f"{cat}: ${avg_profit}")


