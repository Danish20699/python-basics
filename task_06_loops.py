#=================================================
# Task 06: Loops in Python
#(Devops & Automation Use Cases)

print("=" * 50)
print("[+] SERVER FLEET & RETRY AUTOMATION (LOOPS)")
print("=" * 60)


#------------------------1. Basic for loop with a List------------------------

servers = ["web01", "web02", "db-primary", "cache-01", "api-gateway"]

print("------1. Iterating over server Fleet---")
for server in servers:
    print(f"[PING] Sending heartbeat to: {server}.internal")

    #--------------2. Using range() for Controlled Iteration------------------------
    print("\n----2. Staged Development with rage() ---")
    print(f"eploying application payload to cluster Batch #{batch_number}...")


    #-----------3.Using enemerate() to get index and value------------------------
    print("\n---3. Using enemerate() for ordered logs---")

    for index, sevice in enemerate(microservices, start=1):
        print(f"[{index}/{len(microservices)}] Booting up microservice: {sevice}...")


        4#-----------4. Using while loop for retry mechanism------------------------
        print("\n---4. Polling service Health with 'while' loop--")
        max_retries = 5
        current_attempt = 1
        is_service_up = False

        while current_attempt <= max_retries:
            print(f"Helth Check attempt{current_attempt}/{max_retries}...")

            # Simulate a health check (replace with actual check in real scenarios)
            if current_attempt == 3:
                is_service_up = True
                print("Service is UP and running!")
                break

            #immediately

            current_attempt += 1

            if not is_service_up:
                print("[FAILED] Service failed to respond within retry limit.")

            # 5. Loop Control: 'continue' (Skipping Iterations)
# ----------------------------------------------------------
print("\n--- 5. Filtering Nodes with 'continue' ---")
nodes = [
    {"name": "worker-1", "status": "active"},
    {"name": "worker-2", "status": "maintenance"},
    {"name": "worker-3", "status": "active"},
    {"name": "worker-4", "status": "offline"},
]
for node in nodes:
    # Skip any node that is not active
    if node["status"] != "active":
        print(f"[SKIP] Skipping {node['name']} (Reason: {node['status']})")
        continue
    
    print(f"[RUN] Executing job on {node['name']}...")


