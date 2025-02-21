"""
This module provides a function for initializing a 'Programmer' object.

The module includes the 'print_bio' function to view the instance's attributes as a formatted string.
"""

class Programmer:
    def __init__(self, first_name, last_name, language, age):
        """
        Initialize instance of Programmer class.

        :param first_name:  Programmer's first name.
        :param last_name:   Programmer's last name.
        :param language:    Programming language.
        :param age:         Programmer's age.
        :return:            Programmer class instance as object.
        """
        self.first_name = first_name.lower().capitalize()
        self.last_name = last_name.lower().capitalize()
        self.program_language  = language.lower().capitalize()
        self.age = age

    def print_bio(self):
        """
        Print instance attributes as formatted string.

        :return:            Programmer's background information within a formatted sting.
        :raises TypeError:  Object attributes have incorrect data type.
        """
        programmer_info_type = dict(first_name=str, last_name=str, program_language=str, age=int)
        if (not isinstance(self.first_name, programmer_info_type['first_name'])
                or not isinstance(self.last_name, programmer_info_type['last_name']))\
                or not isinstance(self.program_language, programmer_info_type['program_language'])\
                or not isinstance(self.age, programmer_info_type['age']):

            raise TypeError(f'One or more instance attributes has an incorrect data type.'
                            f'\n{programmer_info_type}')

        else:
            return (f'Hey there. I am {self.first_name} {self.last_name}.\n'
                    f'I am {self.age} and like to program using {self.program_language}.')
