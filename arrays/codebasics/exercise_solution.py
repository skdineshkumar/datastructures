#Solution for question number 1:

expenses = [2200, 2350, 2600, 2130, 2190]
months = ["January", "February", "March", "April", "may", "June"]

print ("Dollars spent extra in Feb: ", expenses[1] - expenses[0])
print ("Expenses in first quarter: ", expenses[0] + expenses[1] +expenses[2])

# Find if any month has exactly 2000 spent
for i in range(len(expenses)):
    if expenses[i] == 2000:
        print ("Yes, we have spent exactly 2000 on month of",months[i])
        break
else:
    print ("No, we haven't spent exactly 2000 in any of the months")

#Adding expense of June
expenses.append(1980)
print ("New expeses list after adding June :",expenses)

#Updating Aprils expense
expenses[3] = expenses[3] - 200
print ("Updated expenses list after April's refund :",expenses)


print ("Did I spent 2000 in any months :", 2000 in expenses)


#***********************************************************************#

#Solution for question number : 2


heros=['spider man','thor','hulk','iron man','captain america'] 

#1
print ("Lenght of the list is: ", len(heros))

#2
print ("Adding 'Black Panther to the list")
heros.append('black panther')
print (heros)

#3
print ("Moving black panther next to hulk")
heros.pop()
heros.insert(3, 'black panther')

print (heros)

#4
heros[1:3] = ['doctor strange']
print (heros)

#5
heros.sort()

print (heros)




#*******************************************************************************

#Solution for question number : 3
#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function


user_input = int(input("Enter the max number :"))
odd_number_list = []

for i in range(user_input + 1):
       if i % 2:
        odd_number_list.append(i)
print ("The odd number list: ",odd_number_list)

