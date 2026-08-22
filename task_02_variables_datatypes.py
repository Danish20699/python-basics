#task 2


#Declearing different data types 
#=====================================

# Integer
cpu_cors = 8
#print("CPu Cores:", cpu_cors)

#string
user_name  = "Danish"
#print("User Name:", user_name)

#Float
cpu_speed = 3.5
#print("CPU Speed:", cpu_speed)

#Boolean
maintenance_mode = False
#print("Maintenance Mode:", maintenance_mode)

# 2. Printing the data types of the variables and variables values
print(f"Data Type of cpu_cors: {type(cpu_cors)}")
print(f"Data Type of user_name: {type(user_name)}")
print(f"Data Type of cpu_speed: {type(cpu_speed)}")
print(f"Data Type of maintenance_mode: {type(maintenance_mode)}")


# 4.Dynamic Typing: Assigning a new value of a different data type to an existing variable
#variable can change typrs

print("\n---3. Dynamic Typing in action---")
status = 200  # Initially an integer
print(f"status is: {status}, Data Type of status: {type(status)}")

status = "OK or active"  # Now a string #reassigning a new value of a different data type to an existing variable
print(f"status is: {status}, Data Type of status: {type(status)}")


# 5. Multiple Assignment in a single line
host, port = "127.0.0.1", 8080
print(f"\nHost: {host}, Port: {port}")