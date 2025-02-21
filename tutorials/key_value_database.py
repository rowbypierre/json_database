import os
from json_database.miscellaneous.programmer import Programmer
from json_database.database.key_value_database import KeyValueDatabase
from json_database.table.key_value_table import KeyValueTable

# SAMPLE DATABASE INFORMATION.
database_name = 'sample_database'

# # INITIALIZE DATABASE OBJECTS
# # Note: Within the file system, databases exist as directories/ folders.
# #       Tables are the json files storing the key value pairs.
# # Sample database.
# database_name = 'sample_database'
# table_name = 'sample_table'
# # Database instance.
# sample_database = KeyValueDatabase(database_name=database_name)

# # SET CURRENT WORKING DIRECTORY AS DESTINATION FOR DATABASE FILES
# # Sample database.
# database_name = 'sample_database'
# table_name = 'sample_table'
# # Database and table object.
# sample_database = KeyValueDatabase(database_name=database_name)
# # Set database files destination as current working directory.
# sample_database.set_database_directory()
# # Create database directory (folder containing table as json files).
# sample_database.create_database()


# # SET ALTERNATE DESTINATION FOR DATABASE FILES
# # Note: if provided path below does not exist, the program will attempt to create the path.
# # Sample database.
# database_name = 'sample_database'
# table_name = 'sample_table'
# # Database and table object.
# sample_database = KeyValueDatabase(database_name=database_name)
# # Set database files destination as current working directory.
# sample_database.set_database_directory()
# # Path.
# database_location = os.path.join(os.getcwd(), 'new_database_directory')
# # Set alternate path.
# sample_database.set_database_directory(use_current_directory=False, new_directory_path=database_location)
# # Create database directory (folder containing table as json files).
# sample_database.create_database()

# # COPY DATABASE
# # Note: Current database directory will be saved to provided location.
# # Sample database.
# database_name = 'sample_database'
# # Database object.
# sample_database = KeyValueDatabase(database_name=database_name)
# print(vars(sample_database))
# # Set database files destination as current working directory.
# sample_database.set_database_directory()
# print(vars(sample_database))
# # Create database directory.
# sample_database.create_database()
# # Copy database.
# copy_database_path = os.path.join(os.getcwd(), 'sample_database_copy')
# sample_database.copy_database(copy_database_path=copy_database_path)

# # PRINT DATABASE TABLES
# # Sample database.
# database_name = 'sample_database'
# # Database object.
# sample_database = KeyValueDatabase(database_name=database_name)
# print(vars(sample_database))
# # Set database files destination as current working directory.
# sample_database.set_database_directory()
# print(vars(sample_database))
# # Create database directory.
# sample_database.create_database()
# # Print database tables.
# print(sample_database.get_database_tables())

# # DELETE DATABASE (database directory)
# # Sample database.
# database_name = 'sample_database'
# # Database object.
# sample_database = KeyValueDatabase(database_name=database_name)
# # Set database files destination as current working directory.
# sample_database.set_database_directory()
# # Create database directory.
# sample_database.create_database()
# Delete database.
# delete_database_path = os.path.join(os.getcwd(), 'new_database_directory')
# sample_database.delete_database(delete_database_path)

# # RENAME DATABASE (database directory)
# database_name = 'sample_database_copy'
# # Database object.
# sample_database = KeyValueDatabase(database_name=database_name)
# # Set database files destination as current working directory.
# sample_database.set_database_directory()
# # Create database directory.
# sample_database.create_database()
# # Rename database.
# sample_database.rename_database(new_database_name='sample_database_renamed')

# # RENAME DATABASE (database directory)
# database_name = 'sample_database'
# # Database object.
# sample_database = KeyValueDatabase(database_name=database_name)
# # Set database files destination as current working directory.
# sample_database.set_database_directory()
# # Create database directory.
# sample_database.create_database()
# # Rename database.
# sample_database.rename_database(new_database_name='sample_database_renamed')

# # DATABASE (database directory) METHODS
# database_name = 'sample_database'
# # Database object.
# sample_database = KeyValueDatabase(database_name=database_name)
# # Set database files destination as current working directory.
# sample_database.set_database_directory()
# # Create database objects (table as json file and miscellaneous text file).
# print(os.getcwd())
# table_location = os.path.join(os.getcwd(), database_name, 'sample_table.json')
# misc_text_location = os.path.join(table_location[:table_location.rindex('\\')],
#                                   'sample_misc_text.txt')
# new_table_file = open(table_location, 'w+')
# new_table_file.close()
# new_text_file = open(misc_text_location, 'w+')
# new_text_file.close()
# # - List database objects (tables & etc).
# print(sample_database.list_database_objects())
# # - Count database objects.
# print(len(sample_database.list_database_objects()),
#       sample_database.count_database_objects())
# # - List database tables only.
# print(sample_database.list_database_tables())
# # - Count database tables.
# print(len(sample_database.list_database_tables()),
#       sample_database.count_database_tables())

