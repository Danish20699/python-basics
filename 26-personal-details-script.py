#Personal Details Script

print("=" * 55)
print("[+] Personal Details ")
print("=" * 55)

name = input("Enter your full name: ")
age = int(input("Enter your age: "))
email = input ("Enter your email adress: ")
phone = input("Enter your phone number: ")
city = input ("Enter your city: ")
country = input("Enter your city: ")
occupation = input("Enter you occupation: ")

#2 Derived
birth_year = 1999 - age
is_adult = age >= 18

#Display
print("\n" + "=" * 55)
print("[ Personal Details -Summary Card]")
print("\n" * 55)

print(f"{'FIELD':<20} | {'DETAILS':<30}")
print("-" * 50)
print(f"{'Name:':<20} |{name:<30}")
print(f"{'FIELD':<20} | {'DETAILS':<30}")
print("-" * 55)
print(f"{'Name':<20} | {name:<30}")
print(f"{'Age':<20} | {age:<30}")
print(f"{'Birth Year (est.)':<20} | {birth_year:<30}")
print(f"{'Adult':<20} | {'Yes' if is_adult else 'No':<30}")
print(f"{'Email':<20} | {email:<30}")
print(f"{'Phone':<20} | {phone:<30}")
print(f"{'City':<20} | {city:<30}")
print(f"{'Country':<20} | {country:<30}")
print(f"{'Occupation':<20} | {occupation:<30}")
print("-" * 55)

# 4. Quick Stats
print("\n--- Quick Stats ---")
print(f"Name Length        : {len(name)} characters")
print(f"Email Provider     : {email.split('@')[-1] if '@' in email else 'Invalid email'}")
print(f"Location           : {city}, {country}")
print(f"Status             : {'Adult ✅' if is_adult else 'Minor 🔒'}")
print("\n" + "=" * 55)
print("[✔] Personal details recorded successfully!")
print("=" * 55)