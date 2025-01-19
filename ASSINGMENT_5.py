
# EXERCISE-1:
file1=open("C:\\Users\\anshe\\OneDrive\\Desktop\\Python_assngmt-5-file.txt","r")
print(file1.read())


# EXERCISE-2:
file2=open("C:\\Users\\anshe\\OneDrive\\Desktop\\Python_assngmt-5-file.txt",'r')
content=file2.read()
file3=open("C:\\Users\\anshe\\OneDrive\\Desktop\\Python-assignmt-tofile.txt",'w')
file3.write(content)
file3.close()
file3=open("C:\\Users\\anshe\\OneDrive\\Desktop\\Python-assignmt-tofile.txt",'r')
text=file3.read()
print(text)

# EXERCISE-3:
file4=open("C:\\Users\\anshe\\OneDrive\\Desktop\\Python_assngmt-5-file.txt",'r')
content=file4.read()
words=content.split()
print("Total no.of word in the file is ",len(words))


# EXERCISE-4:
input=input("enter a string:")
try:
    int1=int(input)
    print(int1)
except:
    print("This is not a number string")
finally:
    print("For proper execution enter number string")



# Exercise-5:

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



# Exercise-6:

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

# Exercise-7:
try:
    name=input("Enter the file_name=")
    with open(name,'w') as file1:
        string=input("Enter the file content:")
        file1.write(string)
        file1.close()
    print(f"Welcome to the {name} file")


except:
    print("Unexpected error occur")