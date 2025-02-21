import os
from json_database.miscellaneous.programmer import Programmer
from json_database.database.key_value_database import KeyValueDatabase
from json_database.table.key_value_table import KeyValueTable

# # SAMPLE DATABASE & TABLE INFORMATION
# # Note:     Database and table variables must remain uncommented for sample
# #           code to execute.
# database_name = 'sample_database'
# table_name = 'sample_table'
#
# # INITIALIZE TABLE OBJECT
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
#
# # CREATE RECORD (key and value) WITHIN TABLE.
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Create record (key value pair).
# new_record = {'testing': 'new record'}
# sample_table.set_pair(record_key=new_record[0], record_value=new_record[1])
#
# # CREATE RECORD WITH INSTANCE AS VALUE (key and value) WITHIN TABLE.
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Create record (key value pair)
# new_programmer = Programmer(first_name='rowby', last_name='pierre', age=27, language='Python')
# new_record = {'instance': new_programmer}
# sample_table.set_pair(record_key=new_record[0], record_value=new_record[1])
#
# # DELETE RECORD (key value pair) WITHIN TABLE (JSON file)
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Create record (key value pair)
# new_record = {'testing': 'new record'}
# sample_table.set_pair(record_key=new_record[0], record_value=new_record[1])
# # Delete record.
# sample_table.delete_pair(record_key=new_record[0])
#
# # RETRIEVE PAIR VALUE WITHIN TABLE (JSON file)
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Create record (key value pair).
# new_record = {'testing': 'new record'}
# sample_table.set_pair(record_key=new_record[0], record_value=new_record[1])
# # Get record value (value of key value pair).
# new_record_value = sample_table.get_value(record_key=new_record[0])
# print(new_record_value)
#
# # RETRIEVE PAIR VALUE WHEN OBJECT WITHIN TABLE
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Create record (key value pair).
# new_programmer = Programmer(first_name='rowby', last_name='pierre', age=27, language='Python')
# new_programmer.print_bio()
# new_record = {'instance': new_programmer}
# sample_table.set_pair(record_key=new_record[0], record_value=new_record[1])
# # Get record value (value of key value pair).
# programmer_record = sample_table.get_value(record_key=new_record[0])
# programmer_record.print_bio()
#
# # RETRIEVE ALL TABLE (JSON file) KEYS
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Table keys.
# table_keys = sample_table.get_all_keys()
# print(table_keys)
#
# # RETRIEVE TABLE (JSON file) KEYS WITH SPECIFIC VALUE WITHIN TABLE
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Table keys with specific value.
# search_value = 'value'
# table_keys = sample_table.get_key(record_value=search_value)
# print(table_keys)
#
# # CHECK IF KEY EXIST WITHIN TABLE (JSON file)
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Table keys with specific value.
# search_key = 'record_1'
# search_key_exist = sample_table.check_key(record_key=search_key)
# print(search_key_exist)
#
# # COUNT RECORDS (key value pairs) IN TABLE
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Table record count.
# table_record_count = sample_table.count_records()
# print(table_record_count)
#
# # DUPLICATE TABLE (JSON file) TO PRESENT WORKING DIRECTORY
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Duplicate table.
# sample_table.copy_table(table_file_name=table_name)
#
# # DUPLICATE TABLE (JSON file) TO ALTERNATE LOCATION (file system address)
# # Create alternate location.
# table_backup_location = os.path.join(os.getcwd(), 'sample_database', 'table_backup')
# os.mkdir(table_backup_location)
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Duplicate table.
# sample_table.copy_table(table_file_name=table_name, table_file_path=table_backup_location)
#
# # RENAME CURRENT TABLE (JSON file name)
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Rename table.
# new_table_name = table_name + '_renamed'
# sample_table.rename_table(old_table_name=table_name, new_table_name=new_table_name)
#
# # DELETE TABLE (JSON file from database directory)
# # Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Delete table.
# sample_table.delete_table(table_name=table_name)
#
# CREATE DICTIONARY CONSISTING OF TABLE RECORDS (key value pairs)
# Initialize table object.
# sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
# sample_table.set_database_directory()
# # Create dictionary.
# table_dictionary = sample_table.table_to_dictionary()
# for item in table_dictionary.items():
#     print(item)