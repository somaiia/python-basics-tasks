password = "python1234"
attempts = 3

while attempts > 0:
    current_password = input("enter your password! ")
    if current_password == password:
        print("access granted")
        break
    else:
        attempts -= 1
        print(f"incorrect password, you have {attempts} attempts left")

if attempts == 0:
    print("access denied, you have used all attempts!")
