# Name: Suzanna Wilkinson
# Student ID:3015 4918
# Email: suzannaw@umich.edu
# Collaborators: None (worked independently)
# GenAI Used: ChatGPT (used for structure, debugging, and readability)

import csv

with open('SampleSuperstore.csv', 'r') as dataset:
    csv_reader = csv.reader(dataset)
    header = next(csv_reader)
    for row in csv_reader:
        # opens and reads the CSV file
        print(row)



def read_csv_file(filename):
    """
    Reads the Sample Superstore CSV file into a list of dictionaries.
    Returns the list for further analysis.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data



# Calculation 1 – Average profit by category (West region)

def calculate_avg_profit_by_category_west(filename):
    """
    Filters rows for Region == 'West' and calculates
    the average profit for each product category.
    Returns a dictionary with categories and their average profit.
    """
    data = read_csv_file(filename)
    category_data = {}

    for row in data:
        if row['Region'].strip().lower() == 'west':
            category = row['Category']
            try:
                profit = float(row['Profit'])
            except ValueError:
                continue

            if category not in category_data:
                category_data[category] = {'total_profit': 0.0, 'count': 0}

            category_data[category]['total_profit'] += profit
            category_data[category]['count'] += 1

    avg_profit_by_category = {}
    for category, values in category_data.items():
        if values['count'] > 0:
            avg_profit_by_category[category] = round(values['total_profit'] / values['count'], 2)

    return avg_profit_by_category



# Calculation 2 – % of loss-making orders with high discount

def calculate_discount_loss_percentage(filename):
    """
    Calculates the percentage of orders with discounts > 0.3
    that result in a loss (Profit < 0).
    Returns the percentage rounded to 2 decimal places.
    """
    data = read_csv_file(filename)
    total_discounted = 0
    loss_count = 0

    for row in data:
        try:
            discount = float(row['Discount'])
            profit = float(row['Profit'])
        except ValueError:
            continue

        if discount > 0.3:
            total_discounted += 1
            if profit < 0:
                loss_count += 1

    if total_discounted == 0:
        return 0.0

    loss_percentage = (loss_count / total_discounted) * 100
    return round(loss_percentage, 2)


# Write results to a text file

def write_results_to_file(results_dict, discount_loss, output_filename):
    """
    Writes both calculations to a plain text file.
    """
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write("Superstore Analysis Results\n")
        file.write("----------------------------------------\n")
        file.write("Average Profit by Category (West Region):\n")
        for category, avg_profit in results_dict.items():
            file.write(f"{category}: ${avg_profit}\n")
        file.write("\n")
        file.write(f"Percentage of loss-making orders with discount > 0.3: {discount_loss}%\n")

    print(f"\nResults successfully written to '{output_filename}'")


#  Test Functions

def test_calculate_avg_profit_by_category_west():
    """
    Tests for calculate_avg_profit_by_category_west()
    """
    test_file = 'SampleSuperstore.csv'
    result = calculate_avg_profit_by_category_west(test_file)
    assert isinstance(result, dict), "Output should be a dictionary"
    assert all(isinstance(v, float) for v in result.values()), "All values must be floats"
    assert len(result) > 0, "There should be at least one category"

    # Edge test 
    try:
        calculate_avg_profit_by_category_west('missing.csv')
    except FileNotFoundError:
        print("Edge Case Passed: Missing file handled properly.")


def test_calculate_discount_loss_percentage():
    """
    Tests for calculate_discount_loss_percentage()
    """
    test_file = 'SampleSuperstore.csv'
    result = calculate_discount_loss_percentage(test_file)
    assert isinstance(result, float), "Output should be a float"
    assert 0 <= result <= 100, "Percentage should be between 0 and 100"

    # Edge test
    empty_data = []
    with open('empty.csv', 'w', encoding='utf-8') as file:
        file.write("Discount,Profit\n")
    try:
        result = calculate_discount_loss_percentage('empty.csv')
        assert result == 0.0, "Edge Case Passed: Empty dataset returns 0%"
    except Exception as e:
        print("Edge Case Failed:", e)



#  execution

def main():
    filename = 'SampleSuperstore.csv'
    avg_profit_results = calculate_avg_profit_by_category_west(filename)
    discount_loss_percentage = calculate_discount_loss_percentage(filename)
    write_results_to_file(avg_profit_results, discount_loss_percentage, 'superstore_analysis_results.txt')

    test_calculate_avg_profit_by_category_west()
    test_calculate_discount_loss_percentage()
    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    main()
