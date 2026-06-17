class NetflixAccount:
    """
    Netflix Account Manager
    """

    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    # ==========================
    # Property: Password
    # ==========================

    @property
    def password(self):
        """
        Không trả về mật khẩu thật.
        """
        return "********"

    @password.setter
    def password(self, new_password):
        """
        Kiểm tra độ dài mật khẩu.
        """
        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password

    # ==========================
    # Property: Plan (Read Only)
    # ==========================

    @property
    def plan(self):
        """
        Chỉ cho phép đọc.
        """
        return self.__plan

    # ==========================
    # Static Method
    # ==========================

    @staticmethod
    def validate_email(email):
        """
        Kiểm tra email hợp lệ.
        """
        return "@" in email and "." in email

    # ==========================
    # Class Method
    # ==========================

    @classmethod
    def update_max_profiles(cls, new_limit):
        """
        Cập nhật giới hạn profile toàn hệ thống.
        """
        cls.max_profiles = new_limit

    # ==========================
    # Instance Methods
    # ==========================

    def add_profile(self, profile_name):
        """
        Thêm profile nếu chưa vượt giới hạn.
        """
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
            return

        self.profiles.append(profile_name)
        print("Thêm Profile thành công!")

    def upgrade_plan(self, new_plan):
        """
        Nâng cấp gói cước.
        """

        valid_plans = ["Basic", "Standard", "Premium"]

        if new_plan not in valid_plans:
            print("Gói cước không hợp lệ!")
            return

        self.__plan = new_plan
        print(f"Đã nâng cấp lên gói {new_plan}")

    def display_info(self):
        """
        Hiển thị thông tin tài khoản.
        """

        print("\n===== ACCOUNT INFORMATION =====")
        print(f"Platform : {NetflixAccount.platform_name}")
        print(f"Email    : {self.email}")
        print(f"Password : {self.password}")
        print(f"Plan     : {self.plan}")

        if self.profiles:
            print("Profiles :")
            for index, profile in enumerate(self.profiles, start=1):
                print(f"  {index}. {profile}")
        else:
            print("Profiles : None")

        print("=" * 32)


def main():
    current_account = None

    while True:
        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Đăng ký tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Thêm người xem")
        print("4. Nâng cấp gói cước")
        print("5. Cập nhật chính sách Netflix")
        print("6. Thoát chương trình")
        print("===================================")

        try:
            choice = int(input("Chọn chức năng (1-6): "))
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 6")
            continue

        match choice:

            # ======================
            # Register Account
            # ======================

            case 1:
                print("\n--- REGISTER ACCOUNT ---")

                email = input("Nhập email: ")

                if not NetflixAccount.validate_email(email):
                    print(
                        "Email không hợp lệ, vui lòng chứa ký tự '@' và '.'"
                    )
                    continue

                account = NetflixAccount(email)

                while True:
                    try:
                        password = input("Nhập mật khẩu: ")
                        account.password = password
                        break

                    except ValueError as e:
                        print(e)

                current_account = account

                print("Đăng ký tài khoản thành công!")

            # ======================
            # View Account
            # ======================

            case 2:

                if current_account is None:
                    print(
                        "Vui lòng đăng ký tài khoản trước (Chức năng 1)"
                    )
                    continue

                current_account.display_info()

            # ======================
            # Add Profile
            # ======================

            case 3:

                if current_account is None:
                    print(
                        "Vui lòng đăng ký tài khoản trước (Chức năng 1)"
                    )
                    continue

                profile_name = input(
                    "Nhập tên Profile mới: "
                ).strip()

                current_account.add_profile(profile_name)

            # ======================
            # Upgrade Plan
            # ======================

            case 4:

                if current_account is None:
                    print(
                        "Vui lòng đăng ký tài khoản trước (Chức năng 1)"
                    )
                    continue

                print("\nAvailable Plans:")
                print("1. Basic")
                print("2. Standard")
                print("3. Premium")

                plan = input(
                    "Nhập tên gói muốn nâng cấp: "
                ).strip()

                current_account.upgrade_plan(plan)

            # ======================
            # Update Policy
            # ======================

            case 5:

                try:
                    new_limit = int(
                        input(
                            "Nhập giới hạn Profile mới: "
                        )
                    )

                    if new_limit <= 0:
                        print(
                            "Giới hạn phải lớn hơn 0"
                        )
                        continue

                    NetflixAccount.update_max_profiles(
                        new_limit
                    )

                    print(
                        f"Đã cập nhật giới hạn Profile "
                        f"toàn hệ thống thành {new_limit}"
                    )

                except ValueError:
                    print(
                        "Vui lòng nhập số nguyên hợp lệ"
                    )

            # ======================
            # Exit
            # ======================

            case 6:
                print(
                    "Cảm ơn bạn đã sử dụng Netflix Account Manager!"
                )
                break

            case _:
                print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()