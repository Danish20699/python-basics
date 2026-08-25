#A tuple is an ordered collection created with parentheses()
#THE READ-ONLY-LIST

#WHY USE TUPLES INSTEAD OF LIST?

#......immutable:Once Created, you cannot add,remove or modify items
#Data Protection:Use tuples for constanats (eg databse connection configs, databse connection configs, geo-coordinates, IP/Port pairs) so other parts of your code cannot accidently alter them
#3. Fast & Memory Efficient:Tuples are faster and use less RAm than lists

#1. Creating a Tuple
db_config = ("localhost", 54321, "postgres_admin")

#2. Accessing items by index (same as lists)
print("Host:", db_config[0])  #localhost
print("Port:", db_config[1])  #54321

#3.Tuple Unpacking(very common in python)
host, port, user = db_config
print(f"Connecting to {host}:{port} as {user}")

#Tuples are Immutable! This line will cause are typeError:
#db_config[1] = 3306

#Single-item tuple requires a trailing comma:

single_item =("production",)  #Tuple
not_a_tuple = ("production")  #Just a reguler string!

#2 Sets(set)----Unique & fast Deduplication
#A Set is an Ordered collection created with curly braces{}
#set()).

#Why use Sets?
#.No Duplicate Aloowd:Any duplicate values are automatically discard
#.Lightning fast Lookups:Checking
#if item in my_list is almost instantaneous(0(1)time)
#3.Set Math:Perfect for comparing lists(union,Intersection,Difference)

#1 Automate Deduplication

raw_ips = ["192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1", "10.0.0.5"]
unique_ips = set(raw_ips)
print("Unique IPs:", unique_ips)
# Output: {'192.168.1.1', '10.0.0.5', '172.16.0.1'}

# 2. Adding & Removing elements
firewall_whitelist = {"192.168.1.10", "192.168.1.20"}
firewall_whitelist.add("192.168.1.30")       # Add item
firewall_whitelist.discard("192.168.1.10")   # Safe remove (won't crash if missing)

#⚡ Set Math (Venn Diagram Operations)
team_devops = {"Danish", "Mudasir", "Moin"}
team_security = {"Faizan_Sir", "smd", "musharaff"}

#1 Union (|) -> Everyone combined
all_engineers = team_devops | team_security
print("Union (All Engineers):",all_engineers)

#2. Intersection (&) ----> Present in both sets
cross_functional = team_devops & team_security
print("Intersection(Both teams):", cross_functional)

#3.Difference (-) -> In team_devops but  NOT in team_security
devops_only = team_devops - team_security
print("difference (Devops only:)", devops_only)