"""
This module provides class functions for initializing and using the KeyValueTable class.

The module includes functions for managing database tables (existing as JSON files)
and records (existing as key value pairs).
"""

import os.path
import json_database.database.key_value_database as kvs
import json_database.tools.tools as tools
import pickle

class KeyValueTable(kvs.KeyValueDatabase):
    def __init__(self, database_name, table_name ):
        super().__init__(database_name)
        """
        Initialize KeyValueTable instance.
        
        :param database_name:   Database name.
        :param table_name:      Key value store or table name (json file name).
        :returns:               Initialized 'KeyValueTable' object.
        """
        self.table_file = table_name
        self.table_file_path = None
        self.table_file_object = None
        self.working_file_modes = dict(append='a+', read='r+', write='w')


    def open_table(self, mode='append'):
        """
        Open table (JSON file handle).

        :param mode:                File handle modes - 'append','read', or 'write.'
        :returns:                   Initialized 'KeyValueDatabase' instance as JSON file.
        :raises FileExistsError:    Directory (database) already exist.
        :raises FileNotFoundError:  Parent directory does not exist.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            self.create_database()
            self.table_file_path = os.path.join(self.database_path, self.table_file + '.json')
            self.table_file_object = open(self.table_file_path, self.working_file_modes[mode])

        except FileExistsError as error:
            tools.print_error(error_message=error, debug='dne')
        except FileNotFoundError as error:
            tools.print_error(error_message=error, debug='create_record')
        except PermissionError as error:
            tools.print_error(error_message=error, debug='access')
        except KeyError as error:
            tools.print_error(error_message=error, debug='file_handle')
        except Exception and OSError as error:
            tools.print_error(error_message=error, debug='unknown')

    def close_table(self):
        """
        Close table (JSON file handle).

        :return:                    File handle (table) successfully closed.
        :raises AttributeError:     Database table (json file) closed.
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            self.table_file_object.close()
            self.table_file_object = None

        except AttributeError as error:
            tools.print_error(error_message=error, debug='open_table')
        except FileNotFoundError as error:
            tools.print_error(error_message=error, debug='dne')
        except Exception and OSError as error:
            tools.print_error(error_message=error, debug='unknown')

    def set_pair(self, record_key, record_value, value_is_instance=False):
        """
        Write record (key value pair) to database table (JSON file).

        :param record_key:          Key of key value pair.
        :param record_value:        Value of key value pair.
        :param value_is_instance:   True if pair value is class instance. Else false.
        :return:                    Key value pair saved to database table (json file).
        :raises AttributeError:     Database table (json file) closed.
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            self.open_table()

            if value_is_instance:
                record_value = repr(pickle.dumps(record_value)).replace('\\', '\\\\')
            data = f'\t"{record_key}": "{record_value}"'

            if self.table_file_object.tell() == 0:
                self.table_file_object.write('{\n' + data)
            else:
                self.table_file_object.close()

                self.open_table(mode='read')
                clean_text = lambda text: text.strip().replace('"', '').replace(',', '')
                select_key = lambda text: clean_text(text.split(':')[0])
                reformat_line = lambda line: line.replace('"\n','",\n')

                document_lines = self.table_file_object.readlines()[:-1]
                document_lines_new = [reformat_line(line) for line in document_lines
                                      if line != ',\n'
                                      and select_key(line) != str(record_key)]
                self.table_file_object.close()

                self.open_table(mode='write')
                self.table_file_object.writelines(document_lines_new)
                self.table_file_object.close()

                self.open_table()
                self.table_file_object.write(data)
            self.table_file_object.write('\n}')
            self.close_table()

        except AttributeError as error:
            tools.print_error(error_message=error, debug='open_table')
        except FileNotFoundError as error:
            tools.print_error(error_message=error, debug='dne')
        except PermissionError as error:
            tools.print_error(error_message=error, debug='access')
        except Exception and OSError as error:
            tools.print_error(error_message=error, debug='unknown')

    def get_value(self, record_key, value_is_instance=False):
        """
        Retrieve corresponding record's value for provided record key.

        :param record_key:          Key of key value pair.
        :param value_is_instance:   True if expected value is an instance. Else false.
        :return:                    Key value pair value or instance.
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises KeyError:           Key not found in database table (json file).
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            database = self.table_to_dictionary()
            record_key = tools.convert_to_string(record_key)
            value = database[record_key]
            if value_is_instance:
                value = tools.string_to_bytes(value)
                return pickle.loads(value)
            else:
                return value

        except KeyError as error:
            tools.print_error(error_message=error, debug='key')
        except TypeError as error:
            tools.print_error(error_message=error, debug='type_bytes')
        except FileNotFoundError as error:
            tools.print_error(error_message=error, debug='create_record')
        except OSError as error:
            tools.print_error(error_message=error, debug='unknown')
        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')

    def get_key(self, record_value):
        """
        Retrieve corresponding record key(s) for provided record value.

        :param record_value:        Value of key value pair.
        :return:                    Return list of corresponding key(s) for provided 'pair_value'.
                                    'None' returned when value does not exist.
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises AttributeError:     Database table (json file) closed.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            database_table = self.table_to_dictionary()
            record_value = tools.convert_to_string(data=record_value)
            if record_value in database_table.values():
                possible_keys = [item for item in database_table.items() if item[1] == record_value]
                return possible_keys
            else:
                return None

        except FileNotFoundError and AttributeError as error:
            tools.print_error(error_message=error, debug='create_record')
        except OSError as error:
            tools.print_error(error_message=error, debug='unknown')
        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')

    def delete_pair(self, record_key):
        """
        Delete record (key value pair) from database table (JSON file).

        :param record_key:          Key of key value pair.
        :return:                    Delete key value pair from database table (json file).
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises AttributeError:     Database table (json file) closed.
        :raises KeyError:           Key not found in database table (json file).
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            database_dictionary = self.table_to_dictionary()

            record_key = tools.convert_to_string(record_key)
            database_dictionary.pop(record_key)
            self.open_table(mode='write')
            self.close_table()

            for key, value in database_dictionary.items():
                self.set_pair(record_key= key, record_value= value)

        except KeyError as error:
            tools.print_error(error_message=error, debug='key')
        except FileNotFoundError as error:
            tools.print_error(error_message=error, debug='create_record')
        except AttributeError as error:
            tools.print_error(error_message=error, debug='open_table')
        except Exception and OSError as error:
            tools.print_error(error_message=error, debug='unknown')

    def check_key(self, record_key):
        """
        Search database table (JSON file) for provided record key.

        :param record_key:          key of key value pair.
        :return:                    True if key found in database table (json file). Else false.
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises AttributeError:     Database table (json file) closed.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            database_table = self.table_to_dictionary()
            record_key = tools.convert_to_string(data=record_key)
            if record_key in database_table.keys():
                return True
            else:
                return False

        except FileNotFoundError and AttributeError as error:
            tools.print_error(error_message=error, debug='create_record')
        except OSError as error:
            tools.print_error(error_message=error, debug='unknown')
        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')

    def count_records(self):
        """
        Count database table (JSON file) records (key value pairs).

        :return:                    Number of database table records (key value pairs).
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises AttributeError:     Database table (json file) closed.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            key_value_pair_count = len(self.table_to_dictionary())
            return key_value_pair_count

        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')

    def get_all_keys(self):
        """
        List all database table (JSON file) record (key value pairs) keys.

        :return:                    Database table (json file) keys as list.
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises AttributeError:     Database table (json file) closed.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            database_table = self.table_to_dictionary()
            return database_table.keys()

        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')


    def copy_table(self, table_file_name, table_file_path='.\\'):
        """
        Clone database table (JSON file).

        :param table_file_name:     File name without extension.
        :param table_file_path:     Full directory address.
        :return:                    Replicated document saved to provided path.
        :raises AttributeError:     Database table (json file) closed.
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected occurs.
        """
        try:
            self.open_table(mode='read')

            if not os.path.exists(table_file_path):
                os.mkdir(table_file_path)

            destination = os.path.join(table_file_path, table_file_name + '.json')
            with open(destination, 'w') as outfile:
                for line in self.table_file_object.readlines():
                    outfile.write(line)

            self.close_table()

        except FileNotFoundError and AttributeError as error:
            tools.print_error(error_message=error, debug='dne')
        except Exception and OSError as error:
            tools.print_error(error_message=error, debug='unknown')
        except PermissionError as error:
            tools.print_error(error_message=error, debug='access')

    def rename_table(self, old_table_name, new_table_name):
        """
        Rename database table (JSON file).

        :param old_table_name:      Database table name.
        :param new_table_name:      New database table name.
        :return:                    Renamed database table.
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises PermissionError:    Insufficient file system permissions.
        :raises FileExistError:     Database table (json file) already exists.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error
        """
        try:
            source = os.path.join(tools.trim_folder_location(self.table_file_path), old_table_name + '.json')
            destination = os.path.join(tools.trim_folder_location(self.table_file_path), new_table_name + '.json')
            os.rename(src=source, dst=destination)

        except FileNotFoundError as error:
            tools.print_error(error_message=error, debug='dne')
        except PermissionError as error:
            tools.print_error(error_message=error, debug='access')
        except FileExistsError as error:
            tools.print_error(error_message=error, debug='exist')
        except Exception and OSError as error:
            tools.print_error(error_message=error, debug='unknown')

    def delete_table(self, table_name):
        """
        Delete database table (JSON file).

        :param table_name:          Database table (json file) name.
        :return:                    Delete database table (json file) from database (directory).
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error
        """
        try:
            database_folder_path = tools.trim_folder_location(self.table_file_path)
            table_file_path = os.path.join(database_folder_path, table_name + '.json')
            if os.path.exists(table_file_path):
                os.remove(table_file_path)
            else:
                raise FileNotFoundError

        except FileNotFoundError as error:
            tools.print_error(error_message=error, debug='dne')
        except PermissionError as error:
            tools.print_error(error_message=error, debug='access')
        except Exception and OSError as error:
            tools.print_error(error_message=error, debug='unknown')

    def table_to_dictionary(self):
        """
        Read database table (JSON file) and duplicate records to dictionary object.

        :return:                    Dictionary database table (json file) records (key value pairs).
        :raises FileNotFoundError:  Database table (json file) not found.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            self.open_table(mode='read')
            clean_line = lambda text: text.strip().replace('"', '').replace(',', '')
            split_key = lambda text: clean_line(text.split(':')[0])
            split_value = lambda text: clean_line(text.split(':')[1])

            records_dictionary = {}
            for line in self.table_file_object.readlines()[1:-1]:
                records_dictionary.update({split_key(line): split_value(line)})
            self.close_table()

            return records_dictionary

        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')