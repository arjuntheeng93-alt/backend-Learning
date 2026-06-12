def read_file(filename): #we make function to read a file, takes a filename as an argument
    try:# we use a try block to attempt to open the file and read its content, if the file does not exist, it will raise a FileNotFoundError
        with open(filename, 'r') as f: #try to open the file in read mode, if the file does not exist, it will raise a FileNotFoundError
            content = f.read() #if the file is opened successfully, read its content and store it in the variable content
    except FileNotFoundError as e: #catch the FileNotFoundError exception, which occurs when the file does not exist
        print(f"Error: {e}")
    else:# the else block will execute if no exceptions were raised in the try block, it is typically used to execute code that should only run if the try block was successful, such as processing the data read from a file or performing additional operations that depend on the success of the try block
        print(f"file read successfully: {content}")
    finally: #the finally block will always execute, regardless of whether an exception was raised or not, it is typically used for cleanup actions that must be executed under all circumstances, such as closing files or releasing resources
        print("This always runs, whether the expection occer or not")
        
read_file("fake_file.txt") #try to read a file that does not exist, should catch the FileNotFoundError and print the error message, then print the message in the finally block
read_file("day4/exercise1.py")
    