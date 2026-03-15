def calculate_hike(currentCTC,hikePercentage):
    #calculate the hike amount and new CTC
    hikeAmount=(currentCTC*hikePercentage)/100
    newCTC=currentCTC+hikeAmount
    return hikeAmount,newCTC
def main():
    print("--------The Salary Hike Calculator----------------")
    try:
        print("--------Enter the Details----------------")
        currentCTC=float(input("Enter your current CTC: "))
        hikePercentage=float(input("Enter your hike percentage: "))
        if currentCTC<=0 or hikePercentage<0:
            if currentCTC==0:
                print("Current CTC cannot be zero")
                return
            else:
                print("Current CTC and hike percentage cannot be negative")
                return
        else:
            #Perform the calculation
            hikeAmount,newCTC=calculate_hike(currentCTC,hikePercentage)
        #Display the results
        print("--------Results----------------")
        print(f"Your current CTC is {currentCTC:,.2f}")
        print(f"Your hike percentage is {hikePercentage}%")
        print(f"Your hike amount is {hikeAmount:,.2f}")
        print(f"Your new CTC is {newCTC:,.2f}")
        print("--------Thank you for using the Salary Hike Calculator----------------")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
main()