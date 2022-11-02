# Files Operation
Read and manipulate files


## [Open()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py) files
reading file in python use built in function **open()**
**open()** return value **file object**
close the file with **close()** method 

**open(1, 2)** parameters:
1. Path (mandatory): Path or location of the file
2. Mode (optional): combination of the first and second letter
  - First char is how the file will be opened
    - read (default): read-only mode 
    - write
    - append
  - Second char is the type of files
    - text (default): sequence of lines that end with EOL (End Of Line)
    - binary: non-text files 


**File Object** method:
- [read()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py): read the value of files and return it as string
- [close()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py): close the file and set **closed** attribute into **true**

**File Object** attribute:
- [closed](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py) (boolean): true if the file is not open


