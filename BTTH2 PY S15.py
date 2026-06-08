atm_vault_balance = 50000000
user_account_balance = 10000000


def display_balances():
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    global user_account_balance
    global atm_vault_balance

    user_account_balance += amount
    atm_vault_balance += amount

    return True


def check_withdrawal_rules(amount):
    fee = 1100
    total_deduction = amount + fee

    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"

    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"

    return "OK"


def execute_withdrawal(total_deduction, amount_to_dispense):
    global user_account_balance
    global atm_vault_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense


while True:
    print("\n============= SMART ATM =============")
    print("1. Xem số dư")
    print("2. Nạp tiền")
    print("3. Rút tiền")
    print("4. Kết thúc giao dịch")
    print("=====================================")

    choice = input("Vui lòng chọn giao dịch (1-4): ")

    if choice == "1":
        display_balances()

    elif choice == "2":
        print("\n--- NẠP TIỀN ---")

        try:
            amount = int(input("Nhập số tiền muốn nạp: "))

            if amount <= 0:
                print("Số tiền không hợp lệ")
                continue

            if deposit_money(amount):
                print(
                    f"Giao dịch thành công! "
                    f"Số dư tài khoản hiện tại: {user_account_balance:,} VND."
                )

        except ValueError:
            print("Dữ liệu không hợp lệ")

    elif choice == "3":
        print("\n--- RÚT TIỀN ---")

        try:
            amount = int(input("Nhập số tiền cần rút: "))

            if amount <= 0:
                print("Số tiền không hợp lệ")
                continue

            if amount % 50000 != 0:
                print("Số tiền rút phải là bội số của 50,000")
                continue

            result = check_withdrawal_rules(amount)

            if result == "INSUFFICIENT_FUNDS":
                print("Giao dịch thất bại: Số dư tài khoản không đủ.")

            elif result == "ATM_OUT_OF_CASH":
                print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")

            else:
                fee = 1100
                total_deduction = amount + fee

                execute_withdrawal(total_deduction, amount)

                print("Giao dịch đang xử lý...")
                print(f"Phí giao dịch: {fee:,} VND")
                print(f"Bạn đã rút thành công {amount:,} VND.")
                print(
                    f"Số dư tài khoản còn lại: "
                    f"{user_account_balance:,} VND."
                )

        except ValueError:
            print("Dữ liệu không hợp lệ")

    elif choice == "4":
        print("Cảm ơn quý khách đã sử dụng dịch vụ!")
        break

    else:
        print("Lựa chọn không hợp lệ")