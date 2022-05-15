#####WHY LOGGING OVER PRINT ?#####
# print statements missing contextual information such as time of occurence, linenumber, module

# noo straightforward way to format the output of print statement

# writing print statement output to sources other than the terminal is non trivial & requires 
# significant amount of coding for file handling, threading, email sending etc

def return_sum_of_two_numbers(a, b):
    print(f"Inside function to add [a={a}, b={b}]")
    try:
        print("There are no checks if the inputs are integers")
        return a + b
    except Exception as ex:
        print("%s", ex)


print(return_sum_of_two_numbers(10,20))

# print(return_sum_of_two_numbers(10,'a'))

