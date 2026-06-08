inventory_stock = 100
total_revenue = 0.0


def add_stock(amount):
    global inventory_stock
    inventory_stock += amount


def process_sale(quantity):
    global inventory_stock

    if quantity > inventory_stock:
        print(
            f"Lỗi: Không đủ hàng trong kho. "
            f"Tồn kho hiện tại chỉ còn {inventory_stock}."
        )
        return False

    return True


def calculate_final_price(quantity, price):
    subtotal = quantity * price
    discount = 0

    if subtotal >= 1000:
        discount = subtotal * 0.1

    after_discount = subtotal - discount
    vat = after_discount * 0.08
    final_total = after_discount + vat

    return subtotal, discount, vat, final_total


def complete_sale(quantity, final_total):
    global inventory_stock
    global total_revenue

    inventory_stock -= quantity
    total_revenue += final_total


def print_report():
    global inventory_stock
    global total_revenue

    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")


def input_positive_number(message):
    try:
        value = float(input(message))

        if value <= 0:
            print("Dữ liệu nhập vào phải lớn hơn 0.")
            return None

        return value

    except ValueError:
        print("Dữ liệu nhập vào không hợp lệ.")
        return None


while True:
    print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
    print("1. Nhập thêm hàng vào kho")
    print("2. Bán hàng (Tính toán hóa đơn)")
    print("3. Xem báo cáo tổng quan")
    print("4. Thoát chương trình")
    print("=================================================")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        print("\n--- NHẬP HÀNG ---")

        amount = input_positive_number(
            "Nhập số lượng sản phẩm muốn thêm: "
        )

        if amount is not None:
            amount = int(amount)
            add_stock(amount)

            print(f"Đã nhập thành công {amount} sản phẩm.")
            print(f"Tồn kho hiện tại: {inventory_stock}")

    elif choice == "2":
        print("\n--- BÁN HÀNG ---")

        quantity = input_positive_number(
            "Nhập số lượng mua: "
        )

        if quantity is None:
            continue

        price = input_positive_number(
            "Nhập đơn giá ($): "
        )

        if price is None:
            continue

        quantity = int(quantity)

        if not process_sale(quantity):
            continue

        subtotal, discount, vat, final_total = calculate_final_price(
            quantity, price
        )

        complete_sale(quantity, final_total)

        print("\n-> Hóa đơn chi tiết:")
        print(f"Số lượng: {quantity} | Đơn giá: ${price}")
        print(f"Tạm tính: ${subtotal}")
        print(f"Giảm giá (10%): ${discount}")
        print(f"Thuế VAT (8%): ${vat}")
        print(f"Tổng thanh toán: ${final_total}")
        print("Đã bán thành công!")

    elif choice == "3":
        print_report()

    elif choice == "4":
        print("Đang lưu dữ liệu...")
        print("Thoát chương trình thành công!")
        break

    else:
        print("Vui lòng chọn từ 1 đến 4.")