# ALU Back-End API Tasks

This repository contains Python scripts for managing employee TODO data using a REST API.  
All scripts are located in the `api` folder.

## Scripts Overview

1. **0-gather_data_from_an_API.py**  
   - Fetches TODO list progress for a given employee.  
   - **Usage:**  
     ```bash
     python 0-gather_data_from_an_API.py <EMPLOYEE_ID>
     ```
   - **Example:**  
     ```bash
     python 0-gather_data_from_an_API.py 2
     ```
     Output:
     ```
     Employee Ervin Howell is done with tasks(8/20):
         distinctio vitae autem nihil ut molestias quo
         voluptas quo tenetur perspiciatis explicabo natus
         ...
     ```

2. **1-export_to_CSV.py**  
   - Exports all tasks of a given employee to a CSV file.  
   - **Usage:**  
     ```bash
     python 1-export_to_CSV.py <EMPLOYEE_ID>
     ```
   - Generates a file named `<EMPLOYEE_ID>.csv` in the current folder.  
   - CSV Format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`

3. **2-export_to_JSON.py**  
   - Exports all tasks of a given employee to a JSON file.  
   - **Usage:**  
     ```bash
     python 2-export_to_JSON.py <EMPLOYEE_ID>
     ```
   - Generates a file named `<EMPLOYEE_ID>.json` in the current folder.  
   - JSON Format:
     ```json
     {
       "USER_ID": [
         {"task": "TASK_TITLE", "completed": true, "username": "USERNAME"},
         ...
       ]
     }
     ```

4. **3-dictionary_of_list_of_dictionaries.py**  
   - Exports tasks of **all employees** to a single JSON file.  
   - **Usage:**  
     ```bash
     python 3-dictionary_of_list_of_dictionaries.py
     ```
   - Generates a file named `todo_all_employees.json` in the current folder.  
   - JSON Format:
     ```json
     {
       "USER_ID": [
         {"username": "USERNAME", "task": "TASK_TITLE", "completed": true},
         ...
       ],
       ...
     }
     ```

## Requirements

- Python 3.x  
- `requests` library  
  Install via pip:
  ```bash
  pip install requests
