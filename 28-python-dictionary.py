#The next data structure are Dictionaries(dict)

#In Devops, cloud,and backed automation,Dicionaries are used constantly to handle JSON Payloads
#server configuration,API response,and environment settings

#what is Dictionary?
#A dictionary stores data in key: value pairs inside curly braces{}
#`key`:A umique identifier (usually a string or integer)
#`VALUE`:aNY DATA TYPE (String, number,list or even another dictionary)
#Lookups are extremly fast(0(1) time complexity

#Server configuration Dictionary
server = {
     "hostname": "web-prod-01",
    "ip_address": "192.168.1.50",
    "port": 8080,
    "is_active": True
}

# 2. Print the whole dictionary
print("Server Info:", server)
# 3. Print specific values
#print("Hostname   :", server["hostname"])
#print("Port Number:", server.get("port"))

#1. Acess the key using square brackets
print("Hostname:",
      server["hostname"])

#2. Acess safely using .get()
#-> avoids crash if key is missing
print("port:", server.get("port"))
print("region:", server.get("region", "us-east-1"))
#Returns default 'us-east-1 if the region doesn't exist



#-------------------------------------
#2. Adding updating Modifying

server = {"hostname": "web-prod-01",
           "port:": 8080}

#Adding new key value pair
server["environment"] = "production"

#updatig an existing value
server["port"] = 443

#updating an existing keys at once using .update()

server.update({"status": "RUNNING", "cpu_cores": 4})

print(server)


#---------------------------------
#Removes Keys
#.pop():Removes the key and returns its value.
#del dict[key]:Delete the key directly

config = {"env": "dev", "debug": True, "secret_key": "12345"}

# Remove and capture value
removed_secret = config.pop("secret_key")
print(f"Removed secret: {removed_secret}")

# Delete with 'del'
del config["debug"]

print("Updated config:", config)
# Output: {'env': 'dev'}



#------------------------------------------
#The 3 Essential Dictionary
#  Methods: .keys(), .values(), .items()
metrics = {"cpu": "45%", "memory": "78%", "disk": "60%"}

# 1. .keys() -> All the keys
print("Keys  :", list(metrics.keys()))
# Output: ['cpu', 'memory', 'disk']

# 2. .values() -> All the values
print("Values:", list(metrics.values()))
# Output: ['45%', '78%', '60%']

# 3. .items() -> Key-Value pairs (best for looping!)
for key, value in metrics.items():
    print(f"Metric [{key.upper()}]: {value}")




#---------------######################
#5 Nested Dictionaries (Real-World Cloud / API Example)


# Simulating a cloud instance JSON object
cloud_instance = {
    "id": "i-0987654321",
    "type": "t3.medium",
    "specs": {
        "vcpus": 2,
        "ram_gb": 4,
        "storage_gb": 50
    },
    "tags": ["web", "production", "public"]
}

# Accessing nested data:
print("Instance Type:", cloud_instance["type"])
print("vCPUs        :", cloud_instance["specs"]["vcpus"])
print("First Tag    :", cloud_instance["tags"][0])