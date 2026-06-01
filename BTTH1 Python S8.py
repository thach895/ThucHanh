while True:
    print("+=============================================+");
    print("|    Hệ Thống Quản Lý Nội Dung Tik Tok        |");
    print("+=============================================+");
    print("|   1.Nhập và phân tích thông tin video       |");
    print("|   2.Chuẩn hóa tên tài khoản                 |");
    print("|   3.Kiểm tra tính hợp lệ của hashtag        |");
    print("|   4.Tìm kiếm và thay thế từ khóa trong mô tả|");
    print("|   5.Thoát chương trình                      |");
    print("+=============================================+");
    choice=input("> Mời bạn chọn chức năng:");
    
    match (choice):
        case "1":
            account_name=input("Nhập tên tài khoản:");
            title_video=input("Nhập tiêu đề video:");
            describe_video=input("Nhập mô tả video:");
            hashtag_video=input("Nhập hashtag (cách nhau bởi dấu phẩy):");
            print("Đã qua xử lý");
            print(f"Tên tài khoản:{account_name.strip()}");
            print(f"Tên tiêu đề:{title_video.title().strip()}")
            print(f"Mô tả video:{describe_video.strip()}");
            print(f"Độ dài mô tả:{len(describe_video)}");
            count_space=1+describe_video.count(" ");
            print(f"Số lượng từ trong hashtag:{count_space}");
            new_hashtag_list=hashtag_video.split(",");
            display_hashtag="".join(new_hashtag_list);
            print(f"Danh sách hashtag:{display_hashtag}");
            count_hashtag=len(new_hashtag_list);
            print(f"Số lượng hashtag la: {count_hashtag}")
            print (f"Mo tả video đã chuyển thành thường: {describe_video. lower()}")
            print(f"Mô tả video đã chuyến thành hoa: {describe_video.upper()}")

        case "2":
            print(f"Tên tai khoản trước khi chuan hoa: {account_name}")
            print("Tên tài khoản sau khi chuẩn hóa: ", "@" + account_name. lower())
        case "3":
            hashtag = input("Nhập hashtag: ")
            if (hashtag == ""):
                print ("Không được rỗng!")
            elif (not hashtag.startswith("#")):
                print ("phải bắt đầu bằng #")
            elif (" " in hashtag):
                print ("Không được chưa khoảng trắng")
            elif (len(hashtag) < 2):
                print ("Phải chứa tối thiểu 2 kí tự")
            else:
                print(f"Danh sach hashtag moi: {hashtag_video}")
        case "4":
            find_word = input ("Nhap từ khoa cần tìm: ")
            count_word = describe_video.count(find_word)
            if (count_word > 0):
                describe_video = describe_video. replace(find_word, "Từ khóa mới")
                print(f"Mô tả sau khi thay thế: {describe_video}")
                print (f"Số lần xuất hiện từ khoa: {count_word}")
            else:
                print ("Từ khóa không tìm thấy!")
        case "5":
            break;
        case _:
            print("Lựa chọn không hợp lệ:");

