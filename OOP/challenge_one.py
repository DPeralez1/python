class App():
    def __init__(self,users,storage,username):
        self.users = users
        self.storage = storage
        self.username = username

    def login(self):
        if self.username == "owner" and self.users >= 1:
            print(f"Hi {self.username}")
            print(f"Your storage is: {self.storage}")
        else:
            print("You are not the owner")

    def increase_capacity(self,number):
        self.storage += number
        print(f"Update storage: {self.storage}")

    def check_upgrade(self):
        if self.users >= self.storage:
            upgrade_amt = int(input("Upgrade amount: "))
            self.storage += upgrade_amt
        else:
            print(f"You still have: {self.storage - self.users}, spaces open")

user_one = App(35,89,"owner")
user_one.login()
user_one.increase_capacity(44)
print()
user_two = App(12,128,"David")
user_two.login
user_two.check_upgrade()
