while True:
    print("Select a new password (letters and numbers only):")
    password = input()

    if password.isalnum():
        print("Password valid")
        break
    else:
        print("Password can only be alpha numeric characters")
