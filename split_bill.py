# Get number of people to split the bill
while True:
    try:
        number_of_people_splitting = int(input("Enter number of people to split bill with: "))
        break
    except ValueError:
        print("Invalid input")
        continue

# Get subtotal number
while True:
    try:
        subtotal = float(input("Enter subtotal amount: $"))
        break
    except ValueError:
        print("Invalid input")
        continue


# Get tax number
while True:
    try:
        tax_value = float(input("Enter tax amount: $"))
        break
    except ValueError:
        print("Invalid input")
        continue


# Get tip number
while True:
    try:
        tip_value = float(input("Enter tip amount: $"))
        break
    except ValueError:
        print("Invalid input")
        continue


# Get names and expenses for each person
def expense_collection(number):
    people_expense_book = {}
    for number in range(number):
        key = input("Enter name of person splitting: ")
        value = float(input("Enter how much they spent: $")) # Could possibly flesh this out to take individual purchases and add them up into the dictionary
        people_expense_book[key] = value
    return people_expense_book


# Add together tip and tax
def tip_tax_total(tip, tax):
    tip_tax_total_amount = tip + tax
    return tip_tax_total_amount


# Split bill
def split_bill(number, tip, tax, subtotal):
    people_expense_book = expense_collection(number)
    tip_tax_total_amount = tip_tax_total(tip, tax)
    for key, value in people_expense_book.items():
        percent_of_subtotal = value / subtotal
        total_expense = (percent_of_subtotal * tip_tax_total_amount) + value
        people_expense_book[key] = total_expense
    for key, value in people_expense_book.items():
        print(key, "owes", value)


split_bill(number_of_people_splitting, tip_value, tax_value, subtotal)