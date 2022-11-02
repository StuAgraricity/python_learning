# Files Operation
Read and manipulate files

## [Open()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py) files
reading file in python use built in function **open()**<br/>
**open()** return value **file object**<br/>
close the file with **close()** method<br/>
<br/>
**open(1, 2)** parameters:
1. filename (mandatory): Path or location of the file
2. mode (optional): combination of the first and second letter
  - First char is how the file will be opened
    - read (default): read-only mode 
    - write
    - append
  - Second char is the type of files
    - text (default): sequence of lines that end with EOL (End Of Line)
    - binary: non-text files 

## [File Objects](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py)
#### File Object method:<br/>
- [read()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py): read the value of files and return it as string
  - [size](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/cursor.py) (optional): the number of bytes to return
- [tell()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/cursor.py): returns the current file position in a file stream
- [seek()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/cursor.py): set the current file position in a file stream and return the new position
  - [offset](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/cursor.py): number representing the position to set the current file stream position
- [close()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py): close the file and set **closed** attribute into **true**

#### File Object attribute:
- [closed](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py) (boolean): true if the file is not open

## [Cursor](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py) <br/>
currently position inside the files<br/>
the position will be updated into "after the last char we read"<br/>
use **tell()** to get the position of cursor<br/>
use **seek()** to set the position of cursor<br/>

