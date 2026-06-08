available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0
MAX_SEATS = 50


def calculate_ticket_price(quantity, ticket_class):
    if ticket_class == 1:
        price = BASE_PRICE
    else:
        price = BASE_PRICE * 1.5

    subtotal = quantity * price
    service_fee = subtotal * 0.05
    total = subtotal + service_fee

    return subtotal, service_fee, total


def book_tickets(quantity, total_amount):
    global available_seats
    global flight_revenue

    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return False

    available_seats -= quantity
    flight_revenue += total_amount
    return True


def cancel_tickets(quantity):
    global available_seats
    global flight_revenue

    if available_seats + quantity > MAX_SEATS:
        return None

    refund_amount = quantity * BASE_PRICE * 0.8

    available_seats += quantity
    flight_revenue -= refund_amount

    return refund_amount


def flight_status():
    """
    Hiển thị báo cáo tình trạng chuyến bay VN2026,
    bao gồm sức chứa tối đa, số ghế đã đặt,
    số ghế còn trống và tổng doanh thu hiện tại.
    """
    booked_seats = MAX_SEATS - available_seats

    print("\n--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_SEATS}")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")


while True:
    print("\n============= SKYBOOKING SYSTEM =============")
    print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
    print("1. Đặt vé máy bay")
    print("2. Hủy vé & Hoàn tiền")
    print("3. Xem tình trạng chuyến bay")
    print("4. Đóng hệ thống")
    print("=============================================")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        print("\n--- ĐẶT VÉ MÁY BAY ---")

        try:
            quantity = int(input("Nhập số lượng vé: "))

            if quantity <= 0:
                print("Số lượng vé phải lớn hơn 0.")
                continue

            ticket_class = int(
                input("Chọn hạng vé (1: Economy, 2: Business): ")
            )

            if ticket_class not in [1, 2]:
                print("Hạng vé không hợp lệ.")
                continue

            subtotal, service_fee, total = calculate_ticket_price(
                quantity,
                ticket_class
            )

            if book_tickets(quantity, total):
                ticket_name = (
                    "Economy"
                    if ticket_class == 1
                    else "Business"
                )

                print("-> Xác nhận đặt chỗ:")
                print(
                    f"Số lượng: {quantity} | Hạng: {ticket_name}"
                )
                print(f"Tạm tính: ${subtotal}")
                print(f"Phí dịch vụ (5%): ${service_fee}")
                print(f"Tổng thanh toán: ${total}")
                print(
                    f"Đặt vé thành công! Ghế trống còn lại: {available_seats}"
                )

        except ValueError:
            print("Dữ liệu nhập không hợp lệ.")

    elif choice == "2":
        print("\n--- HỦY VÉ & HOÀN TIỀN ---")

        try:
            quantity = int(input("Nhập số lượng vé muốn hủy: "))

            if quantity <= 0:
                print("Số lượng vé phải lớn hơn 0.")
                continue

            refund = cancel_tickets(quantity)

            if refund is None:
                print(
                    "Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra."
                )
            else:
                print(
                    f"Hủy vé thành công. Hệ thống đã hoàn lại: "
                    f"${refund} (80% giá cơ bản)."
                )
                print(
                    f"Ghế trống hiện tại: {available_seats}"
                )

        except ValueError:
            print("Dữ liệu nhập không hợp lệ.")

    elif choice == "3":
        flight_status()

    elif choice == "4":
        print("Kết thúc phiên làm việc!")
        break

    else:
        print("Vui lòng chọn từ 1 đến 4.")