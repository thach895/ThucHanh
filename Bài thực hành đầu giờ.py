smart_parking=[];
count=1;
while True:
    print("===================================");
    print(" Quản Lý Bãi Xe - Smart Parking");
    print("===================================");
    print("1.Thêm xe mới vào bãi");
    print("2.Hiển thị danh sách xe trong bãi");
    print("3.Xóa xe khỏi bãi");
    print("4.Thoát chương trình");
    print("===================================");

    choice=input("Nhập lựa chọn của bạn:");

    match choice:
        case "1":
            while True:
                flag=1;
                type=input("Nhập loại xe:");
                if(type==""):
                    print("Loại xe không được để trống");
                    continue;
                owner=input("Nhập tên chủ xe:");
                if(owner==""):
                    print("Chủ xe không được để trống");
                    continue;
                if flag==1:
                    break;
            vehicle={
                "id":count,
                "type":type,
                "owner":owner
            }
            smart_parking.append(vehicle);
            count+=1;
        case "2":
            if len(smart_parking)==0:
                print("Bãi xe hiện đang trống");
                break;
            print("{:<5} {:<5} {:<5}".format(
                "Id","Loại xe","Chủ xe"
            ))
            for item in smart_parking:
                print("{:<5} {:<5} {:<5}".format(
                vehicle["id"],
                vehicle["type"],
                vehicle["owner"]
            ))
        case "3":
            found=input("Nhập Id xe muốn xóa:");
            
                


            

                

