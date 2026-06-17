#today we are going to make write and readfiles

with open ("day6/notes.txt", "w") as f:
    f.write("hello from day 6\n")
    f.write("Learning files I/o\n")
    f.write("I can do it\n")
  
#after  write a file we will read it 
with open("day6/notes.txt", "r") as f:
    content = f.read()
    print(content)
    
#we will read line by line using a generator

with open("day6/notes.txt", "r") as f:
    for line in f:
        print(line.strip())