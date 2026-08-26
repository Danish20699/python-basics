# Accessing list elements by index
fruits = ["apple", "banana", "orange", "grape"]
print(fruits[0])    # apple
print(fruits[-1])   # grape
print(fruits[-2])   # orange

# Iterating over a List
colors = ["red", "green", "blue"]
for color in colors:
    print(f"Color: {color}")

# Iterating over a String (character by character)
word = "Python"
for letter in word:
    print(letter, end=" ")

print()  # New line

# Iterating with index using enumerate()
tools = ["git", "docker", "linux"]
for index, tool in enumerate(tools):
    print(f"{index}: {tool}")




#Concatnation

frontend = ["html", "Css", "Js",]
backend  = ["python", "djano",]


full_stack = frontend + backend
print(full_stack)

#Concatenating Strings
first = "hello"
second = "world"
combined = first + " " + second
print(combined)

dashes = "-" * 30
print(dashes)

nums = [0] * 5
print(nums)


#The in Operator
#Checks if an item exists inside a sequence. Returns True or False.

#'in with Lists

servers = ["web-01", "db-01", "cache-01"]
print("web-01" in servers)

#'not in
print("api-01" not in servers)

#in with Strings (checks for substring)

filename = "backup_2025_08_26.tar.gz"
print(".tar.gz" in filename)
print(".zip" in filename)

#in with Dictionaries Checks KEYS only!
config = {"host": "localhost", "port": 8080}

print("host" in config)
print("localhost" in config)

#6 Sequence Unpacking & Assigment
#Assigning multiple values from a sequence into seprate variable in 
#ONE LINE

#Basic Unpacking from a LIst
server_info = ["web-prod-01", "192.168.1.10", 443]

hostname, ip, port = server_info
print(f"Host: {hostname}")
print("fIP : {ip}")
print(f"Port: {port}")

#Unpacking from a Tuple 
cordinates = (28.6139, 77.2090)
lat, lng = cordinates 
print(f"Latitude: {lat}, Longitude", [lng])

#swaping two variables
a = 10
b = 20
a, b = b, a
print(f"a = {a}, b = {b}")

scores = [95,88,60,45]
first, second, *rest = scores

print(f"Top 1 :{first}")
print(f"Top 2 : {second}")
print(f"others : {rest}")


#. Sets (Recap with Simple Examples)
#Unordered collection with no duplicates. Great for uniqueness and fast lookups.
# Creating a Set
skills = {"python", "linux", "docker", "python"}  # duplicate 'python' ignored
print(skills)  # {'python', 'linux', 'docker'}

# Creating a Set from a List (deduplication)
raw_data = [1, 2, 2, 3, 3, 3, 4]
unique_data = set(raw_data)
print(unique_data)  # {1, 2, 3, 4}

# Adding & Removing
skills.add("git")
skills.discard("linux")     # Safe remove (no error if missing)
print(skills)

# Set Operations
team_a = {"Alice", "Bob", "Charlie"}
team_b = {"Bob", "David", "Eve"}

print(team_a | team_b)   # Union:        All members combined
print(team_a & team_b)   # Intersection: Common members -> {'Bob'}
print(team_a - team_b)   # Difference:   Only in team_a -> {'Alice', 'Charlie'}

# Membership check (very fast!)
blocked = {"1.1.1.1", "2.2.2.2"}
print("1.1.1.1" in blocked)   # True
print("8.8.8.8" in blocked)   # False