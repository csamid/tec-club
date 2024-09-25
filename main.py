# have a gui (tkinter or qt) and have a new member button
# exsiting club members only have to enter their ID or Name they
# use when they were a new member
import club

# read current data
data = club.read_data()

end_program = False
while not end_program:
    print("Welcome the the TEC Club!")

    while True:
        new_member = input("Are you a new member? Y or N: ").upper()
        if new_member in ["Y", "N"]:
            break  # exit loop if the input is vaild
        elif new_member == "END-SIGN-INS":
            end_program = True
            break

        print("Invalid input. Please enter 'Y' or 'N")

    if new_member == "Y":
        club.new_member(data)

    elif new_member == "N":
        club.current_member(data)

    else:
        print("Hi")

club.write_data(data)
