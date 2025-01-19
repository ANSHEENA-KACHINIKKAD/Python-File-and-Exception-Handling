# Python-File-and-Exception-Handling
File handling and Exception handling -Python programs.

## Exercise-1:
  Python program to read a file and display its contents.

  code:
  
    file1=open("C:\\Users\\anshe\\OneDrive\\Desktop\\Python_assngmt-5-file.txt","r")
    print(file1.read())

  Explanation:
  
   * Create a text file named " Python_assngmt-5-file" in desktop.
   * Then open the file using the open function
   * Read the content in the file and display it.


## Exercise-2:
  Python program to copy the contents of one file to another file.

  code:
  
    file2=open("C:\\Users\\anshe\\OneDrive\\Desktop\\Python_assngmt-5-file.txt",'r')
    content=file2.read()
    file3=open("C:\\Users\\anshe\\OneDrive\\Desktop\\Python-assignmt-tofile.txt",'w')
    file3.write(content)
    file3.close()
    file3=open("C:\\Users\\anshe\\OneDrive\\Desktop\\Python-assignmt-tofile.txt",'r')
    text=file3.read()
    print(text)

  Explanation:
  
   * Create a text file named " Python_assngmt-5-file" in desktop.
   * Then open the file using the open function
   * Read the content in the file as a new variable.
   * Create another text file named "Python assignmt-tofile"
   * Open the file in write mode and write the content in the new variable to the file using write() then close the file.
   * Then open the new file as read mode and read it also display it.


## Exercise-3:
  Python program to read the content of a file and count the total number of words in that file.

  code:
  
    file4=open("C:\\Users\\anshe\\OneDrive\\Desktop\\Python_assngmt-5-file.txt",'r')
    content=file4.read()
    words=content.split()
    print("Total no.of word in the file is ",len(words))

  Explanation:
  
   * Create a text file named " Python_assngmt-5-file" in desktop.
   * Then open the file as read mode.
   * Read the content in the file as a new variable named "content".
   * Split the word in the text and make it list using split() and assinged to variable with name "words".
   * Print the length of words named list it indicates the Total number of words in the content.


## Exercise-4:
  Python program that prompts the user to input a string and converts it to an integer. Use try-except blocks to handle any exceptions that might occure.

  code:
  
    input=input("enter a string:")
    try:
    int1=int(input)
    print(int1)
    except:
    print("This is not a number string")
    finally:
    print("For proper execution enter number string")

  Explanation:
  
   * Prompts the user for input.
   * Tries to convert the input string to an integer using int().
   * try...except ValueError: block specifically catches ValueError exceptions that occur when the input string cannot be converted to an integer.
   * finally: block executes regardless of whether an exception occurred or not.
   * It prints "For proper execution enter number string" to give general guidance to the user.



## Exercise-5:
  Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative.

  code:
  
    def get_positive_integer_list():
    while True:
        try:
            num = int(input("enter the list element:"))
            if num <= 0:
                raise ValueError("The negative list element not allowed !")
            return num
        except ValueError as e:
            print(f"Error {e}")

    try:
    num_elements=int(input("Enter the number of elemnets:"))
    if num_elements<=0:
        raise ValueError("Number of elements should be positive integer.")
    positive_list=[]
    for _ in range(num_elements):
        positive_list.append(get_positive_integer_list())

    print("Positive integer list ",positive_list)
    except ValueError as e:
    print(f"Error is {e}")

  Explanation:
  
   * Defines a function named get_positive_integer_list(). This function will be responsible for getting a single positive integer from the user.
   * The code within the try block will be executed, and if any exceptions occur, they will be handled by the except block that follows.
   * Prompts the user to "enter the list element" and then attempts to convert the user's input into an integer using the int() function.
   * Checks if the entered number is less than or equal to zero.If the condition is true then it raises a ValueError with the message "The negative list element not allowed !".Otherwise return the number.
   * another try block for the main part of the code,prompts the user to enter the number of elements they want in the list.
   * creates an empty list named positive_list to store the valid positive integers entered by the user.Then starts a loop that will iterate num_elements times.
   * In each iteration of the loop, this line calls the get_positive_integer_list() function.The function will prompt the user for a positive integer and return it.
   * The returned value (the positive integer) is then appended to the positive_list.
   * Display the list.


## Exercise-6:
  Python program that prompts the user to input a list of integers and computes the average of those integers. Use try-except blocks to handle any exceptions that might occur.use the finally clause to 
  print a message indicating that the program has finished running.

  code:
  
    def get_positive_integer():
    while True:
         try:
            num=int(input("Enter the list elements:"))
            if num<=0:
                 raise ValueError("The number should not less than zero!")
            return num
         except ValueError as e:
             print(f"Error:{e}")


    len_list=int(input("Enter the number of list elements:"))
    positive_list=[]
    for _ in range(len_list):
        positive_list.append(get_positive_integer())

    try:
    Average=sum(positive_list)/len(positive_list)
    print("Average of list:",Average)
    except:
    print("Unexpected error occur in the Average")

    finally:
    print("program has finished running!")

  Explanation:

   * Defines a function named get_positive_integer(). This function is designed to get a single positive integer from the user.
   * begins a try block. The code inside this block will be executed, and if any exceptions occur within this block, they will be handled by the corresponding except block.
   * prompts the user to "Enter the list elements" and then attempts to convert the user's input into an integer using the int() function.
   * checks if the entered number is less than or equal to zero,If condition is true raises a ValueError with the message "The number should not less than zero!". This signals that the input is invalid.
   * If the number is positive (greater than zero), this line returns the valid integer value. This effectively exits the try block and breaks out of the while loop.
   * prompts the user to "Enter the number of list elements" and then converts the user's input into an integer.creates an empty list named positive_list
   * arts a loop that will iterate len_list number of times,In each iteration of the loop, this line calls the get_positive_integer() function.
   * The get_positive_integer() function will prompt the user for a positive integer and return it.The returned value (the positive integer) is then appended to the positive_list.
   * another try block for the average calculation,prints the calculated average to the console.
   * except block that will catch any exception that occurs during the average calculation. It's generally not recommended to use a general except block without specifying the type of exception you're 
     expecting, as it can mask unexpected errors.
   * If any exception occurs within the average calculation try block, this line prints a generic error message.
   * Finally block  prints the message "program has finished running!" to indicate that the program has completed its execution.

## Exercise-7:
  Python program that prompts the user to input a filename and writes a string to that file. Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no 
  exception occurred.

  code:
  
    try:
    name=input("Enter the file_name=")
    with open(name,'w') as file1:
        string=input("Enter the file content:")
        file1.write(string)
        
    print(f"Welcome to the {name} file")


    except:
    print("Unexpected error occur")

  Explanation:
  
   * begins a try block. The code within this block is executed, and if any errors occur during its execution, the program will jump to the except block.
   * prompts the user to enter the desired filename and stores the user's input in the variable name.
   * open(name, 'w') attempts to open a file with the given filename (name) in "write" mode ('w').
   * If the file doesn't exist, it will be created,If the file already exists, it will be overwritten.
   * assigns the opened file object to the variable file1.
   * prompts the user to enter the content they want to write to the file and stores the input in the variable string.
   * writes the content stored in the string variable to the file represented by the file1 object.file is automatically closed when the with block ends.
   * prints a success message indicating that the file has been created/written to successfully.
   * If any error occurs within the try block, the program execution will jump to this block.
   * prints a generic error message "Unexpected error occur" if any exception is encountered.
