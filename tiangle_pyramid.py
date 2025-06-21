number_of_rows = int(input("Enter number of rows: "))

def number_triagle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

number_triagle(number_of_rows)