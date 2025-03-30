########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, Jacob Nelson, <your name here if you made a change>
# Summary:
#    This class stores the notion of a collection of messages
########################################################################

from message import Message
from control import Control

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename: str):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, subjectControl: Control) -> None:
        for m in self._messages:
            try:
                if not m.empty:
                    m.display_properties(subjectControl)
            except PermissionError:
                pass

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id, subjectControl: Control) -> bool:
        for m in self._messages:
            if m.get_id() == id:
                try:
                    m.display_text(subjectControl)
                    return True
                except PermissionError as e:
                    print(f"ERROR! {e}")
                    return False
        return False

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text: str, subjectControl: Control) -> None:
        for m in self._messages:
            if m.get_id() == id:
                try:
                    m.update_text(text, subjectControl)
                except PermissionError as e:
                    print(f"ERROR! {e}")
                    return

    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id, subjectControl: Control) -> None:
        for m in self._messages:
            if m.get_id() == id:
                try:
                    m.clear(subjectControl)
                except PermissionError as e:
                    print(f"ERROR! {e}")
                    return

    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ##################################################
    def add(self, text: str, author: str, date: str, assetControl: Control) -> None:
        m = Message(text, author, date, assetControl)
        self._messages.append(m)

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename: str) -> None:
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    self.add(text.rstrip('\r\n'), author, date, Control(text_control.upper()))
        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
