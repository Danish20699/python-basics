# ==========================================================
# Task 04: User Input & Modern F-Strings
# ==========================================================

print("=" * 55)
print("[+] INTERACTIVE SERVER CONFIGURATION SETUP")
print("=" * 55)

# 1. Taking User Inputs (Remember: input() returns str)
server_name = input("Enter server name (e.g. web-app-01): ")
cpu_cores = int(input("Enter number of CPU cores (e.g. 4): "))
hourly_rate = float(input("Enter hourly hosting rate in $ (e.g. 0.85): "))

# 2. Performing Calculations with converted numbers
hours_per_month = 24 * 30  # 720 hours in a month
monthly_cost = hourly_rate * hours_per_month

# 3. Modern F-String Formatting
print("\n" + "=" * 55)
print("[*] PROVISIONING SUMMARY REPORT")
print("=" * 55)

# :.2f  -> 2 decimal places
# :,.2f -> thousands separator with commas
print(f"Server Hostname  : {server_name}")
print(f"Allocated Cores  : {cpu_cores} vCPUs")
print(f"Hourly Cost      : ${hourly_rate:.2f}")
print(f"Est. Monthly Cost: ${monthly_cost:,.2f}")

# 4. Formatted Table / Column Alignment
print("\n--- Capacity Metrics ---")
print(f"{'METRIC':<20} | {'VALUE':<15}")
print("-" * 38)
print(f"{'Total Compute':<20} | {f'{cpu_cores * 2.5:.1f} GHz':<15}")
print(f"{'Memory Est.':<20} | {f'{cpu_cores * 4} GB RAM':<15}")
print(f"{'Status':<20} | {'READY TO DEPLOY':<15}")
