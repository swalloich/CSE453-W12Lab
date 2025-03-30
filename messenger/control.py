########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, Jacob Nelson <your name here if you made a change>
# Summary:
#    This class stores the notion of Bell-LaPadula
########################################################################
from os import path

########################################################################
# I know the reading says to use an enum, but it also describes the
# ability to add and remove levels. Since this is not possible with an
# enum, I am going to use a class with a dictionary to store the levels.
########################################################################
class Control:

    CONTROL_LEVELS_FILE = path.join(path.dirname(path.abspath(__file__)), "current_security_levels.txt")

    def __init__(self):
        """
        Initialize the Control class with predefined security levels.
        """
        self._levels = self._load_levels_from_file(self.CONTROL_LEVELS_FILE)
        self._value = 0
        self._name = list(self._levels.keys())[0]

    def __init__(self, level: str):
        """
        Initialize the Control class with a specific security level.
        """
        self._levels = self._load_levels_from_file(self.CONTROL_LEVELS_FILE)
        if level in self._levels:
            self.current_level = self._levels[level]
            self._value = self._levels[level]
            self._name = level
        else:
            raise ValueError(f"Invalid security level: {level}")

    def __ge__(self, other):
        """
        Define the greater than operator for the Control enumeration.
        """
        if isinstance (other, Control):
            return self.value >= other.value
        if isinstance(other, int):
            return self.value >= other
        elif isinstance(other, str):
            return self.value >= self._levels[str(other)]
        else:
            return NotImplemented

    def __le__(self, other):
        """
        Define the less than or equal to operator for the Control enumeration.
        """
        if isinstance(other, Control):
            return self.value <= other.value
        if isinstance(other, int):
            return self.value <= other
        elif isinstance(other, str):
            return self.value <= self._levels[str(other)]
        else:
            return NotImplemented

    # Getters and Setters
    @property
    def name(self) -> str:
        """
        Get the name of the current security level.
        """
        return self._name
    
    @property
    def value(self) -> int:
        """
        Get the value of the current security level.
        """
        return self._value
    
    # Private methods
    def _load_levels_from_file(self, filename: str) -> None:
        """
        Load security levels from a file.
        """
        levels = {}
        try:
            with open(filename, 'r') as file:
                for i, line in enumerate(file):
                    level_name = line.strip()
                    levels[level_name] = i
            return levels
        except FileNotFoundError:
            print(f"File {filename} not found. Using default levels.")
