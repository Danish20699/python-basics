#fruits = ["apple", "banana", "cherry", "date", "berry"]
#indexing  0       1        2     3       4      

#print(fruits[0])
#print(fruits[1])


#Negative index counts items from the end of the list
#print(fruits[-1])  # Last item
#print(fruits[-2])  # Second to last item


tools = ["git", "docker", "kubernetes", ]

tools[2] = "helm"  # Update the third item

print(tools)  # Output: ['git', 'docker', 'helm']

servers = ["web01", "web02", ]

#at the end of the list
servers.append("db-primary")  # Add a new server at the end

#insert at index 1
servers.insert(1, "db-01")
print(servers)




#5. Removing Items
#.remove(value): Removes by name.
#.pop(): Removes the last item (or at a specific index).
#
#
#
#
#
#
colors = ["red", "green", "blue", "yellow"]

# 1. Remove by name
colors.remove("green")
print(colors)  
# Output: ['red', 'blue', 'yellow']

# 2. Remove the last item with .pop()
last_color = colors.pop()
print(f"Removed: {last_color}")  # Removed: yellow
print(colors)                    # Output: ['red', 'blue']




#6. Finding the Length (len)
#Use len() to count how many items are in the list:
#
#
#
#
#
#
tasks = ["setup", "test", "deploy", "monitor"]

print("Total tasks:", len(tasks))
# Output: Total tasks: 4



# Looping Through a List
users = ["Alice", "Bob", "Charlie"]

for user in users:
    print(f"Welcome, {user}!")

# Output:
# Welcome, Alice!
# Welcome, Bob!
# Welcome, Charlie!


#Checking if an Item Exists (in)
#Use the in keyword:

allowed_users = ["admin", "developer", "tester"]

if "admin" in allowed_users:
    print("Access Granted!")
else:
    print("Access Denied!")


    # Quick Practice Script
#You can copy and test this small complete example:
# Easy List Practice
my_skills = ["Python", "Linux", "Git"]

print("My current skills:", my_skills)

# Add a skill
my_skills.append("Docker")
print("After learning Docker:", my_skills)

# Print each skill with a message
print("\n--- Skill Checklist ---")
for skill in my_skills:
    print(f"✅ I know {skill}")