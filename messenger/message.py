########################################################################
# COMPONENT:
#    MESSAGE
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    This class stores the notion of a message
########################################################################

from control import Control

##################################################
# MESSAGE
# One message to be displayed to the user or not
##################################################
class Message:

    # Static variable for the next id
    _id_next = 100

    ##################################################
    # MESSAGE DEFAULT CONSTRUCTOR
    # Set a message to empty
    ##################################################
    def __init__(self):
        self._empty = True
        self._text = "Empty"
        self._author = ""
        self._date = ""
        self._id = Message._id_next
        Message._id_next += 1
        self._control = Control()

    ##################################################
    # MESSAGE NON-DEFAULT CONSTRUCTOR
    # Create a message and fill it
    ##################################################
    def __init__(self, text, author, date, control: Control):
        self._control = control
        self._text = text
        self._author = author
        self._date = date
        self._id = Message._id_next
        Message._id_next += 1
        self._empty = False

    @property
    def empty(self):
        return self._empty

    ##################################################
    # MESSAGE :: GET ID
    # Determine the unique ID of this message
    ##################################################
    def get_id(self):
        return self._id

    ##################################################
    # MESSAGE :: DISPLAY PROPERTIES
    # Display the attributes/properties but not the
    # content of this message
    ##################################################
    def display_properties(self, subjectControl: Control) -> None:
        if not self._security_condition_read(self._control, subjectControl):
            raise PermissionError("You do not have permission to view this information.")
        if self._empty:
            return
        print(f"\t[{self._id}] Message from {self._author} at {self._date}")

    ##################################################
    # MESSAGE :: DISPLAY TEXT
    # Display the contents or the text of the message
    ##################################################
    def display_text(self, subjectControl: Control) -> None:
        if not self._security_condition_read(self._control, subjectControl):
            raise PermissionError("You do not have permission to view this message.")
        print(f"\tMessage: {self._text}")

    ##################################################
    # MESSAGE :: UPDATE TEXT
    # Update the contents or text of the message
    ##################################################
    def update_text(self, new_text: str, subjectControl: Control) -> None:
        if not self._security_condition_write(self._control, subjectControl):
            raise PermissionError("You do not have permission to write to this message.")
        self._text = new_text

    ##################################################
    # MESSAGE :: CLEAR
    # Delete the contents of a message and mark it as empty
    ##################################################
    def clear(self, subjectControl: Control) -> None:
        if not self._security_condition_write(self._control, subjectControl):
            raise PermissionError("You do not have permission to delete this message.")
        self._control = Control
        self._text = "Empty"
        self._author = ""
        self._date = ""
        self._empty = True

    def _security_condition_read(self, assetControl: Control, subjectControl: Control) -> bool:
        """
        Check if the subject can read the asset based on the Bell-LaPadula model.
        """
        return subjectControl >= assetControl

    def _security_condition_write(self, assetControl: Control, subjectControl: Control) -> bool:
        """
        Check if the subject can write to the asset based on the Bell-LaPadula model.
        """
        return subjectControl <= assetControl
