# Student Name - Neil Khan
# Date - 23 June 2026
# Program Description - Personal Expense Tracker (Week 4 Assignment)
# Tier Level - Base Level

import os
import datetime


# Expense Records
def build_record(description, amount, category):
    today = str(datetime.date.today())

    # Description
    short_description = description[:30]

    # Amount
    formatted_amount = f"{amount:.2f}"

    # Comma-separated record
    record = ",".join(
        [today, short_description, formatted_amount, category]
    )

    return record


# Save records to the expenses file
def save_record(filename, record):
    with open(filename, "a") as expense_file:
        expense_file.write(record + "\n")


# Load all records from the expenses file
def load_records(filename):

    records = []

    try:
        with open(filename, "r") as expense_file:

            for line in expense_file:

                line = line.strip()

                if line == "":
                    continue

                record_fields = line.split(",")

                records.append(record_fields)

    except FileNotFoundError:
        return []

    return records


# Display records in a formatted table
def display_records(records):

    print("\n===== Expense Records =====")

    if len(records) == 0:
        print("No expenses on record yet.")
        return

    print(
        f"{'Date':<12}"
        f"{'Description':<32}"
        f"{'Amount':<12}"
        f"{'Category':<15}"
    )

    print("-" * 71)

    for record in records:

        date = record[0]
        description = record[1]
        amount = record[2]
        category = record[3]

        print(
            f"{date:<12}"
            f"{description:<32}"
            f"${amount:<11}"
            f"{category:<15}"
        )


# ---------------------------
# Main Program
# ---------------------------

filename = "expenses.txt"

# Greeting
print("\n" + "=" * 60)
print("Welcome to the Personal Expense Tracker app!")
print("=" * 60)

# OS module
if not os.path.exists(filename):
    print("Expense file does not exist yet. A new file will be created when you add records.")

# Load and display existing records
expense_records = load_records(filename)
display_records(expense_records)

# Ask user how many expenses to add
number_of_expenses = int(
    input("\nHow many expenses do you want to add? ")
)

# Collect new expenses
for expense_number in range(1, number_of_expenses + 1):

    print(f"\n--- Expense {expense_number} ---")

    description = input("Description: ").strip()

    amount = float(
        input("Amount: ")
    )

    category = input(
        "Category: "
    ).strip()

    # Build record string
    expense_record = build_record(
        description,
        amount,
        category
    )

    # Save record
    save_record(
        filename,
        expense_record
    )

# Reload and display updated records
updated_records = load_records(filename)

print("\n===== Updated Expense Records =====")
display_records(updated_records)
