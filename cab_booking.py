       
while True:
    print("\n===== CAB BOOKING CHATBOT =====")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nSelect Cab Type")
        print("1. Auto - Rs.12/km")
        print("2. Sedan - Rs.18/km")
        print("3. SUV - Rs.25/km")

        cab_choice = input("Choose cab: ")

        if cab_choice == "1":
            cab = "Auto"
            rate = 12
        elif cab_choice == "2":
            cab = "Sedan"
            rate = 18
        elif cab_choice == "3":
            cab = "SUV"
            rate = 25
        else:
            print("Invalid cab choice!")
            continue

        print("\nSelect Route")
        print("1. Pune Station to Shivajinagar - 5 km")
        print("2. Swargate to Kothrud - 8 km")
        print("3. Hinjawadi to Wakad - 10 km")

        route_choice = input("Choose route: ")

        if route_choice == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route_choice == "2":
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif route_choice == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid route choice!")
            continue

        fare = distance * rate

        print("\n===== FARE DETAILS =====")
        print("Cab:", cab)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "/km")
        print("Total Fare: Rs.", fare)

        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm = input("Enter your choice: ")

        if confirm == "1":
            otp = 4821
            print("Your OTP is:", otp)
            print("Cancellation is not allowed after OTP sharing.")
            print("Booking Confirmed!")

        elif confirm == "2":
            print("Ride cancelled. No OTP shared.")

        else:
            print("Invalid confirmation choice. Booking not confirmed.")

    elif choice == "2":
        print("Thank you......Goodbye.")
        break

    else:
        print("Invalid choice! Please select 1 or 2.")


        



