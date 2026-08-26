#Indexing
servers = ["web-01", "db-01", "cache-01"]

print(servers[0])   # web-01
print(servers[1])   # db-01
print(servers[2])   # cache-01

#With Loop (using range + index):
servers = ["web-01", "db-01", "cache-01"]

for i in range(len(servers)):
    print(f"Index {i} -> {servers[i]}")

# Output:
# Index 0 -> web-01
# Index 1 -> db-01
# Index 2 -> cache-01

#Slicing
ports = [22, 80, 443, 3306, 8080]

first_three = ports[0:3]
print(first_three)   # [22, 80, 443]

#ports = [22, 80, 443, 3306, 8080]


#With Loop (looping through a slice):
print("First 3 ports:")
for port in ports[:3]:
    print(f"  Port: {port}")

# Output:
#   Port: 22
#   Port: 80
#   Port: 443

#Iterating
#Basic (for loop):
#
tools = ["git", "docker", "linux"]

for tool in tools:
    print(tool)

#With enumerate() loop (index + value):
tools = ["git", "docker", "linux"]

for index, tool in enumerate(tools, start=1):
    print(f"{index}. {tool}")

# Output:
# 1. git
# 2. docker
# 3. linux

print("--------------------------------")
#With while loop:
tools = ["kubernates", "system_design", "linux"]

i = 0
while i < len(tools):
    print(f"Tool: {tools[i]}")
    i += 1

print("--------------------------------")


#Concatenation
list_aa = [1, 2, 3]
list_b = [4, 5, 6]
combined = list_aa + list_b
print(combined)  # [1, 2, 3, 4, 5, 6]





print("--------------------------------")
#With Loop (building a combined list manually):
list_a = [1, 2, 3]
list_b = [4, 5, 6]

combined = []
for item in list_a:
    combined.append(item)
for item in list_b:
    combined.append(item)

print(combined)  # [1, 2, 3, 4, 5, 6]

# The in Operator
print("--------------------------------")


#The in Operator
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("mango" in fruits)

#With Loop (checking multiple items at once):

fruits = ["apple", "banana", "cherry"]

shopping_list = ["banana", "mango", "apple", "grapes"]

for item in shopping_list:
    if item in fruits:
        print(f"✅ '{item}' is available")
    else:
        print(f"❌ '{item}' is not available" )




print("--------------------------------")
#Unpacking
server = ("web-01", "192.168.1.10", 443)
name, ip, port = server

print(f"Name: {name}, ip: {ip}, Port: {port}")

#With Loop (unpacking inside a loop — very common!):
servers = [
    ("web-01", "192.168.1.10"),
    ("db-01", "192.168.1.20"),
    ("cache-01", "192.168.1.30"),
]
for name, ip in servers:
    print(f"Server: {name} -> IP: {ip}")


#Sets
#server = ("web-01", "192.168.1.10")   # 2 items

#name, ip = server   # Works! 2 = 2
#print(f"Name: {name}, IP: {ip}")

#With Loop (unpacking inside a loop — very common!):
#servers = [
    #("web-01", "192.168.1.10"),
    #("db-01", "192.168.1.20"),
    #("cache-01", "192.168.1.30"),


#for name, ip in servers:
   # print(f"Server: {name} -> IP: {ip}")

# Output:
# Server: web-01 -> IP: 192.168.1.10
# Server: db-01 -> IP: 192.168.1.20
# Server: cache-01 -> IP: 192.168.1.30
















