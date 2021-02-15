def email(expected_email):
    for user_expected_email in expected_email:
        if user_expected_email == '@':
            return email

        user_email = input("enter your email: ")
        print(email(user_email))


def confirm_email(the_user_should_confirm_email):
    for email_confirmation in the_user_should_confirm_email:
        if email_confirmation == "Confirm, confirm":
            return confirm_email


def user(receiver, sender):
    for the_receiver_of_alert in receiver:
        if the_receiver_of_alert == "Confirm":
            print("Account confirm! You can now withdraw.")
        return receiver

    for the_sender_of_alert in sender:
        if the_sender_of_alert == "send":
            print("You transaction was successful!")
        return sender


def confirm(self):
    if self.confirm_email == confirm_email(self):
        print("Your email had been confirmed successfully.")
    else:
        print("Dear customer, you've not confirmed your email.")


def save_money(withdraw, transfer_out, transfer_in):
    amount = int(input("Enter the amount you want to save: "))

    if save_money(withdraw, transfer_in, transfer_out) == amount:
        print(f"The available balance is:{amount}")

        if withdraw >= amount:
            print(f"Your account had been debited with {withdraw}\n"
                  f"Your total balance is {amount - withdraw}.")
        else:
            print(f"Insufficient balance: {amount}")

        if transfer_in >= 0:
            print(f"Your account had been credited with: {amount + transfer_in} from ", amount + transfer_in)
        else:
            print(f"Insufficient balance: {amount - transfer_in}")

        if transfer_out <= amount:
            print(f"Insufficient balance: {amount}")
        else:
            print(f"No sufficient fund: {amount}")
    else:
        print()
