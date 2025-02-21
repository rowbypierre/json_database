# JSON Database

---

The Udemy course [Python Programming - Foundation Course for Data Engineers by Prashant Kumar Pandey and Satyam Kumar](https://www.udemy.com/share/103S4m3@WqEPRqkVqBgOREnp0JdXZ5Rr8LO_Up30nMLXhjVdRiOPY-nJE6TVWAvEWOwavP0hYA==/) 
captsone project served as inspiration for this repository. 

The code within this repository is original. Furthermore, several database and table instance methods were added to 
enhance the module's functionalities. 

The provided modules will allow users to create:
+ Database(s) using the host's file system to save data. 

+ Record(s) existing as key value pairs within tables existing as files adhering to JavaScript Object Notation format.

Note: Program includes function to store and retrieve Python class instances as a record value.

A database exist as a directory containing one or more tables (JSON formatted files).

## Getting Started

---

- [x] Python is installed (version 3.x recommended).
- [x] Download project files.

## Definitions

---

__Database__:
   File system folder or directory.

__Table__: 
   Text file formated in adherence to JavaScript Object Notation.

__Record__:
   Key value pair written to table (see previous definition).

__Record key__:
   Key of key value pair.

__Record value__:
   Value of key value pair.

__Database object__:
   File located in database (see database definition).

__Database table__:
   JSON formatted file located within database (see database definition).

## Create & Manage a Database

---
1. Import modules.
   ```python
   from json_database.database.key_value_database import KeyValueDatabase
   from json_database.table.key_value_table import KeyValueTable
   ```
2. Create a database:
   1. Create database object.
      ``` python
      from json_database.database.key_value_database import KeyValueDatabase
      
      # Database information.    
      database_name = 'sample_database'
      # Database and table object.
      sample_database = KeyValueDatabase(database_name=database_name)
      ```
   2. Set the working directory.
      ``` python
      # Set database files destination as current working directory.
      sample_database.set_database_directory()
      
      # Set alternate location for database files.
      # Note: if provided path below does not exist, the program will attempt to create the path.
      # Location.
      database_location = os.path.join(os.getcwd(), 'new_database_directory')
      # Set alternate path.
      sample_database.set_database_directory(use_current_directory=False, new_directory_path=database_location)
      ```
   3. Create the database (folder/ directory).
      ``` python
      # Create database directory (folder containing table as json files).
      sample_database.create_database()
      ```

3. Manage database:
   1. Clone.
      ``` python
      # Copy database.
      copy_database_path = os.path.join(os.getcwd(), 'sample_database_copy')
      sample_database.copy_database(copy_database_path=copy_database_path)
      ```
   2. Delete.
      ``` python
      # Delete database.
      delete_database_path = os.path.join(os.getcwd(), 'new_database_directory')
      sample_database.delete_database(delete_database_path)
      ```
   3. Rename.
      ``` python
      # Rename database.
      sample_database.rename_database(new_database_name='sample_database_renamed')
      ```

## Additional Database Functionalities

---

+ List database objects.
   ``` python
   # - List database objects (tables & etc).
   print(sample_database.list_database_objects())
   ```
+ Count of database objects.
   ``` python
   # - Count database objects.
   print(len(sample_database.list_database_objects()),
      sample_database.count_database_objects())
   ```
+ List database tables.
   ``` python
   # - List database tables only.
   print(sample_database.list_database_tables())
   ```
+ Count of database tables.
   ``` python
   # - Count database tables.
   print(len(sample_database.list_database_tables()),
         sample_database.count_database_tables())
   ```
  
## Create & Manage a Table

---

1. Create a Table:
   1. Create table object.
      ``` python
      # Initialize table object.
      sample_table = KeyValueTable(database_name=database_name, table_name=table_name) 
      ```
   2. Set the working directory.
      ``` python
      # Set database files destination as current working directory.
      sample_table.set_database_directory()
      ```
   3. Create a record (key value pair).
      ``` python
      # Create record (key value pair).
      new_record = {'testing': 'new record'}
      sample_table.set_pair(pair_key=new_record[0], pair_value=new_record[1])
      ```

2. Manage table:
   1. Create record.
      ``` python
      # print('See the example right above.')
      ```
   2. Create record with record value as an instance.
      ``` python
      # Create record (key value pair).
      new_programmer = Programmer(first_name='rowby', last_name='pierre', age=27, language='Python')
      new_programmer.print_bio()
      new_record = {'instance': new_programmer}
      sample_table.set_pair(record_key=new_record[0], record_value=new_record[1])
      ```
   3. Delete record.
      ``` python
      # Create record (key value pair)
      new_record = {'testing': 'new record'}
      sample_table.set_pair(record_key=new_record[0], record_value=new_record[1])
      # Delete record.
      sample_table.delete_pair(record_key=new_record[0])
      ```
   4. Retrieve record value.
      ``` python
      # Get record value (value of key value pair).
      new_record_value = sample_table.get_value(record_key=new_record[0])
      print(new_record_value)
      ```
   5. Retrieve record key that's an instance.
      ``` python
      # Get record value (value of key value pair).
      programmer_record = sample_table.get_value(record_key=new_record[0])
      programmer_record.print_bio()
      ```
   6. Clone table.
      ``` python
      # Create alternate location.
      table_backup_location = os.path.join(os.getcwd(), 'sample_database', 'table_backup')
      os.mkdir(table_backup_location)
      # Initialize table object.
      sample_table = KeyValueTable(database_name=database_name, table_name=table_name)
      sample_table.set_database_directory()
      # Duplicate table.
      sample_table.copy_table(table_file_name=table_name, table_file_path=table_backup_location)
      ```
   7. Rename table.
      ``` python
      # Rename table.
      new_table_name = table_name + '_renamed'
      sample_table.rename_table(old_table_name=table_name, new_table_name=new_table_name)
      ```
   8. Delete table.
      ``` python
      # Delete table.
      sample_table.delete_table(table_name=table_name)
      ```

## Additional Table Functionalities

---
+ Retrieve all table keys.
   ``` python
   # Table keys.
   table_keys = sample_table.get_all_keys()
   print(table_keys)
   ```
+ Create python dictionary containing all table records.
   ``` python 
  # Create dictionary.
  table_dictionary = sample_table.table_to_dictionary()
  for item in table_dictionary.items():
    print(item)
   ```
+ Retrieve all table keys with specific record value.
   ``` python
   # Table keys with specific value.
   search_value = 'value'
   table_keys = sample_table.get_key(record_value=search_value)
   print(table_keys)
   ```
+ Check if record key exists.
   ``` python
   # Table keys with specific value.
   search_key = 'record_1'
   search_key_exist = sample_table.check_key(record_key=search_key)
   print(search_key_exist)
   ```
+ Count table records.
   ``` python
   # Table record count.
   table_record_count = sample_table.count_records()
   print(table_record_count)
   ```