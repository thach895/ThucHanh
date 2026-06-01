note = ""

while True:

    print("\n===== MENU =====")
    print("1. Nhập dữ liệu đơn hàng")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ")
        continue

    if choice == 1:

        sender_name = input("Tên người gửi: ")
        sender_phone = input("SĐT người gửi: ")
        pickup_address = input("Địa chỉ lấy hàng: ")
        receiver_name = input("Tên người nhận: ")
        receiver_phone = input("SĐT người nhận: ")
        delivery_address = input("Địa chỉ giao hàng: ")
        note = input("Ghi chú giao hàng: ")

        if sender_name.strip() == "":
            print("Tên người gửi không được bỏ trống")
            continue

        if sender_phone.strip() == "":
            print("Số điện thoại người gửi không được bỏ trống")
            continue

        if pickup_address.strip() == "":
            print("Địa chỉ lấy hàng không được bỏ trống")
            continue

        if receiver_name.strip() == "":
            print("Tên người nhận không được bỏ trống")
            continue

        if receiver_phone.strip() == "":
            print("Số điện thoại người nhận không được bỏ trống")
            continue

        if delivery_address.strip() == "":
            print("Địa chỉ giao hàng không được bỏ trống")
            continue

        if note.strip() == "":
            print("Ghi chú giao hàng không được bỏ trống")
            continue

        sender_name = sender_name.strip().title()
        receiver_name = receiver_name.strip().title()

        pickup_address = pickup_address.strip()
        delivery_address = delivery_address.strip()

        note = note.strip()

        print("\n===== BÁO CÁO =====")

        print("Tên người gửi:", sender_name)
        print("Tên người nhận:", receiver_name)

        print("Địa chỉ lấy hàng:", pickup_address)
        print("Địa chỉ giao hàng:", delivery_address)

        print("Ghi chú:", note)

        print("Độ dài ghi chú:", len(note))

        print("Số lượng từ:", len(note.split()))

        print("Ghi chú chữ thường:")
        print(note.lower())

        print("Ghi chú chữ hoa:")
        print(note.upper())

    elif choice == 2:

        order_code = input("Nhập mã đơn hàng: ")

        if order_code.strip() == "":
            print("Mã đơn hàng không được bỏ trống")
            continue

        original_code = order_code

        order_code = order_code.strip()

        order_code = order_code.upper()

        order_code = order_code.replace(" ", "-")

        if not order_code.startswith("GRAB-"):
            order_code = "GRAB-" + order_code

        print("Mã đơn hàng ban đầu:")
        print(original_code)

        print("Mã đơn hàng chuẩn hóa:")
        print(order_code)

    elif choice == 3:

        sender_phone = input("Nhập SĐT người gửi: ")
        receiver_phone = input("Nhập SĐT người nhận: ")

        if not sender_phone.isdigit():
            print("Số điện thoại người gửi không hợp lệ")
            continue

        if len(sender_phone) != 10:
            print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            continue

        if not receiver_phone.isdigit():
            print("Số điện thoại người nhận không hợp lệ")
            continue

        if len(receiver_phone) != 10:
            print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
            continue

        hidden_sender = (
            sender_phone[:3]
            + "*****"
            + sender_phone[-2:]
        )

        hidden_receiver = (
            receiver_phone[:3]
            + "*****"
            + receiver_phone[-2:]
        )

        print("SĐT người gửi:", hidden_sender)
        print("SĐT người nhận:", hidden_receiver)

    elif choice == 4:

        if note == "":
            print("Chưa có ghi chú giao hàng để tìm kiếm")
            continue

        keyword = input("Nhập từ khóa cần tìm: ")
        new_keyword = input("Nhập từ khóa thay thế: ")

        count = note.count(keyword)

        if count == 0:
            print("Không tìm thấy từ khóa")
        else:

            new_note = note.replace(
                keyword,
                new_keyword
            )

            print("Số lần xuất hiện của từ khóa:", count)

            print("Ghi chú sau khi thay thế:")
            print(new_note)

    elif choice == 5:

        print("Thoát chương trình")
        break