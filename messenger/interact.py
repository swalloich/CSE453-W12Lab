########################################################################
# COMPONENT:
#    INTERACT
# Author:
#    Br. Helfrich, Kyle Mueller, Jacob Nelson <your name here if you made a change>
# Summary:
#    This class allows one user to interact with the system
########################################################################

from control import Control
from os import path

###############################################################
# USER
# User has a name and a password
###############################################################
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.security_level = Control(self._get_security_level())

    # Security level stored in a file since it needs to be able
    # to change without changing the code
    def _get_security_level(self):
        try:
            FILE_NAME = path.join(path.dirname(path.abspath(__file__)), "security_level_map.txt")
            with open(FILE_NAME, "r") as f:
                for line in f:
                    if line.startswith(self.name):
                        return line.split('|')[1].rstrip('\n')
        except FileNotFoundError:
            print("Security level map file not found.")
            return

# I fail to see how this fits the description of step 5 on the assignment page.
userlist = [
   [ "AdmiralAbe",     "password"],
   [ "CaptainCharlie", "password"],
   [ "SeamanSam",      "password"],
   [ "SeamanSue",      "password"],
   [ "SeamanSly",      "password"]
]

###############################################################
# USERS
# All the users currently in the system
###############################################################
users = [*map(lambda u: User(*u), userlist)]

ID_INVALID = -1

######################################################
# INTERACT
# One user interacting with the system
######################################################
class Interact:

    ##################################################
    # INTERACT CONSTRUCTOR
    # Authenticate the user and get him/her all set up
    ##################################################
    def __init__(self, username: str, password: str, messages: str):
        self._authenticate(username, password)
        self._username = username
        USER_CONTROL = self._security_level_from_user(username)
        self._security_level = Control(USER_CONTROL)
        self._p_messages = messages

    ##################################################
    # INTERACT :: SHOW
    # Show a single message
    ##################################################
    def show(self):
        id_ = self._prompt_for_id("display")
        if not self._p_messages.show(id_, self._security_level):
            print(f"ERROR! Message ID \'{id_}\' does not exist")
        print()

    ##################################################
    # INTERACT :: DISPLAY
    # Display the set of messages
    ################################################## 
    def display(self):
        print("Messages:")
        self._p_messages.display(self._security_level)
        print()

    ##################################################
    # INTERACT :: ADD
    # Add a single message
    ################################################## 
    def add(self):
        self._p_messages.add(self._prompt_for_line("message"),
                             self._username,
                             self._prompt_for_line("date"),
                             self._prompt_for_line("security level"))

    ##################################################
    # INTERACT :: UPDATE
    # Update a single message
    ################################################## 
    def update(self):
        id_ = self._prompt_for_id("update")
        if not self._p_messages.show(id_, self._security_level):
            print(f"ERROR! Message ID \'{id_}\' does not exist\n")
            return
        self._p_messages.update(id_, self._prompt_for_line("message"), self._security_level)
        print()
            
    ##################################################
    # INTERACT :: REMOVE
    # Remove one message from the list
    ################################################## 
    def remove(self):
        self._p_messages.remove(self._prompt_for_id("delete"), self._security_level)

    ##################################################
    # INTERACT :: PROMPT FOR LINE
    # Prompt for a line of input
    ################################################## 
    def _prompt_for_line(self, verb):
        return input(f"Please provide a {verb}: ")

    ##################################################
    # INTERACT :: PROMPT FOR ID
    # Prompt for a message ID
    ##################################################
    def _prompt_for_id(self, verb):
        return int(input(f"Select the message ID to {verb}: "))

    ##################################################
    # INTERACT :: AUTHENTICATE
    # Authenticate the user: find their control level
    ##################################################
    def _authenticate(self, username, password):
        id_ = self._id_from_user(username)
        return ID_INVALID != id_ and password == users[id_].password

    ##################################################
    # INTERACT :: ID FROM USER
    # Find the ID of a given user
    ##################################################
    def _id_from_user(self, username):
        for id_user in range(len(users)):
            if username == users[id_user].name:
                return id_user
        return ID_INVALID
    
    ##################################################
    # INTERACT :: SECURITY LEVEL FROM USER
    # Find the security level of a given user
    ##################################################
    def _security_level_from_user(self, username):
        id_ = self._id_from_user(username)
        if ID_INVALID == id_:
            raise ValueError(f"Invalid user: {username}")
        return users[id_].security_level.name

#####################################################
# INTERACT :: DISPLAY USERS
# Display the set of users in the system
#####################################################
def display_users():
    for user in users:
        print(f"\t{user.name}")
