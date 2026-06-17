class BankAccount:
    bank_name= "Vietcombank"
    transaction_fee= 2000

    def __init__(self,account_number,account_name):
        self.account_number = account_number
        self.account_name = account_name
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance
    @property
    def get_account_name(self):
        return self.account_name
    @get_account_name.setter
    def set_account_name(self, new_name: str):
        self.account_name = new_name.strip().upper()
    @staticmethod
    def validate_account_number(account_number: str):
        if account_number.isdigit() and len(account_number) == 10:
            return True
        else: 
            return False
    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self,amount):
        total = amount + self.transaction_fee
        if self.__balance < total :
            print("số dư không đủ")
        else:
            self.__balance -= total
    def display_info(self):
        print(f"Tên ngân hàng:{self.bank_name}")
        print(f"Số TK:{self.account_number}")
        print(f"Tên chủ TK:{self.get_account_name}")
        print(f"Số dư hiện tại{self.balance}")


def main():
    current_account = None
    while True:
        choice = int(input("""===== VIETCOMBANK DIGIBANK SIMULATOR =====
                        1. Mở tài khoản mới
                        2. Xem thông tin tài khoản
                        3. Giao dịch Nạp / Rút tiền
                        4. Cập nhật Tên chủ tài khoản
                        5. Đổi phí giao dịch hệ thống
                        6. Thoát chương trình
                        ==========================================
                        Chọn chức năng (1-6):"""))
        match choice:
            case 1:
               new_account = None
               while True: 
                   number_bank_account = input("nhập vào số TK: ")
                   account_new_name = input("nhập vào Tên TK: ")
                   if BankAccount.validate_account_number(number_bank_account):
                        new_account = BankAccount(number_bank_account, account_new_name)
                        current_account = new_account
                        print("Đã thêm tài khoản mới thành công")
                        break
                   else: 
                       print("STK không hợp lệ")
            case 2:

                if current_account is None:
                    print("Vui lòng mở tài khoản (Chức năng 1) trước")
                else: 
                    current_account.display_info()
            case 3:
                if current_account is None:
                    print("Vui lòng mở tài khoản (Chức năng 1) trước")
                else:
                    transaction_choice = int(input("""
                        1. Nạp tiền
                        2. Rút tiền
                        Chọn giao dịch: """))

                    match transaction_choice:
                        case 1:
                            amount = float(input("Nhập số tiền cần nạp: "))
                            if amount > 0:
                                current_account.deposit(amount)
                                print("Nạp tiền thành công")
                                print(f"Số dư hiện tại: {current_account.balance}")
                            else:
                                print("Số tiền nạp phải lớn hơn 0")

                        case 2:
                            amount = float(input("Nhập số tiền cần rút: "))
                            if amount > 0:
                                current_account.withdraw(amount)
                                print(f"Số dư hiện tại: {current_account.balance}")
                            else:
                                print("Số tiền rút phải lớn hơn 0")

                        case _:
                            print("Lựa chọn không hợp lệ")
            case 4:
                if current_account is None:
                    print("Vui lòng mở tài khoản trước")
                else:
                    new_name = input("Nhập tên mới: ")

                    current_account.account_holder_name = new_name

                    print("Cập nhật tên thành công")
                    print(
                        f"Tên mới: "
                        f"{current_account.account_holder_name}"
                    )
            case 5:
                print(
                    f"Phí hiện tại: "
                    f"{BankAccount.transaction_fee:,} VNĐ"
                )

                try:
                    new_fee = int(
                        input("Nhập phí mới: ")
                    )

                    if new_fee < 0:
                        print(
                            "Phí giao dịch "
                            "không được âm"
                        )
                    else:
                        BankAccount.update_transaction_fee(
                            new_fee
                        )

                        print(
                            "Cập nhật phí "
                            "thành công"
                        )

                except ValueError:
                    print("Vui lòng nhập số")

            case 6:
                print(
                    "Cảm ơn bạn đã sử dụng "
                    "Vietcombank Digibank"
                )
                break
main()