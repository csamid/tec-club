# functions for club
import pandas as pd


def read_data():
    """Reads data if exists, if not creates empty DataFrame,
    returns DataFrame"""
    try:
        data = pd.read_csv(
            "tec_members_data.csv", index_col=False, converters={"id": str}
        )
    except FileNotFoundError:
        first_meeting = {
            "name": [],
            "email": [],
            "id": [],
            "attendance": [],
        }
        data = pd.DataFrame(first_meeting)

    return data


def new_member(existing_data):
    while True:
        # 1) ask for full name
        new_member_full_name = input(
            "Please enter your full name\nExample: Sam Sample\n: "
        )

        # 2) ask for lbcc email
        while True:
            new_member_lbcc_email = input(
                "Please enter your LBCC email\nExample: samsample@lbcc.edu\n: "
            )
            if new_member_lbcc_email[-9::] == "@lbcc.edu":
                break

            print("Invalid email, make sure its a lbcc email.")

        # 3) ask for lbcc ID
        while True:
            new_member_lbcc_id = input(
                "Please enter your LBCC ID\nExample: 0123456\n: "
            )
            if len(new_member_lbcc_id) == 7:
                break

            print("Invalid ID!")

        correct_info = input(
            f"Is this information correct:\nName: {new_member_full_name}\nEmail: {new_member_lbcc_email}\nID: {new_member_lbcc_id}\n[Y/N]: "
        ).upper()
        if correct_info == "Y":
            break

    new_member_data = [
        new_member_full_name,
        new_member_lbcc_email,
        new_member_lbcc_id,
        1,
    ]
    existing_data.loc[len(existing_data.index)] = new_member_data


def current_member(existing_data):
    """Updates the attendance of a current member"""
    while True:
        current_member_id = input("Please enter your LBCC ID to sign in: ")
        # get the row of data of that member
        member_info = existing_data[existing_data.id == current_member_id]
        if len(member_info) == 1:
            break
        else:
            print("Invalid ID!")

    # get index of row matched then
    member_index = member_info.index.values[0]
    # use current_data.loc[row,col] += 1
    existing_data.loc[member_index, "attendance"] += 1


def write_data(existing_data):
    """Writes the updated data into csv after sign-ins end"""
    existing_data.to_csv("tec_members_data.csv", index=False)
