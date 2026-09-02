def validate_password(password):
    #mininum length of 9 characters
    if len(password) < 9:
        return "Passwod ust be at least 9 characters long"

    #At least one number
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number"

    #At least one uppercase letter
    if not any (char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"

    #At least one symbol from @#$%^&+=!~
    if not any (char in "@#$%^&+=!~" for char in password):
        return "Password must contain at least 1 symbol from @#$%^&+=!~"

    return "Password is valid"

password = input("Enter a password to validate: ")
print(validate_password(password))
