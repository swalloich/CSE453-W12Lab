from enum import Enum

########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    This class stores the notion of Bell-LaPadula
########################################################################

class Control(Enum):
    """
    Control is an enumeration that defines the security levels for the Bell-LaPadula model.
    """
    UNCLASSIFIED = 0
    CONFIDENTIAL = 1
    SECRET = 2
    TOP_SECRET = 3

    def __str__(self):
        return self.name.lower()
