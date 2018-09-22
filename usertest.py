from helpers import PropertyHelper;
import base64;
import mysql.connector;

config = PropertyHelper();
print(base64.b64encode(b'root'));

username = base64.b64decode(config.props['username'])
password = base64.b64decode(config.props['password']);
host = config.props['host'];
port = config.props['port']
dbname = config.props['dbname']
conn = mysql.connector.connect(user=username, password=password , host=host, port=port, database=dbname);
print(conn.is_connected());