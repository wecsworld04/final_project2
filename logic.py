from PyQt6.QtWidgets import *
from bank_account import *
import csv


class Logic(QMainWindow, Ui_bank_account):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.login_button.clicked.connect(lambda: self.login())
        self.submit_button.clicked.connect(lambda: self.submit())
        self.exit_button.clicked.connect(lambda: self.exit())
        self.exit_button.hide()

        self.login_count = False
        self.error_label = QLabel(self.centralwidget)
        self.error_label.setGeometry(420, 200, 200, 20)

        self.balance_label = QLabel(self.centralwidget)
        self.balance_label.setGeometry(420, 230, 200, 20)

        self.account_type = None
        self.c_balance = 100

    def login(self):
        """
        Handles the login process.
        """
        try:
            first_name_input = self.name_input.text()
            last_name_input = self.last_label.text()
            id_input = self.pin_input.text()

            if not str(first_name_input) or not str(last_name_input):
                self.error_label.setText("Please enter valid first and last name.")
                self.error_label.adjustSize()
                return

            with open('bank_info.csv', 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for line in reader:
                    if len(line) < 3:
                        continue
                    if line[0] == first_name_input and line[1] == last_name_input and line[2] == id_input:
                        # Successful login
                        self.login_count = True
                        self.clear()
                        self.error_label.setText("You have successfully logged in.")
                        self.error_label.adjustSize()
                        self.login_button.hide()
                        self.pin_input.hide()
                        self.label_4.hide()
                        self.exit_button.show()
                        self.name_input.setText(first_name_input)
                        self.last_label.setText(last_name_input)
                        return

                # Invalid login
                self.error_label.setText("Invalid credentials. Please try again.")
                self.error_label.adjustSize()

        except FileNotFoundError:
            self.error_label.setText("Login information not found.")
            self.error_label.adjustSize()

    def submit(self):
        """
               Handles the submission of transactions.
        """
        if self.login_count:
            amount_text = self.amount_input.text()
            if not amount_text:
                self.error_label.setText("Please enter an amount.")
                self.error_label.adjustSize()
                return

            try:
                amount = float(amount_text)
            except ValueError:
                self.error_label.setText("Invalid amount. Please enter a valid number.")
                self.error_label.adjustSize()
                return

            if not (self.checking_acc_button.isChecked() or self.saving_acc_button.isChecked()):
                self.error_label.setText("Please select at least one account type.")
                self.error_label.adjustSize()
                return

            if not (self.deposit_button.isChecked() or self.withdraw_button.isChecked()):
                self.error_label.setText("Please select at least one action.")
                self.error_label.adjustSize()
                return

            account_type = "Savings" if self.saving_acc_button.isChecked() else "Checking"
            c_balance = None

            with open('bank_info.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for line in reader:
                    if len(line) < 5:
                        continue
                    if account_type == "Savings":
                        c_balance = line[4]
                    else:
                        c_balance = line[3]
                        break

            if c_balance is None:
                self.error_label.setText("Account not found.")
                return

            new_balance = c_balance.isdigit()
            if self.deposit_button.isChecked():
                new_balance += amount
                self.error_label.setText(f"Deposited ${amount:.2f} into {account_type} account.")
                self.error_label.adjustSize()
            elif self.withdraw_button.isChecked():
                if amount <= new_balance:
                    new_balance -= amount
                    self.error_label.setText(f"Withdrew ${amount:.2f} from {account_type} account.")
                    self.error_label.adjustSize()
                else:
                    self.error_label.setText(f"Error: Insufficient funds in {account_type} account.")
                    self.error_label.adjustSize()

            with open('bank_info.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                lines = []
                for line in reader:
                    if len(line) < 5:
                        continue
                    if account_type == "Savings":
                        line[4] = str(new_balance)
                    else:
                        line[3] = str(new_balance)
                    lines.append(line)

            self.balance_label.setText(f"Current account balance: ${new_balance:.2f}")
            self.balance_label.adjustSize()

    def exit(self):
        """
        exits from logged in user
        :return:
        """
        self.clear()
        self.amount_input.clear()
        self.login_button.show()
        self.pin_input.show()
        self.label_4.show()
        self.balance_label.clear()
        self.saving_acc_button.setChecked(False)
        self.checking_acc_button.setChecked(False)
        self.deposit_button.setChecked(False)
        self.withdraw_button.setChecked(False)
        self.login_count = False

    def clear(self):
        self.error_label.clear()
        self.name_input.clear()
        self.last_label.clear()
        self.pin_input.clear()
