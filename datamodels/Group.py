class User:
    """
        Class documentation
    """
    def __init__(self):
        """
            my constructor
        """
        self.username = None;
        self.password = None;

    def test(self):
        """about the method"""
        pass;

    def __del__(self):
        pass;

    def __repr__(self):
        if self.username is not None and self.password is not None:
            return self.username + "," + self.password;
        else:
            return "Empty User";

