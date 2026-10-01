print("=================================")
print("   SHOPPING DISCOUNT CALCULATOR  ")
print("=================================")

valid = False

while not valid:
    try:
        bill = float(input("Enter the total bill amount: "))
        discount_percent = float(input("Enter the discount percentage (e.g., 20 for 20%): "))
        num_people = int(input("Enter the number of people sharing the bill: "))

        discount_amount = bill * (discount_percent / 100)
        final_bill = bill - discount_amount
        amount_per_person = final_bill / num_people
    except ValueError:
        print("Please enter valid numbers only.")
    except ZeroDivisionError:
        print("The number of people cannot be zero.")
    else:
        print(f"Final bill after {discount_percent}% discount: ${final_bill:.2f}")
        print(f"Each person pays: ${amount_per_person:.2f}")
        valid = True
print("Attempt finished.")