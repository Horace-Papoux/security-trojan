from src.db.db_utils import get_db_connection, clean_db

class Account:
    def __init__(self, id=None, username=None, password=None, email=None, url=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.url = url 

    def to_json(self):
        """ Return a json representation of the account """
        return {
            "username": self.username,
            "id": self.id,
            "password": self.password,
            "email": self.email,
            "url": self.url
        }
        
    @staticmethod
    def from_json(json):
        """ Return an account from a json """
        return Account(
            json.get("id", None), # Default value (None)
            json.get("username", None),
            json.get("password", None),
            json.get("email", None),
            json.get("url", None)
        )
        
    @staticmethod
    def as_class(row):
        """ Return an account from the db """
        return Account(
            row["id"],
            row["username"],
            row["password"],
            row["email"],
            row["url"]
        )
        
    @staticmethod
    def all():
        """ Fetch all the accounts from the db """
        connection = get_db_connection()
        
        accounts = connection.execute('SELECT * FROM accounts').fetchall()
        
        # Close the connection
        connection.close()
        
        # Return the todos
        return [Account.as_class(account) for account in accounts]
    
    def save(self):
        """ Save the account to the db """
        connection = get_db_connection()
        
        cursor = connection.cursor()
        
        cursor.execute('INSERT INTO accounts (username, password, email, url) VALUES (?, ?, ?, ?)', (self.username, self.password, self.email, self.url))
        
        self.id = cursor.lastrowid
        
        connection.commit()
        
        connection.close()
        
        return self
    
    @staticmethod
    def clean_db():
        """ Clean the db """
        clean_db()