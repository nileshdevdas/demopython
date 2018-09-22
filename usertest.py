from dao import UserDAO;
from datamodels import User,Group;


def createUser():
    userDAO = UserDAO();
    user = User();
    user.username = "nilesh";
    user.password = "nilesh";
    group = Group();
    group.grouName = "admin";
    group.addUser(user);
    userDAO.save(user);


createUser();