class Group:
    # method allows me to create empty group
    def __init__(self):
        self.grouName= None;
        self.users = [];


    # allow me to add users to group
    def addUser(self, user):
        self.users.append(user);


    # remove all the users
    def removeUsers(self):
        self.users = [];


