#len() total number of items in a list

port = [22,33,80,443,8080]

total_ports=len(port)
print("Total Ports configured:", total_ports)


#Count() Frequncy of an item in a list
#counts how many times a specific
#values appears in a list

response_codes = [200, 404, 500, 200, 200, 403]

#Count how many times 200 (ok) and 404 (not found) appear in the list
ok_count = response_codes.count(200)
error_count = response_codes.count(404)


print(f"200 OK response:{ok_count}")
print(f"404 Not Found response:{error_count}")

print(f"503 Service Unavailable response:{response_codes.count(503)}")


#3. index() - Find the index of an item in a list
#finds the index(0-based position) of the first occurrence of a value in a list

servers = ["web01", "web02", "db-primary", "cache-01"]  

#Where is "db-primary" in the list?
db_index = servers.index("db-primary")

print(f"db-primary is at index: {db_index}")

#Always check if item  exists with 'in to avoid value Error

items_to_find = "cache-01"
if items_to_find in servers:
    print(f"{servers.index(items_to_find)}")
else:
    print(f"'{items_to_find}' is not in the list!")






#4. sort() Arranging in order (Ascending /Decending)
#sorts numbers from smallest to largest or strings aplhabetically
#Sorting the Numbers
latencies_ms = [45.2, 12.8, 89.1, 5.4, 23, 0]
#Acending (smallest to largest)
latencies_ms.sort()
print("Sorted Acending :", latencies_ms)
latencies_ms.sort(reverse=True)
print("Sorted Decending:", latencies_ms)


 
#Sorting alphabetically Strings----
regions= ["ws-west-1", "ap-south-1", "east-1"]
regions.sort()
print("Alphabetical :", regions)
#Note() modifies the list in-place if u want a sorted
#copy without changing the original list use
#sorted(my_list)



#5.reverse() Flipping the List
#Flips the elements of the list backwards from right to left

steps = ["1. Build","2. Test", "3. Package", "4. Deploy"]
steps.reverse()
print("Reversed Steps", steps)


#Practice: List Operation
#(Len, count, index, sort, reverse)

status_logs = ["SUCCESS", "FAILED", "SUCCESS", "SUCCESS", "PENDING", "FAILED"]
print("Original Logs:", status_logs)

#1. Len()
print("\n1. Total log entries:", len(status_logs))

#2. count()
print("\2. Total SUCCESS count:",status_logs.count("SUCCESS"))
print("   Total FAILED count  :", status_logs.count("Failed"))

# 3. index()
first_failure = status_logs.index("FAILED")
print(f"3. First FAILED job found at index: {first_failure}")

#4. reverse()
status_logs.reverse()
print("4 Logs reversed (newest to oldest):", status_logs)

#5. sort()
status_logs.sort()
print("5. Logs sorted alphabetically:", status_logs)
