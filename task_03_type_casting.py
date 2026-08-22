# ==========================================================
# Task 03: Type Casting & Conversions
# ==========================================================

# 1. Implicit Conversion (Python handles it automatically)
int_num = 10
float_num = 4.5
result = int_num + float_num  # 10 + 4.5 = 14.5
print("--- 1. Implicit Conversion ---")
print("Result:", result, "| Type:", type(result))

# 2. Explicit Conversion (String to Number)
print("\n--- 2. String to Numbers ---")
port_str = "8080"
port_num = int(port_str)      # Convert to int
print(f"Port String: '{port_str}' -> Port Int: {port_num} ({type(port_num)})")

latency_str = "23.45"
latency_float = float(latency_str) # Convert to float
print(f"Latency Float: {latency_float} ({type(latency_float)})")

# 3. Truncating Decimals with int()
print("\n--- 3. Float to Int (Truncation) ---")
score = 99.85
score_int = int(score)        # Notice: It cuts off .85 (does NOT round up)
print(f"Original Float: {score} -> Truncated Int: {score_int}")

# 4. Number to String Concatenation
print("\n--- 4. Number to String ---")
users_count = 500
message = "Total registered users: " + str(users_count)
print(message)

# 5. Truthy vs Falsy in Python
print("\n--- 5. Truthy vs Falsy Values ---")
print("bool(0)     ->", bool(0))        # 0 is False
print("bool('')    ->", bool(""))       # Empty string is False
print("bool(None)  ->", bool(None))     # None is False

print("bool(100)   ->", bool(100))      # Non-zero number is True
print("bool('Dev') ->", bool("Dev"))    # Non-empty string is True
