"""
SECURITY LOG ANALYZER
Phân tích và xử lý log hệ thống.
"""

raw_logs = []
processed_logs = []


def clean_raw_logs():
    """
    Nhập log thô và làm sạch dữ liệu.

    - Loại bỏ ký tự ! @ # $
    - Tách log bằng dấu ;
    - Lưu vào raw_logs
    """
    global raw_logs

    print("\n--- NẠP DỮ LIỆU LOG ---")

    raw_input_log = input(
        "Nhập chuỗi log thô (cách nhau bởi dấu ;): "
    )

    translate_table = str.maketrans("", "", "!@#$")

    cleaned_text = raw_input_log.translate(
        translate_table
    )

    logs = [
        log.strip()
        for log in cleaned_text.split(";")
        if log.strip()
    ]

    raw_logs = logs

    print(
        f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống."
    )


def filter_warning_logs():
    """
    Lọc các log chứa ERROR hoặc CRITICAL.

    Sử dụng List Comprehension.
    """
    global processed_logs

    if not raw_logs:
        print(
            "\nChưa có dữ liệu log, vui lòng thực hiện chức năng 1."
        )
        return

    print("\n--- LỌC CẢNH BÁO ---")

    processed_logs = [
        log
        for log in raw_logs
        if "ERROR" in log.upper()
        or "CRITICAL" in log.upper()
    ]

    if processed_logs:
        print(
            f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:"
        )

        for log in processed_logs:
            print(f"- {log}")

    else:
        print("Không tìm thấy cảnh báo nguy hiểm.")


def mask_ip_logs():
    """
    Mã hóa IP trong processed_logs.

    Ví dụ:
    192.168.1.1 -> 192.168.*.*
    """
    if not raw_logs:
        print(
            "\nChưa có dữ liệu log, vui lòng thực hiện chức năng 1."
        )
        return

    if not processed_logs:
        print(
            "\nChưa có log cảnh báo. Hãy thực hiện chức năng 2 trước."
        )
        return

    print("\n--- MÃ HÓA IP ---")

    masked_logs = []

    for log in processed_logs:

        words = log.split()

        new_words = []

        for word in words:

            # Kiểm tra có dạng IP
            if "." in word:

                ip_parts = word.split(".")

                if len(ip_parts) == 4:

                    masked_ip = ".".join(
                        ip_parts[:2] + ["*", "*"]
                    )

                    new_words.append(masked_ip)

                else:
                    new_words.append(word)

            else:
                new_words.append(word)

        masked_logs.append(" ".join(new_words))

    print("Báo cáo log an toàn:")

    for index, log in enumerate(masked_logs, start=1):
        print(f"{index}. {log}")

    return masked_logs


def display_menu():
    """
    Hiển thị menu chương trình.
    """
    print("\n============= SECURITY LOG ANALYZER =============")
    print("1. Nhập và làm sạch dữ liệu Log thô")
    print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
    print("3. Mã hóa địa chỉ IP (Masking)")
    print("4. Đóng hệ thống")
    print("=================================================")


def main():
    """
    Hàm điều khiển chương trình.
    """
    while True:

        display_menu()

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            clean_raw_logs()

        elif choice == "2":
            filter_warning_logs()

        elif choice == "3":
            mask_ip_logs()

        elif choice == "4":
            print("\nĐóng hệ thống...")
            print("Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ.")


main()