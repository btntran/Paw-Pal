class UserProfile:
    def __init__(self, googleSignin, username, password, phoneNum):
        self.username = username
        self.googleSignin = googleSignin
        self.password = password
        self.phoneNum = phoneNum

    def update_profile(self, username=None, googleSignin=None, password=None, phoneNum=None):
        if username:
            self.username = username
        if username:
            self.googleSignin = googleSignin
        if password:
            self.password = password
        if password:
            self.phoneNum = phoneNum
    def display(self):
        print(f"username: {self.username}")
        print(f"googleSignin: {self.googleSignin}")
        print(f"password: {self.password}")
        print(f"phoneNum: {self.phoneNum}")
  
# Creating a user profile
user1 = UserProfile("johndoe@gmail.com","John Doe",12345, 53018278376)

# Display the initial profile
user1.display()

# Update some details of the profile
user1.update_profile(username="Johnathan Doe", password=12345)

# Display the updated profile
user1.display() # type: ignore
