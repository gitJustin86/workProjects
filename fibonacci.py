# Install pip
# sudo apt-get install pip

# Install xlsxwriter
# sudo pip install xlsxwriter

# Import module
import xlsxwriter

# Create an xlsx file
workbook = xlsxwriter.Workbook("data.xlsx")

# Add a new worksheet
worksheet = workbook.add_worksheet()

# Definte rows and columns
row = 0
column = 0

# Data
fibonacci = [1,1]

# Ask user how many fibonacci numbers they want?
x = int(input("Max fibonacci numbers? "))

# Populate cells
for number in range(0, x):

    # Write
    if (number == 0):
        worksheet.write(row, column, fibonacci[0])
    elif (number == 1):
        worksheet.write(row, column, fibonacci[1])
    else:
        newNumber = fibonacci[number-2]+fibonacci[number-1]
        worksheet.write(row, column, newNumber)
        fibonacci.append(newNumber)

    # Iterate
    row += 1

# Close your workbook
workbook.close()
