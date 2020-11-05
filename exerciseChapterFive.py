num = 0
total = 0
while True:
    sval = input("Enter Number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("Invalid Input")
        continue

    num = num + 1
    total = total + fval

print(total, num, total/num)