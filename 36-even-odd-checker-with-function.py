# ==========================================================
# Task 36: Even/Odd Checker with Function
# ==========================================================

#def check_even_odd(number):
    #if number % 2 == 0:
       # return "Even"
    #else:
        #return "Odd"

# Single number check
#num = int(input("Enter a number: "))
#print(f"{num} is {check_even_odd(num)}")

# Check a list of numbers
#numbers = [10, 23, 44, 57, 68]
#print("\n--- Batch Check ---")
#for n in numbers:
    #print(f"{n} -> {check_even_odd(n)}")


# 1. Basic Even/Odd Checker Function
def check_even_odd(number):
    """Checks if a number is even or odd and returns the result."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# 2. Batch Checker Function (takes a list)
def batch_check(numbers):
    """Checks a list of numbers and returns a dictionary of results."""
    results = {}
    for num in numbers:
        results[num] = check_even_odd(num)
    return results
# 3. Counter Function
def count_even_odd(numbers):
    """Counts how many even and odd numbers are in a list."""
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
# ============ Testing Our Functions ============
print("=" * 50)
print("[+] EVEN / ODD CHECKER")
print("=" * 50)
# Single number check
print("\n--- Single Number Check ---")
num = int(input("Enter a number: "))
result = check_even_odd(num)
print(f"{num} is {result}")
# Batch check with a predefined list
print("\n--- Batch Check ---")
sample_list = [10, 23, 44, 57, 68, 91, 100]
print(f"{'NUMBER':<10} | {'RESULT':<10}")
print("-" * 25)
results = batch_check(sample_list)
for number, status in results.items():
    print(f"{number:<10} | {status:<10}")
# Count summary
even, odd = count_even_odd(sample_list)
print(f"\n--- Summary for {sample_list} ---")
print(f"Even numbers : {even}")
print(f"Odd numbers  : {odd}")
print(f"Total        : {len(sample_list)}")
print("\n" + "=" * 50)
print("[+] Done!")
print("=" * 50)