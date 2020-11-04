largest_num = 0

arrayOfNumbers = [23, 1 ,3 ,5 ,6 ,46 ,28 ,76 ,97 ,34 ,56]

print("Before", largest_num)
for number in arrayOfNumbers:
    #Check if number is larger than the number before
    if number > largest_num:
        #Assigen
        largest_num = number
    print(largest_num, number)

print("After", largest_num)