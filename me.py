hoursInput = float(input("Enter Hours:"))
rateInput = float(input("Enter Rate:"))

def calculatePayHour(hours, rate):
    if hours < 40:
        return hours * rate
    elif hours >= 40:
        #First we get over hours * 1.5 then * to rate
        return (((hours - 40) * 1.5) + 40) * rate

print(calculatePayHour(hoursInput, rateInput))