
# 1. Star Pattern Code
def print_star_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

def main_star():
    n = int(input("Enter the number of rows you want to print (star pattern): "))
    print_star_pattern(n)

# 2. Number Pattern Code
def print_number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main_number():
    n = int(input("Enter the number of rows you want to print (number pattern): "))
    print_number_pattern(n)

# 3. Reverse Number Pattern Code
def reverse_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main_reverse():
    n = int(input("Enter the number of rows you want to print (reverse number pattern): "))
    reverse_pattern(n)

# Uncomment one of the below to run the desired pattern:
# main_star()
# main_number()
# main_reverse()
