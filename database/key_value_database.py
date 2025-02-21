"""
This module provides class functions for initializing and using the KeyValueDatabase class.

The module includes functions for managing database(s) at the file system level.
"""

import json_database.tools.tools as tools
import os
from shutil import copytree

class KeyValueDatabase:
    def __init__(self, database_name):
        """
        Initialize KeyValueDatabase instance.

        :param database_name:   Database name.
        :returns:               Initialized 'KeyValueDatabase' object.
        :raises KeyError:       Required positional argument 'database_name' is missing.
        """
        self.database_parent_directory = None
        self.database_name = database_name
        self.database_path = None



    def set_database_directory(self, use_current_directory=True, new_directory_path=None):
        """
        Assign database working directory.

        :param use_current_directory:   Default true. Use current working directory as database directory location.
        :param new_directory_path:      When 'use_current_directory' is False, provide desired path.
        :return:                        Update object attributes 'database_parent_directory' and 'database_path'.
        :raises FileNotFoundError:      Directory does not exist.
        :raises Exception:              Unexpected error.
        """
        try:
            if use_current_directory:
                self.database_parent_directory = os.getcwd()
            else:
                if os.path.exists(new_directory_path):
                    self.database_parent_directory = new_directory_path
                else:
                    raise FileExistsError()

            self.database_path = os.path.join(self.database_parent_directory, self.database_name)

        except FileExistsError as error:
            tools.print_error(error_message=error, debug='exist')
        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')

    def create_database(self):
        """
        Create database (directory/ folder) at file system.

        :return:                    Directory (database) created in file system.
        :raises FileExistsError:    Directory (database) already exist.
        :raises FileNotFoundError:  Parent directory does not exist.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            if not os.path.exists(self.database_path):
                os.mkdir(self.database_path)

        except FileExistsError('Directory already exist.') as error:
            tools.print_error(error_message=error, debug='exist')
        except FileNotFoundError('Parent directory does not exist.') as error:
            tools.print_error(error_message=error, debug='dne')
        except PermissionError('Insufficient permissions to directory (database)') as error:
            tools.print_error(error_message=error, debug='access')
        except OSError as error:
            tools.print_error(error_message=error, debug='unknown')
        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')

    def copy_database(self, copy_database_path):
        """
        Duplicate a database (directory/ folder at file system).

        :param copy_database_path:  File system location for copied database files.
        :return:                    Database directory saved to 'copy_database_path' location.
        :raises FileExistsError:    Directory (database) already exist.
        :raises FileNotFoundError:  Parent directory does not exist.
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Unexpected operating system error.
        :raises Exception:          Unexpected error.
        """
        try:
            if not os.path.exists(copy_database_path):
                database_directory = self.database_path
                copytree(src=database_directory, dst=copy_database_path)

            else:
                raise FileExistsError()

        except FileExistsError('Directory already exist.') as error:
            tools.print_error(error_message=error, debug='exist')
        except FileNotFoundError('Parent directory does not exist.') as error:
            tools.print_error(error_message=error, debug='dne')
        except PermissionError('Insufficient permissions to directory (database)') as error:
            tools.print_error(error_message=error, debug='access')
        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')

    @classmethod
    def delete_database(cls, database_location):
        """
        Delete a database (directory/ folder at file system).

        :param database_location:   Corresponding database directory path.
        :return:                    Delete database directory path (deleting database).
        :raises PermissionError:    Insufficient file system permissions.
        :raises OSError:            Directory is not empty.
        :raises Exception:          Unexpected error.
        """
        try:
            if os.path.exists(database_location):
                for table_name in os.listdir(database_location):
                    table_path = os.path.join(database_location, table_name)

                    if os.path.isfile(table_path):
                        os.remove(table_path)

                os.rmdir(path=database_location)

        except PermissionError as error:
            tools.print_error(error_message=error, debug='access')
        except OSError as error:
            tools.print_error(error_message=error, debug='empty')
        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')

    def rename_database(self, new_database_name):
        """
        Rename a database (directory/ folder at file system).

        :param new_database_name:   New database name (directory name).
        :return:                    Renamed database (directory) within current working directory.
        """
        new_database_path = os.path.join(self.database_parent_directory, new_database_name)
        self.copy_database(copy_database_path=new_database_path)
        self.delete_database(database_location=self.database_path)

    def list_database_objects(self):
        """
        Catalog of database objects (list all files within database directory/ folder).

        :return:                        List containing all database object.
        :raises FileNotFoundError:      Path does not exist.
        :raises PermissionError:        Insufficient file system permissions.
        :raises OSError:                Unexpected operating system error.
        :raises Exception:              Unexpected error.
        """
        try:
            database_objects = os.listdir(self.database_path)
            return database_objects
        except FileNotFoundError as error:
            tools.print_error(error_message=error, debug='dne')
        except PermissionError as error:
            tools.print_error(error_message=error, debug='access')
        except OSError as error:
            tools.print_error(error_message=error, debug='os')
        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')

    def count_database_objects(self):
        """
        Summation of database objects (all files within database directory/ folder).

        :return:                        Sum of database (directory) objects.
        :raises FileNotFoundError:      Path does not exist.
        :raises PermissionError:        Insufficient file system permissions.
        :raises OSError:                Unexpected operating system error.
        :raises Exception:              Unexpected error.
        """
        return len(self.list_database_objects())

    def list_database_tables(self):
        """
        Catalog of database tables (list all JSON files within database directory/ folder).

        :return:                        List containing all database table (json file) names.
        :raises FileNotFoundError:      Path does not exist.
        :raises PermissionError:        Insufficient file system permissions.
        :raises OSError:                File system error.
        :raises Exception:              Unexpected error.
        """
        try:
            database_objects = self.list_database_objects()
            database_table_files = [table_file_name for table_file_name in database_objects
                                            if table_file_name[table_file_name.rindex('.'):] == '.json']
            database_table_files_trimmed = [table_file_name[:table_file_name.rindex('.')] for table_file_name in database_table_files]

            return database_table_files_trimmed

        except FileNotFoundError as error:
            tools.print_error(error_message=error, debug='dne')
        except PermissionError as error:
            tools.print_error(error_message=error, debug='access')
        except OSError as error:
            tools.print_error(error_message=error, debug='os')
        except Exception as error:
            tools.print_error(error_message=error, debug='unknown')

    def count_database_tables(self):
        """
        Summation of database tables (all JSON files within database directory/ folder).

        :return:                        Sum of database (directory) tables (json files).
        :raises FileNotFoundError:      Path does not exist.
        :raises PermissionError:        Insufficient file system permissions.
        :raises OSError:                Unexpected operating system error.
        :raises Exception:              Unexpected error.
        """
        return len(self.list_database_tables())