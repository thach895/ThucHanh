i=1; total = 0; count_big_bill = 0;
while True:
    cus_bill = int(input (f"Khách hàng {i} - Nhập vào gia tri hóa đơn:"));
    count_big_bill += 1;    
    total = total + cus_bill;
    continue_chose = input("Có muốn nhập tiếp không? (C/K):");
    if (continue_chose. lower() == "k"):
        print("Thoát!");
        break;
count = i;
i = i + 1;

print(" -- Báo cáo tổng doanh thu cuối ngày Rikkei Store -- ")
print ("Tổng hóa đơn đã xử lý:", )