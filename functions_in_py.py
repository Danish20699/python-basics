#1. Simplest Function (No Parameters, No Return)

def say_hello():
    print("Hello, Welcome to python")

#Calling the function
say_hello()
say_hello()

#2. Function With Parameters

def greet(name):
    print(f"Hi {name}, good to see you!")

greet("Danish")
greet("Alice")

#3. Function With return (Sends a Value Back)
def add(a, b):
    result = a  + b
    return result

#Store returned value in a variable

total = add(10, 20)
print("Total:", total)

#Use directly in print
print ("sum:", add(5, 3))



#Function With return (Sends a Value Back)
def add(a, b):
    result = a + b
    return result

# Store returned value in a variable
total = add(10, 20)
print("Total:", total)   # Total: 30

# Use directly in print
print("Sum:", add(5, 3))  # Sum: 8


#💡 print() vs return:
# print() -> just displays on screen, returns nothing
def add_print(a, b):
    print(a + b)

# return -> sends value back, you can save it
def add_return(a, b):
    return a + b

x = add_print(2, 3)    # Prints: 5
print("x is:", x)       # x is: None  (print returns nothing!)

y = add_return(2, 3)    # Prints nothing
print("y is:", y)       # y is: 5  (return saved the value!)



#4. Default Parameters
#If no argument is passed, the default value is used
def connect(host, port=3306):
    print(f"Connecting to {host} on port {port}...")

connect("localhost")         # Uses default port 3306
connect("db-server", 5432)   # Overrides with 5432

# Output:
# Connecting to localhost on port 3306...
# Connecting to db-server on port 5432...

#5. Multiple Parameters & Keyword Arguments

def create_user(name, role, active=True):
    print(f"Name: {name} | Role: {role} | Active: {active}")

# Positional arguments (order matters)
create_user("Danish", "DevOps")

# Keyword arguments (order doesn't matter)
create_user(role="Admin", name="Alice", active=False)

# Output:
# Name: Danish | Role: DevOps | Active: True
# Name: Alice | Role: Admin | Active: False

#6. Returning Multiple Values
def get_min_max(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

data = [45, 12, 89, 3, 67]

low, high = get_min_max(data)
print(f"Min: {low}, Max: {high}")
# Output: Min: 3, Max: 89

#7. Function Calling Another Function

def square(n):
    return n * n
def sum_of_squares(a, b):
    return square(a) + square(b)

result = sum_of_squares(3, 4)
print("Sum of Squares:", result)


#8. *args (Accept Any Number of Arguments)

def total(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total(10, 20))           # 30
print(total(1, 2, 3, 4, 5))   # 15


#9. **kwargs (Accept Any Number of Named Arguments)
def show_info(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")

print("Server Info:")
show_info(name="web-01", ip="10.0.0.1", status="active")

# Output:
# Server Info:
#   name: web-01
#   ip: 10.0.0.1
#   status: active

#10. Function With a List (Pass & Modify)
def add_server(server_list, new_server):
    server_list.append(new_server)
    print(f"Added '{new_server}'. Total servers: {len(server_list)}")

my_servers = ["web-01", "db-01"]

add_server(my_servers, "cache-01")
add_server(my_servers, "api-01")

print("Final list:", my_servers)

# Output:
# Added 'cache-01'. Total servers: 3
# Added 'api-01'. Total servers: 4
# Final list: ['web-01', 'db-01', 'cache-01', 'api-01']