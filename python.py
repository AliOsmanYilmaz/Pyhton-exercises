
#welcome to python exercises
#Select with Ctrl + K then Ctrl + U to uncomment the code blocks

#-----------------------------------------------------------------


# Check if a number is prime #


# print("Check if a number is prime")
# isPrime = True
# a = 2

# number = int(input("Enter a number: "))
        
# if number <= 1 :
#     isPrime = False

# while a != number:
#      if number % a == 0:
#          isPrime = False
#          break
#      a += 1

# if isPrime:
#      print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")   




#-------------------------------------------------------------------

#  Count the number of divisors of a number  #


# print("Count the number of divisors of a number")
# count = 0
# a = 1
# i = 1
# number = int(input("Enter a number: "))

# while a <= number:
#     if number % a == 0:
#         count += 1
#         print(i,". element is ",a)
#         i += 1
#     a += 1

# print("Count : ",count)    




#-------------------------------------------------------------------

#  Sum of digits of a number  #


#print("Sum of digits of a number")
# sum = 0
# number = int(input("Enter a number: "))

# number_str = str(number)

# for digit in number_str:
#     sum += int(digit)

# print("Sum of digits : ",sum)




            #OR



# print("Sum of digits of a number")
# sum = 0
# number = int(input("Enter a number: "))

# while number > 0:
#     digit = number % 10
#     sum += digit
#     number = number // 10  #integer division

# print("Sum of digits : ",sum)    




#-------------------------------------------------------------------

#  Find maximum and minimum number from a list of numbers  #


# print("Find maximum and minimum number from a list of numbers")
# numbers = [1,2,3,4,5]
# numbers[0] = int(input("Enter first number: "))
# numbers[1] = int(input("Enter second number: "))
# numbers[2] = int(input("Enter third number: "))
# numbers[3] = int(input("Enter fourth number: "))
# numbers[4] = int(input("Enter fifth number: "))

# max_number = numbers[0]

# for num in numbers:
#     if num > max_number:
#         max_number = num

# min_number = numbers[0]

# for num in numbers:
#     if num < min_number:
#         min_number = num        

# print("Maximum number is : ",max_number)
# print("Minimum number is : ",min_number)        




                #OR



# print("Find maximum and minimum number from a list of numbers")
# numbers = []      

# for index in range(5):
#     number = int(input("Enter number : "))
#     numbers.append(number)

# print("Maximum number is : ",max(numbers))
# print("Minimum number is : ",min(numbers))


#-------------------------------------------------------------------

#  Check if a number is a perfect square  #


# print("Check if a number is a perfect square")
# a = 1
# number = int(input("Enter a number: "))
 
# while(a * a <= number):
#     if (a * a == number):
#         print(f"{number} is a perfect square.")
#         break
#     a += 1  

# if (a * a != number):
#     print(f"{number} is not a perfect square.")



    
                #OR


# print("Check if a number is a perfect square")
# import math
# number = int(input("Enter a number: "))

# if math.sqrt(int(number)).is_integer():
#     print(f"{number} is a perfect square.")

# else:
#     print(f"{number} is not a perfect square.")




                #OR             



# print("Check if a number is a perfect square")
# number = int(input("Enter a number: "))
# sqrt = number ** 0.5

# if sqrt == int(sqrt):
#     print(f"{number} is a perfect square.")
# else:
#     print(f"{number} is not a perfect square.")



#-------------------------------------------------------------------

#  Count frequency of each character in a string  #



# print("Count frequency of each character in a string")
# string = input("Enter a string: ")
# string = string.replace(" ", "")  # Remove spaces
# string = string.lower() # Convert to lowercase
# dictionary = dict()

# for char in string:
#     if char in dictionary:
#         dictionary[char] += 1
#     else:
#         dictionary[char] = 1

# print("Character frequencies:")
# for char, freq in dictionary.items():
#     print(f"'{char}': {freq}")




#-------------------------------------------------------------------

#  Replace all occurrences of 'a' with 'A' in a string  #


# print("Replace all occurrences of 'a' with 'A' in a string")
# string = input("Enter a string: ")
# string = string.replace(" ", "") # Remove spaces
# string2 = ""

# for char in string:
#     if char == "a":
#         string2 += "A"
#     else:
#         string2 += char

# print("Modified string:",string2)



                #OR



# print("Replace all occurrences of 'a' with 'A' in a string")
# string = input("Enter a string: ")
# string = string.replace(" ", "") # Remove spaces

# for char in string:
#     if char == "a":
#         string = string.replace("a","A")

# print("Modified string:",string)


#-------------------------------------------------------------------