total_bill = int(input("Nhap tong so lượng hóa đơn:"));
max_bill = 0;
for i in range(1, total_bill + 1):
    bill_value = int(input (f"Nhập vào hóa đơn īthứ {i}:"));
    if(i==1):
        min_bill=bill_value;
    if (bill_value > max_bill) :
        max_bill = bill_value
    if(bill_value<min_bill):
        min_bill=bill_value;
print("Hóa đơn có giá trị lớn nhất là:", max_bill);
print("Hóa đơn có giá trị nhỏ nhất là:",min_bill);