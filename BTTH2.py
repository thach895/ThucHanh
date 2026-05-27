total=0;
day=0;
count=0;
for i in range(1,8):
    day_work=int(input(f"Nhập doanh thu ngày {i}: "));
    total +=day_work;
    day=day+1;
    if(day_work>=5000000):
        count +=1;
print("Tổng doanh thu tuần:", total);
print("Doanh thu trung bình:",total/day);
print("Số ngày có doanh thu trên 5000000: ",count);