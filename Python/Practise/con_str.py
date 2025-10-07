# # ticket_status="Confirmed"
# # luggage_weight=32
# # weight_limit=30  #Weight limit for the airline
# # extra_luggage_charge=0
# # if(ticket_status=="Confirmed"):
# #     if(luggage_weight>0 and luggage_weight<=weight_limit):
# #         print("Check-in cleared")
# #     elif(luggage_weight<=(weight_limit+10)):
# #         extra_luggage_charge=300*(luggage_weight-weight_limit)
# #     else:
# #         extra_luggage_charge=500*(luggage_weight-weight_limit)
# #     if(extra_luggage_charge>0):
# #         print("Extra luggage charge is Rs.", extra_luggage_charge)
# #         print("Please make the payment to clear check-in")
# # else:
#     # print("Sorry, ticket is not confirmed")

# # luggage_weight=30
# # weight_limit=30  # Weight limit for the airline
# # extra_luggage_charge=0

# # if luggage_weight <= 0:
# #     print("Invalid luggage weight")
# # elif luggage_weight <= weight_limit:
# #     print("Check-in cleared")
# # elif luggage_weight <= weight_limit + 10:
# #     extra_luggage_charge = 300 * (luggage_weight - weight_limit)
# # else:
# #     extra_luggage_charge = 500 * (luggage_weight - weight_limit)

# # import random
# # x=10
# # y=50
# # print(random.randrange(x,y)) 


# # import math
# # num1=234.01
# # num2=6
# # num3=-27.01

# # print("The smallest integer greater than or equal to num1,",num1,":",math.ceil(num1))
# # print("The largest integer smaller than or equal to num1,",num1,":",math.floor(num1))
# # print("The factorial of num2,",num2,":", math.factorial(num2))
# # print("The absolute value of num3",num3,":",math.fabs(num3))



# # import time
# # import datetime

# # #To get current GM time
# # print("Current GM time:",time.gmtime())
# # #This returns a time structure containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.

# # #To get current local time
# # print("Current local time:",time.localtime())
# # #This also returns a time structure containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.

# # #To extract today's date in a specified string format
# # print("Today's date using time module",time.strftime("%m-%m/%Y"))

# # #Python additionally allows use of  datetime module
# # #Prints today's date
# # print("Today's date using datetime module:", datetime.date.today())

# # #To extract today's date in a specified string format
# # print("Today's date (dd/mm/yyyy) using datetime module:", datetime.date.today().strftime("%d/%m/%Y"))


# # #To convert a date in string format to datetime value
# # print("Today's date (dd/mm/yyyy):", datetime.datetime.strptime("17/04/1","%y/%d/%m"))

# #Creating a string
# pancard_number="AABGT6715H"

# #Length of the string
# print("Length of the PAN card number:", len(pancard_number))

# #Concatenating two strings
# name1 ="PAN "
# name2="card"
# name=name1+name2
# print(name)

# print("Iterating the string using range()")
# for index in range(0,len(pancard_number)):
#     print(pancard_number[index])
    
# print("Iterating the string using keyword in")
# for value in pancard_number:
#     print(value)

# print("Searching for a character in string")
# if "Z" in pancard_number:
#     print("Character present")
# else:
#     print("Character is not present")

# #Slicing a string
# print("The numbers in the PAN card number:", pancard_number[5:9])
# print("Last but one 3 characters in the PAN card:",pancard_number[-4:-1])

# # pancard_number[2]="A" #This line will result in an error, i.e., string is immutable
# print(pancard_number)

# # def generate_ticket(airline,source,destination,no_of_passengers):
# #     ticket_number_list=[]
# #     #Write your logic here
# #     for num in range(101, no_of_passengers):
# #         ticket_number_list.append(f'{airline}:{source}{[:3]}:{num}')
# #     #Use the below return statement wherever applicable
# #     return ticket_number_list

# # #Provide different values for airline,source,destination,no_of_passengers and test your program
# # print(generate_ticket("AI","Bangalore","London",7))

# boarding_call="Good Evening, this is the final call to AI passengers for the flight AI 466 which is planned to take off at 8.40A.M."

# if(boarding_call.startswith("Good Evening")):
#     print(boarding_call.replace("Good Evening","Good Morning"))

# if(boarding_call.find("AI"))>=0:
#     print("Welcome to Air India.")

# if(boarding_call.endswith("A.M.")):
#     print("Passengers are requested to have their breakfast.")

# a=boarding_call.split(" ")
# for i in a:
#     if(i.isdigit()):
#         print("Flight Number is specified to the passengers.")

# print("Total number of times flight service name is specified in the boarding call:",boarding_call.count("AI"))


# message="Thank you all..Have a nice journey!"

# print(message.upper())

# print(message.lower())


# row1 = (101,"Dallas",3.5)
# row2 = (102,"Atlanta",5.6)
# row3 = (103,"Tokyo",9.8)
# table = [row1,row2,row3]
# print(table[0])
# print(table[1])
# print(table[2])

# pancard_list=["AABGT6715H", "UFFAC4352T", "IFSBD9163K", "JOOEC1225H","RWXAFE187B"] 

# val= pancard_list[3][6]
# print(val, end=" ")
# print(pancard_list[4][3:])


# song="JINGLE Bells jingle Bells Jingle All The Way"
# song.upper()
# song_words=song.split()
# count=0
# for word in song_words:
#     if(word.startswith("jingle")):
#         count=count+1
# print(count)


# def count_names(name_list):
#     count1=0
#     count2=0
    
#     #start writing your code here
#     #Populate the variables: count1 and count2

#     # Use the below given print statements to display the output
#     # Also, do not modify them for verification to work
#     for name in name_list:
#         if str(name).encode("_at"):
#             count1 += 1
#         if str(name).encode("%at%"):
#             count2 += 1
#     print("_at -> ",count1)
#     print("%at% -> ",count2)



# #lex_auth_01273338869591244855
# count=0
# i=1
# for baggage_weight in 29, 30, 31, 32, 28:
#     if(baggage_weight <= 30):
#         print("Passenger",i,": Proceed for baggage check.")
#         count+=1
#     else:
#         print("Passenger",i,": Maximum baggage weight allowed is 30kg.")
#     i+=1

# print("No. of passengers who cleared baggage check:", count)

def find_common_characters(msg1,msg2):
    #Remove pass and write your logic here
    msg1 = "".join(msg1)
    msg2 = "".join(msg2)
    
    common_msg = ""
    for msg1_char in msg1:
        for  msg2_char in msg2:
            if msg1_char == msg2_char and msg1_char not in common_msg:
                common_msg += msg1_char
                
    return "".join(common_msg)

msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)