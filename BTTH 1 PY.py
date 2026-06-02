cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n===== SHOPEE CART MANAGEMENT =====")
    print("1. Xem gio hang")
    print("2. Them san pham")
    print("3. Cap nhat so luong")
    print("4. Xoa san pham")
    print("5. Thoat")

    try:
        choice = int(input("Nhap lua chon: "))
    except:
        print("Lua chon khong hop le!")
        continue

    if choice == 1:
        if len(cart_items) == 0:
            print("Gio hang rong!")
            continue

        print("\n{:<8}{:<25}{:<10}{:<15}{:<15}".format(
            "Ma SP", "Ten SP", "SL", "Don gia", "Thanh tien"
        ))

        total_quantity = 0
        total_money = 0

        for item in cart_items:
            product_id = item[0]
            product_name = item[1]
            quantity = item[2]
            price = item[3]

            amount = quantity * price

            total_quantity += quantity
            total_money += amount

            print("{:<8}{:<25}{:<10}{:<15}{:<15}".format(
                product_id,
                product_name,
                quantity,
                price,
                amount
            ))

        print("\nTong so luong:", total_quantity)
        print("Tong tien:", total_money)

    elif choice == 2:
        product_id = input("Nhap ma san pham: ")
        product_name = input("Nhap ten san pham: ")

        try:
            quantity = int(input("Nhap so luong: "))
            price = int(input("Nhap don gia: "))
        except:
            print("So luong va don gia phai la so!")
            continue

        if quantity <= 0 or price < 0:
            print("So luong hoac don gia khong hop le!")
            continue

        found = False

        for item in cart_items:
            if item[0] == product_id:
                item[2] += quantity
                found = True
                print("Da cong don so luong san pham.")
                break

        if not found:
            cart_items.append([
                product_id,
                product_name,
                quantity,
                price
            ])
            print("Them san pham thanh cong!")

    elif choice == 3:
        product_id = input("Nhap ma san pham: ")

        try:
            new_quantity = int(input("Nhap so luong moi: "))
        except:
            print("So luong phai la so!")
            continue

        if new_quantity <= 0:
            print("So luong phai lon hon 0!")
            continue

        found = False

        for item in cart_items:
            if item[0] == product_id:
                item[2] = new_quantity
                found = True
                print("Cap nhat thanh cong!")
                break

        if not found:
            print("Ma san pham khong ton tai trong gio hang.")

    elif choice == 4:
        product_id = input("Nhap ma san pham can xoa: ")

        found = False

        for i in range(len(cart_items)):
            if cart_items[i][0] == product_id:
                cart_items.pop(i)
                found = True
                print("Xoa san pham thanh cong!")
                break

        if not found:
            print("Ma san pham khong ton tai trong gio hang.")

    elif choice == 5:
        print("Da thoat chuong trinh!")
        break

    else:
        print("Vui long nhap tu 1 den 5!")