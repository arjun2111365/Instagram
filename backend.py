class Instagram():

    def __init__(self):
        self.users = {}
        self.id = 0

    def create_user(self, name, password, email):
        if name in self.users:
            return False

        self.id += 1
        self.users.update({
            name: {
                "id": self.id,
                "password": password,
                "email": email,
                "following": 0,
                "posts": 0,
                "followers": 0
            }
        })

        return True

    def login(self, name, password):

        if name in self.users and password == self.users[name]["password"]:
            return True
        else:
            return False

    def delete_account(self, name):

        del self.users[name]


if __name__ == "__main__":

    app = Instagram()

    def account_existance(name, password):
        valid = app.login(name, password)
        return valid

    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Delete Account")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            email = input("Enter your email: ")

            check = app.create_user(name, password, email)

            if check:
                print("Successfully account created!")
            else:
                x = input("Account already exists. Would you like to login? (y/n): ")

                if x == "y":
                    check2 = account_existance(name, password)

                    if check2:
                        print("Login successful")
                    else:
                        print("Wrong password!")

        elif choice == "2":
            name = input("Enter your name: ")
            password = input("Enter your password: ")

            check = account_existance(name, password)

            if check:
                print("Login successful")
            else:
                print("Wrong password!")

        elif choice == "3":
            name = input("Enter your name: ")
            password = input("Enter your password: ")

            check = account_existance(name, password)

            if check:
                app.delete_account(name)
                print("Account deleted")
            else:
                print("Wrong username or password!")

        elif choice == "4":
            break