description = ""
discount_codes = []

while True:

    print("\n===== MENU =====")
    print("1. Nhập dữ liệu sản phẩm")
    print("2. Chuẩn hóa tên shop")
    print("3. Kiểm tra mã giảm giá")
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

        shop_name = input("Nhập tên shop: ")

        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        product_name = input("Nhập tên sản phẩm: ")

        description = input("Nhập mô tả sản phẩm: ")

        if description.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        category = input("Nhập danh mục sản phẩm: ")

        keywords = input("Nhập danh sách từ khóa: ")

        shop_name = shop_name.strip()

        product_name = product_name.strip().title()

        description = description.strip()

        category = category.strip().lower()

        keyword_list = keywords.split(",")

        for i in range(len(keyword_list)):
            keyword_list[i] = keyword_list[i].strip()

        print("\n===== BÁO CÁO =====")

        print("Tên shop:", shop_name)

        print("Tên sản phẩm:", product_name)

        print("Mô tả:", description)

        print("Độ dài mô tả:", len(description))

        print("Danh mục:", category)

        print("Danh sách từ khóa:", keyword_list)

        print("Số lượng từ khóa:", len(keyword_list))

        print("Mô tả chữ thường:")
        print(description.lower())

        print("Mô tả chữ hoa:")
        print(description.upper())

    elif choice == 2:

        shop_name = input("Nhập tên shop: ")

        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        original = shop_name

        shop_name = shop_name.strip()

        shop_name = shop_name.lower()

        shop_name = shop_name.replace(" ", "-")

        if not shop_name.startswith("shop-"):
            shop_name = "shop-" + shop_name

        print("Tên shop ban đầu:")
        print(original)

        print("Tên shop chuẩn hóa:")
        print(shop_name)

    elif choice == 3:

        code = input("Nhập mã giảm giá: ")

        if code == "":
            print("Mã giảm giá không được rỗng")

        elif " " in code:
            print("Mã giảm giá không được chứa khoảng trắng")

        elif len(code) < 6 or len(code) > 12:
            print("Độ dài phải từ 6 đến 12 ký tự")

        elif not code.isupper():
            print("Mã giảm giá phải viết hoa toàn bộ")

        elif not code.isalnum():
            print("Mã giảm giá chỉ được chứa chữ và số")

        elif not code.startswith("SALE"):
            print("Mã giảm giá phải bắt đầu bằng SALE")

        else:
            print("Mã giảm giá hợp lệ")

            discount_codes.append(code)

            print("Danh sách mã giảm giá hiện tại:")
            print(discount_codes)

    elif choice == 4:

        if description == "":
            print("Chưa có mô tả sản phẩm")
            continue

        keyword = input("Nhập từ khóa cần tìm: ")

        new_keyword = input("Nhập từ khóa thay thế: ")

        count = description.count(keyword)

        if count == 0:
            print("Không tìm thấy từ khóa")
        else:
            new_description = description.replace(
                keyword,
                new_keyword
            )

            print("Số lần xuất hiện:", count)

            print("Mô tả sau khi thay thế:")
            print(new_description)

    elif choice == 5:
        print("Thoát chương trình")
        break