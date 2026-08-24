# ==========================================================
# Task 07: Python Core Data Structures
# ==========================================================

print("=" * 60)
print("[+] INFRASTRUCTURE INVENTORY & DATA STRUCTURES")
print("=" * 60)

# ----------------------------------------------------------
# 1. LISTS: Ordered, Mutable, Allows Duplicates
# ----------------------------------------------------------
print("--- 1. Lists (Server Fleet Management) ---")
servers = ["web-01", "web-02", "db-01"]

# Adding elements
servers.append("cache-01")       # Adds to the end
servers.insert(1, "lb-01")       # Inserts at index 1

# Removing elements
removed_server = servers.pop()   # Removes last item ("cache-01")
servers.remove("web-02")         # Removes specific item by value

print(f"Updated Server List: {servers}")
print(f"Total Servers: {len(servers)}")
print(f"First Server: {servers[0]} | Last Server: {servers[-1]}")
print(f"Sliced Servers (First 2): {servers[0:2]}")

# ----------------------------------------------------------
# 2. TUPLES: Ordered, Immutable (Read-Only)
# ----------------------------------------------------------
print("\n--- 2. Tuples (Immutable System Constants) ---")
db_connection = ("postgres-prod.internal", 5432, "admin_user")

# Unpacking a tuple
host, port, user = db_connection
print(f"DB Host: {host} | Port: {port} | User: {user}")

# NOTE: Tuples cannot be modified! The following line would raise a TypeError:
# db_connection[1] = 3306

# ----------------------------------------------------------
# 3. DICTIONARIES: Key-Value Pairs, Fast O(1) Lookups
# ----------------------------------------------------------
print("\n--- 3. Dictionaries (Cloud Resource Metadata) ---")
instance = {
    "instance_id": "i-098abc123",
    "hostname": "api-gateway-prod",
    "cpu_cores": 8,
    "memory_gb": 32,
    "is_active": True,
    "tags": ["prod", "public-facing"]
}

# Accessing values safely with .get() (avoids KeyError if key missing)
print(f"Instance Hostname : {instance['hostname']}")
print(f"Region (with fallback) : {instance.get('region', 'us-east-1')}")

# Modifying and adding key-value pairs
instance["status"] = "RUNNING"
instance["memory_gb"] = 64  # Upgraded memory

# Iterating through key-value pairs using .items()
print("\nInstance Summary:")
for key, value in instance.items():
    print(f"  - {key:<12}: {value}")

# ----------------------------------------------------------
# 4. SETS: Unordered, Unique Elements Only (No Duplicates)
# ----------------------------------------------------------
print("\n--- 4. Sets (IP Whitelisting & Firewall Auditing) ---")
incoming_traffic_ips = [
    "192.168.1.10", "10.0.0.5", "192.168.1.10", 
    "172.16.0.2", "10.0.0.5", "192.168.1.50"
]

# Deduplicating list into a Set
unique_ips = set(incoming_traffic_ips)
print(f"Unique Incoming IPs ({len(unique_ips)}): {unique_ips}")

# Set Operations (Union, Intersection, Difference)
allowed_subnet = {"192.168.1.10", "192.168.1.50", "192.168.1.99"}

# Intersection (&): IPs present in both sets
authorized_traffic = unique_ips & allowed_subnet
print(f"Authorized Traffic (Intersection)  : {authorized_traffic}")

# Difference (-): IPs that are unauthorized
unauthorized_traffic = unique_ips - allowed_subnet
print(f"Unauthorized Traffic (Difference)   : {unauthorized_traffic}")