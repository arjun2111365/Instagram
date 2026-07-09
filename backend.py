class UserManager:

    def __init__(self):
        self.users = {}
        self.user_id = 0

    def create_user(self, name, password, email):
        if name in self.users:
            return False

        self.user_id += 1
        self.users[name] = {
            "id": self.user_id,
            "password": password,
            "email": email,
            "following": 0,
            "posts": 0,
            "followers": 0
        }

        return True

    def login(self, name, password):
        return name in self.users and password == self.users[name]["password"]

    def delete_account(self, name):
        del self.users[name]

class Post:
    def __init__(self,name,content,post_id):
        self.name=name
        self.content=content
        self.post_id=post_id
        
        
class PostManager:
    
    def __init__(self):
        self.posts={}
        self.post_id=0
    
    def create_post(self,name,content):
        self.post_id+=1
        post_obj=Post(name,content,self.post_id)
        self.posts[self.post_id]=post_obj
        


class InstagramApp:
    def __init__(self):
        self.users = UserManager()
        self.posts=PostManager()


if __name__ == "__main__":
    current_user=None
    app = InstagramApp()

    def account_existance(name, password):
        return app.users.login(name, password)

    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Delete Account")
        print("4. Create Post")
        print("5. loggout")
        print("6. Exit")
        

        choice = input("Choice: ")

        if choice == "1":
            if  current_user is not None:
                print("please loggout first!")
                continue 


            name = input("Enter your name: ")
            password = input("Enter your password: ")
            email = input("Enter your email: ")

            check = app.users.create_user(name, password, email)

            if check:
                print("Successfully account created!")
            else:
                x = input("Account already exists. Would you like to login? (y/n): ")

                if x == "y":
                    if account_existance(name, password):
                        current_user=name
                        print("Login successful")
                    else:
                        print("Wrong password!")

        elif choice == "2":
            name = input("Enter your name: ")
            password = input("Enter your password: ")

            if account_existance(name, password):
                current_user=name
                print("Login successful")
            else:
                print("Wrong password!")

        elif choice == "3":
            name = input("Enter your name: ")
            password = input("Enter your password: ")

            if account_existance(name, password):
                app.users.delete_account(name)
                print("Account deleted")
            else:
                print("Wrong username or password!")

        elif choice == "4":
            if current_user is None:
                print("please Loggin first!")
                continue
            content=input("enter your post: ")
            app.posts.create_post(current_user,content)
            app.users.users[current_user]["posts"] += 1
            print("Post created successfully!")
            
        elif choice=="5":
            current_user=None

        elif choice=="6":
            break