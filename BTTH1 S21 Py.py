import logging
import re

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def deposit(balance):
    print("\n--- NẠP TIỀN VÀO VÍ ---")

    while True:
        try:
            amount = int(input("Nhập số tiền cần nạp: "))

            if amount <= 0:
                print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                logging.error(
                    f"InvalidAmountError: Attempted to process {amount} VND."
                )
                return balance

            balance += amount

            logging.info(
                f"Deposit successful: +{amount} VND. Current Balance: {balance}"
            )

            print(f"\nNạp tiền thành công: +{amount:,} VND")
            print(f"Số dư hiện tại: {balance:,} VND")

            return balance

        except ValueError:
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
            logging.error(
                "ValueError: Invalid numeric input for deposit."
            )


def transfer(balance):
    print("\n--- CHUYỂN TIỀN ---")

    phone = input("Nhập số điện thoại người nhận: ")

    if not re.fullmatch(r"\d{10}", phone):
        print("Lỗi: Số điện thoại phải gồm đúng 10 chữ số.")
        return balance

    try:
        amount = int(input("Nhập số tiền cần chuyển: "))

        if amount <= 0:
            print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
            logging.error(
                f"InvalidAmountError: Attempted to process {amount} VND."
            )
            return balance

        if amount > balance:
            print("\nGiao dịch thất bại: Số dư của bạn không đủ.")
            print(f"Số dư hiện tại: {balance:,} VND")

            logging.error(
                f"InsufficientBalanceError: Attempted to transfer {amount} VND with balance {balance} VND."
            )
            return balance

        if amount >= 10000000:
            logging.warning(
                f"High value transaction detected: {amount} VND to {phone}"
            )

        balance -= amount

        logging.info(
            f"Transfer successful: -{amount} VND to {phone}. Current Balance: {balance}"
        )

        print(f"\nChuyển tiền thành công tới số điện thoại {phone}.")
        print(f"Số tiền đã chuyển: {amount:,} VND")
        print(f"Số dư còn lại: {balance:,} VND")

        return balance

    except ValueError:
        print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
        logging.error(
            "ValueError: Invalid numeric input for transfer."
        )
        return balance


def show_balance(balance):
    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {balance:,} VND")

    logging.info(
        f"Balance checked. Current Balance: {balance}"
    )


def show_transaction_history():
    print("\n--- LỊCH SỬ GIAO DỊCH ---")

    try:
        with open("momo_transactions.log", "r", encoding="utf-8") as file:
            content = file.read()

            if content.strip() == "":
                print("Chưa có lịch sử giao dịch nào trong hệ thống.")
            else:
                print(content)

    except FileNotFoundError:
        print("Chưa có lịch sử giao dịch nào trong hệ thống.")


def display_menu():
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Xem lịch sử giao dịch")
    print("5. Thoát chương trình")
    print("=====================================")


def main():
    balance = 0

    while True:
        display_menu()

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            balance = deposit(balance)

        elif choice == "2":
            balance = transfer(balance)

        elif choice == "3":
            show_balance(balance)

        elif choice == "4":
            show_transaction_history()

        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng dịch vụ.")
            logging.info("System shutdown")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()