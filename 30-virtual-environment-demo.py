# ==========================================================
# Task 30: Virtual Environment Inspection & Verification
# ==========================================================
# This script programmatically checks if it is running inside
# an isolated Virtual Environment (venv) and inspects runtime
# paths, Python version, and system details.
# ==========================================================

import sys
import os
import platform

print("=" * 60)
print("[+] PYTHON RUNTIME & ENVIRONMENT INSPECTOR")
print("=" * 60)

# 1. Detect if running inside a Virtual Environment
# When a venv is active: sys.prefix (venv path) != sys.base_prefix (global Python path)
is_in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)

# 2. Key Environment Details
python_version = platform.python_version()
executable_path = sys.executable
environment_path = sys.prefix
base_python_path = getattr(sys, "base_prefix", sys.prefix)

# 3. Formatted Environment Report
print("\n" + "=" * 60)
print("[*] ENVIRONMENT STATUS REPORT")
print("=" * 60)

status_badge = "[ACTIVE] Isolated Virtual Environment (venv)" if is_in_venv else "[INACTIVE] Global System Python"
print(f"{'STATUS':<20} | {status_badge}")
print("-" * 60)
print(f"{'Python Version':<20} | {python_version}")
print(f"{'Platform':<20} | {platform.system()} {platform.release()} ({platform.machine()})")
print(f"{'Current Executable':<20} | {executable_path}")
print(f"{'Active Prefix':<20} | {environment_path}")
print(f"{'Base Python Prefix':<20} | {base_python_path}")
print("-" * 60)

# 4. Check Site-Packages Search Paths
print("\n--- Site-Packages Search Paths (sys.path) ---")
for index, path in enumerate(sys.path, start=1):
    if "site-packages" in path.lower():
        print(f"  [{index}] (Packages Dir) -> {path}")
    else:
        print(f"  [{index}] -> {path}")

# 5. Summary Message
print("\n" + "=" * 60)
if is_in_venv:
    print("[+] Status: You are safely running inside an isolated venv!")
    print("    Packages installed with `pip install` stay inside this project.")
else:
    print("[!] Status: You are currently using the Global Python installation.")
    print("    Tip: Create & activate a venv (`python -m venv .venv`).")
print("=" * 60)

