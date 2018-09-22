import  base64;
# helpers from this....
from helpers import PropertyHelper;
import mysql.connector;
class UserDAO:
    def __init__(self):
        self.config = PropertyHelper().props;

    ## this method is private......
    def __getConnection(self):
        conn= None;
        try:
            user = (base64.standard_b64decode(self.config['username']))
            password = (base64.standard_b64decode(self.config['password']))
            host = self.config['host'];
            port  = self.config['port'];
            dbname = self.config['dbname'];
            conn = mysql.connector.connect(user=user, password=password, host=host, port=port,
                                           database=dbname);
            print("Connection---")
            print(conn);
        except Exception as err:
            print(err);
        finally:
            pass;
        return  conn;

    def save(self, user):
        connection = None;
        try:
            connection = self.__getConnection();
            print(connection)
            # INSERT
        except Exception as err:
                pass;


    def update(self, user):
        # UPDATE
        pass;



    def delete(self, user):
        # DELETE
        pass;

    def find(self, user):
        # FIND
        pass;