import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ItemNotFoundError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []


def view_menu():
    """Hiển thị thực đơn."""
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")

    for code, item in DRINK_MENU.items():
        print(
            f"[{code}] - {item['name']} - {item['price']:,} VNĐ"
        )


def add_to_order(order):
    """Thêm món vào giỏ hàng."""

    print("\n--- THÊM MÓN VÀO GIỎ ---")

    try:
        drink_code = input("Nhập mã đồ uống: ").strip().upper()

        if drink_code not in DRINK_MENU:
            raise ItemNotFoundError

        quantity = int(input("Nhập số lượng: "))

        if quantity <= 0:
            raise InvalidQuantityError

        order.append(
            {
                "code": drink_code,
                "quantity": quantity
            }
        )

        logging.info(
            f"Added {quantity} of {drink_code} to order"
        )

        print(
            f"Đã thêm {quantity} x "
            f"{DRINK_MENU[drink_code]['name']} vào giỏ hàng."
        )

    except ValueError:
        print("Vui lòng nhập số lượng là một số nguyên!")
        logging.error(
            "ValueError - Invalid quantity input"
        )

    except ItemNotFoundError:
        print(
            "Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!"
        )
        logging.warning(
            f"ItemNotFoundError - Code: {drink_code}"
        )

    except InvalidQuantityError:
        print("Số lượng phải lớn hơn 0!")
        logging.warning(
            f"InvalidQuantityError - Quantity: {quantity}"
        )


def calculate_total(order):
    """Tính tổng tiền."""

    total = 0

    for item in order:
        code = item["code"]
        quantity = item["quantity"]

        total += (
            DRINK_MENU[code]["price"] * quantity
        )

    return total


def view_order(order):
    """Hiển thị giỏ hàng."""

    if not order:
        print(
            "Giỏ hàng trống, vui lòng chọn món (Chức năng 2)."
        )
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(
        "Mã SP | Tên đồ uống | Đơn giá | Số lượng | Thành tiền"
    )
    print("-" * 65)

    for item in order:
        code = item["code"]
        quantity = item["quantity"]

        name = DRINK_MENU[code]["name"]
        price = DRINK_MENU[code]["price"]

        subtotal = price * quantity

        print(
            f"{code:<5} | "
            f"{name:<18} | "
            f"{price:>7,} | "
            f"{quantity:^8} | "
            f"{subtotal:>10,} VNĐ"
        )

    print("-" * 65)

    total = calculate_total(order)

    print(
        f"Tổng tiền cần thanh toán: {total:,} VNĐ"
    )


def checkout(order):
    """Thanh toán."""

    if not order:
        print(
            "Giỏ hàng trống, vui lòng chọn món (Chức năng 2)."
        )
        return

    total = calculate_total(order)

    print("\n--- THANH TOÁN ---")
    print(
        f"Tổng tiền cần thanh toán: {total:,} VNĐ"
    )

    confirm = input(
        f"Xác nhận thanh toán {total:,} VNĐ? (y/n): "
    ).strip().lower()

    if confirm == "y":
        print("Thanh toán thành công.")
        logging.info("Checkout successful")

        order.clear()

        print("Giỏ hàng đã được làm trống.")

    elif confirm == "n":
        print(
            "Đã hủy thao tác thanh toán. Quay lại menu chính."
        )

    else:
        print(
            "Lựa chọn không hợp lệ. Thanh toán đã bị hủy."
        )


def display_menu():
    """Hiển thị menu chính."""

    print("\n========== HIGHLANDS MINI POS ==========")
    print("1. Xem thực đơn")
    print("2. Thêm món vào giỏ")
    print("3. Xem giỏ hàng & Tính tổng tiền")
    print("4. Thanh toán & Xóa giỏ hàng")
    print("5. Thoát ca làm việc")
    print("========================================")


def main():
    """Hàm điều khiển chương trình."""

    while True:
        display_menu()

        choice = input(
            "Chọn chức năng (1-5): "
        )

        if choice == "1":
            view_menu()

        elif choice == "2":
            add_to_order(current_order)

        elif choice == "3":
            view_order(current_order)

        elif choice == "4":
            checkout(current_order)

        elif choice == "5":
            logging.info(
                "Cashier logged out. System shutdown."
            )
            print(
                "Đã thoát ca làm việc. Hẹn gặp lại!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()