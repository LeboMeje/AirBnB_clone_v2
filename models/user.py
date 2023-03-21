<<<<<<< HEAD
 the User class."""
=======
#!/usr/bin/python3
"""Defines the User class."""
>>>>>>> babff1351fbadb6c54591f8420e121f2e3fa9b6b
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.
<<<<<<< HEAD
=======

>>>>>>> babff1351fbadb6c54591f8420e121f2e3fa9b6b
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
