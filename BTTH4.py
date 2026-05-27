secret_number=79;
flag=0;
for i in range(5):
    number=int(input("Nhập vào số may mắn của bạn:"));
    if(number==secret_number):
        print("Chúc mừng bạn đã đoán chính xác");
        flag=1;
        break;
    elif(number>secret_number):
        print("Số bạn nhập lớn hơn số may mắn!");
    else:
        print("Số bạn nhập nhỏ hơn số may mắn!");

if  flag==0:
    print("Bạn đã hết lượt");