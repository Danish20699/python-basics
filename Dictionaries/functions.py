#Functions allow you to write clean,resuable and mouduler code following the DRY
#Dont Repeat Yourself principal

#Core Concepts:Functions
#1 def keyword:Used to declare a functions
#2. Parameter vs Arguements:
#   .Parameter:The Variable listed inside in function definition
#eg def greet(name)

#   Argument:The actul value sent to the function when calling it
#eg greet("Danish")).
#return vs Print()
    #.print() just showstext on the terminal
#   return sends a value back to the caller so you can save it into a variable or pass it to another calculation.

#Default Parameter: Provide fallback values if no arguements is passed eg port=8080

#functio Definition
def calculate_monthly_cost(hourly_rate, hours=720):
    """Calculates hosting cost for a month (default: 720 hours)."""
    total = hourly_rate * hours
    return total 

# Function Call
cost_web = calculate_monthly_cost(0.25)          # Uses default 720 hours
cost_db = calculate_monthly_cost(0.75, hours=500) # Custom hours
print(f"Web Server Cost: ${cost_web:.2f}")  # $180.00
print(f"DB Server Cost : ${cost_db:.2f}")   # $375.00


#2. Default Parameters & Keyword Arguments
def deploy_service(service_name, environment="staging", replicas=1):
    print(f"Deploying'{service_name}' to [{environment.upper()}] with{replicas} replica(s)...")

# Positional call (uses defaults)
deploy_service("auth-service")

# Using defaults
deploy_service("auth-service")

# Using keyword arguments (order doesn't matter when named)
deploy_service(service_name="payment-api", replicas=3, environment="production")

# 3. Returning Multiple Values (Tuple Return)
#In Python, a function can return multiple values separated by commas:

def get_system_status():
    cpu = 45.0
    memory = 62.5
    status = "Healthy"
    return cpu, memory, status


#unpacking returned valus

cpu_val, mem_val, sys_status = get_system_status()
print(f"Status: {sys_status} | CPU: {cpu_val}% | Memory: {mem_val}%")


#4. *args and **kwargs (Variable Arguments)
#*args: Allows passing any number of positional arguments (captured as a tuple).
#**kwargs: Allows passing any number of keyword arguments (captured as a dictionary).


#1. *args Example (Flexible list of sercvers to ping)

def ping_servers(*servers):
    print("Pinging servers:")
    for server in servers:
        print(f"  -> Pinging {server}....")

ping_servers("web-01", "web-02", "db_01", "cache-01")

# 2. **kwargs Example (Flexible configuration tags)
def configure_instance(instance_id, **metadata):
    print(f"\nConfiguring Instance: {instance_id}")
    for key, value in metadata.items():
        print(f"  Tag: {key} = {value}")

    configure_instance("i-0123abc", env="prod", team="DevOps", owner="Danish")










# ==========================================================
# Task: Functions & Automation Helpers
# ==========================================================

print("=" * 60)
print("[+] SERVER HEALTH CHECK & DEPLOYMENT PIPELINE")
print("=" * 60)

# Helper Function 1: Check HTTP Status
def is_service_healthy(status_code):
    """Returns True if status is 200, otherwise False."""
    return status_code == 200

# Helper Function 2: Generate Server Alert Message
def create_alert(service_name, metric, value, threshold=80):
    """Generates an alert string if a metric exceeds the threshold."""
    if value > threshold:
        return f"🚨 [CRITICAL ALERT] {service_name} {metric} is at {value}% (Threshold: {threshold}%)"
    else:
        return f"✅ [NORMAL] {service_name} {metric} is safe at {value}%"

# --- Testing Our Functions ---

# Test 1: Service Health
api_status = 200
db_status = 503

print(f"API Gateway Healthy? : {is_service_healthy(api_status)}")
print(f"Database Healthy?    : {is_service_healthy(db_status)}")

# Test 2: Resource Alerts
print("\n--- Running System Threshold Checks ---")
print(create_alert("Web-Frontend", "CPU Usage", 88.5, threshold=75))
print(create_alert("DB-Cluster", "Disk Space", 65.0, threshold=80))



def backup_database(db_name, compress=True):
    """Simulates backing up a databse with optional compression"""
    print(f"Backing up database: {db_name}")

    if compress:
     print("compression: Enabled (.tar.gz)")
    else:
        print("Compression: Disabled (raw dump)")

    return


result = backup_database("users_db")
print(f"Status: {result}")
print()  # Empty line for spacing
result2 = backup_database("logs_db", compress=False)
print(f"Status: {result2}")

    