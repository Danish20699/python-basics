# ==========================================================
# Task: Tuples (Constants) & Sets (Security Whitelisting)
# ==========================================================

print("=" * 60)
print("[+] INFRASTRUCTURE SECURITY & ACCESS CONTROL")
print("=" * 60)

# --- TUPLE: Immutable Server Profile ---
server_profile = ("aws", "us-east-1", "t3.large", 443)
provider, region, instance_type, secure_port = server_profile

print(f"Deploying on {provider.upper()} ({region}) using {instance_type} on port {secure_port}")

# --- SETS: Access Control List (ACL) Audit ---
allowed_ssh_users = {"admin", "danish", "deploy_bot"}
current_active_logins = ["danish", "guest", "admin", "danish", "hacker_123"]

# 1. Deduplicate active logins
unique_active_users = set(current_active_logins)
print(f"\nUnique Active Users ({len(unique_active_users)}): {unique_active_users}")

# 2. Find Authorized Logins (Intersection)
authorized_logins = unique_active_users & allowed_ssh_users
print(f"✅ Authorized Logins : {authorized_logins}")

# 3. Find Unauthorized Logins / Intruders (Difference)
unauthorized_logins = unique_active_users - allowed_ssh_users
print(f"🚨 Unauthorized Logins (Flagged): {unauthorized_logins}") 


