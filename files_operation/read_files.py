files = open('configuration.txt', 'r')
content = files.read()
print(content)
print(files.closed)
files.close()
print(files.closed)
