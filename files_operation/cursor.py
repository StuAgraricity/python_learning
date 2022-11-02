files = open('configuration.txt', 'r')
content = files.read(2)
print(content)

content = files.read(10)
print(content)

print(files.tell())

pos = files.seek(5)
print(files.tell())
print(pos)
content = files.read(20)
print(content)

files.close()
