cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]

while True:
    print("\n===== SHOPEE CART MANAGEMENT =====")
    print("1. Xem giỏ hàng")
    print("2. Thêm sản phẩm / Tăng số lượng")
    print("3. Cập nhật số lượng")
    print("4. Xóa sản phẩm")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ")

    match choice:
        case "1":
            total_number = 0
            total_money = 0

            print("\nDanh sách sản phẩm:")
            print("-" * 80)

            for item in cart_items:
                amount = item["number"] * item["price"]

                print(
                    f"{item['id']} | "
                    f"{item['name']} | "
                    f"SL: {item['number']} | "
                    f"Đơn giá: {item['price']} | "
                    f"Thành tiền: {amount}"
                )

                total_number += item["number"]
                total_money += amount

            print("-" * 80)
            print(f"Tổng số lượng: {total_number}")
            print(f"Tổng tiền: {total_money}")

        case "2":
            product_id = input("Nhập mã sản phẩm: ")
            product_name = input("Nhập tên sản phẩm: ")

            try:
                number = int(input("Nhập số lượng: "))
                price = int(input("Nhập đơn giá: "))
            except ValueError:
                print("Số lượng và đơn giá phải là số!")
                continue

            if number <= 0 or price < 0:
                print("Dữ liệu không hợp lệ!")
                continue

            found = False

            for item in cart_items:
                if item["id"] == product_id:
                    item["number"] += number
                    found = True
                    print("Đã cộng dồn số lượng.")
                    break

            if not found:
                cart_items.append(
                    {
                        "id": product_id,
                        "name": product_name,
                        "number": number,
                        "price": price
                    }
                )
                print("Đã thêm sản phẩm mới.")

        case "3":
            product_id = input("Nhập mã sản phẩm: ")

            try:
                new_number = int(input("Nhập số lượng mới: "))
            except ValueError:
                print("Số lượng phải là số!")
                continue

            if new_number <= 0:
                print("Số lượng không hợp lệ!")
                continue

            found = False

            for item in cart_items:
                if item["id"] == product_id:
                    item["number"] = new_number
                    found = True
                    print("Cập nhật thành công.")
                    break

            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        case "4":
            product_id = input("Nhập mã sản phẩm cần xóa: ")

            found = False

            for i in range(len(cart_items)):
                if cart_items[i]["id"] == product_id:
                    del cart_items[i]
                    found = True
                    print("Xóa thành công.")
                    break

            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        case "5":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ 1 đến 5.")