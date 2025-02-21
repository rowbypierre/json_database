"""
This module provides functions to process data within the modules defining database and table classes.

The module includes functions checking and converting data types to string and bytes.
Functions handling errors and formatting file system address are included.
"""

def check_string(data):
    """
    Determine if data is a string.

    :param data:    Python object.
    :return:        True if object is a string. False if not a sting.
    """
    return isinstance(data, str)

def convert_to_string(data):
    """
    Convert data to string.

    :param data:    Python object.
    :return:        Python object as string.
    """
    if not check_string(data=data):
        data =  str(data)
    return data

def string_to_bytes(string):
    """
    Reformat string as bytes.

    :param string:  String.
    :return:        String as bytes.
    """
    string_as_bytes = eval(string.replace('\\\\', '\\'))
    return string_as_bytes

def print_error(error_message, debug=None):
    """
    Print formatted error and debugging details in place of default display message.

    :param error_message:   Program error message.
    :param debug:           Debug or troubleshooting key.
    :return:                Formatted print screen of original error message and troubleshooting step(s).
    """
    message = f'Error:\t\t{error_message}'

    if debug is not None:
        debug_options = {
            'create_record': '\nDebug:\t\tCreate at least one key value pair with \'set_pair\' method.',
            'key': '\nDebug:\t\tProvide key that exists.',
            'file_handle': '\nDebug:\t\tEnter \'append\',\'read\', or \'write\' for optional '
                           '\'mode\' parameter.',
            'open_table': '\nDebug:\t\tOpen table using \'open_table\' method after '
                            'creating database object.',
            'exist': '\nDebug:\t\tEnsure directory or file does not exist. Provide alternate name or location.',
            'dne': '\nDebug:\t\tEnsure directory or file exists. Provide alternate name or location.',
            'unknown': 'Unexpected error occurred.',
            'access': 'Configure file system properties.',
            'empty': 'Move remaining files within the provided path',
            'type_bytes': 'value_is_instance is True - bytes type object not retrieved from database table '
                          '(json file).'
        }
        print(message + debug_options[debug])

    else:
        print(message)

def trim_folder_location(full_file_path):
    """
    Trim file system address for parent directory.

    :param full_file_path:  Complete file path.
    :return:                Full path of file including filename and extension.
    """
    return full_file_path[:full_file_path.rindex('\\')]