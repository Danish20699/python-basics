# ==========================================================
# Task: Dictionary Operations & Cloud Inventory
# ==========================================================

print("=" * 55)
print("[+] CLOUD INVENTORY MANAGEMENT")
print("=" * 55)

# 1. Define server metadata dictionary
database_node = {
    "service": "PostgreSQL",
    "host": "db-prod.internal",
    "port": 5432,
    "max_connections": 100,
    "ssl_enabled": True
}

# 2. Safe retrieval with .get()
backup_location = database_node.get("backup_s3_bucket", "default-backup-bucket")
print(f"Backup Bucket: {backup_location}")

# 3. Modifying dictionary
database_node["max_connections"] = 250  # Upgraded connection pool
database_node["version"] = "15.4"       # Added new field

# 4. Looping through with .items()
print("\n--- Current Node Configuration ---")
for key, val in database_node.items():
    print(f"{key:<18} : {val}")

# 5. Checking key existence
if "ssl_enabled" in database_node and database_node["ssl_enabled"]:
    print("\n🔒 Security Check: SSL is ACTIVE.")