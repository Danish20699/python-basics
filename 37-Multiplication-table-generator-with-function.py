# ==========================================================
# Task 37: Multiplication Table Generator with Function
# ==========================================================

def print_table(number,limit=10):
    """Prints the multiplication table of a given number up to a limit."""
    print(f"\n--- Multiplication Table for {number} (1 to {limit}) ---")

    for i in range(1,limit + 1):
        print(f"{number} x {i} = {number*i}")

# Get input from user
num = int(input("Enter a number to print its multiplication table: "))

print_table(num)
    