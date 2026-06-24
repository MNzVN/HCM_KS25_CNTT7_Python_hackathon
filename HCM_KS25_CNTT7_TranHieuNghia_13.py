class InventoryItem:
    def __init__(self, item_id, name, category, quantity, unit_price, storage_fee):
        self.id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price
        self.storage_fee = storage_fee

        self.total_inventory_value = 0
        self.inventory_type = ""

        self.calculate_inventory_value()
        self.classify_inventory()

    def calculate_inventory_value(self):
        self.total_inventory_value = (
            self.quantity * self.unit_price + self.storage_fee
        )

    def classify_inventory(self):
        if self.total_inventory_value < 5_000_000:
            self.inventory_type = "Thấp"
        elif self.total_inventory_value < 20_000_000:
            self.inventory_type = "Trung bình"
        elif self.total_inventory_value < 50_000_000:
            self.inventory_type = "Cao"
        else:
            self.inventory_type = "Rất cao"


class InventoryManager:
    def __init__(self):
        self.items = []

    def find_by_id(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def show_item_table(self, item):
        print(
            f"{item.id:<12}"
            f"{item.name:<20}"
            f"{item.category:<20}"
            f"{item.quantity:<12}"
            f"{item.unit_price:<15,.0f}"
            f"{item.storage_fee:<15,.0f}"
            f"{item.total_inventory_value:<20,.0f}"
            f"{item.inventory_type}"
        )

    def add_item(self):
        item_id = input("Nhập mã hàng hóa: ").strip()

        if item_id == "":
            print("Mã hàng hóa không được rỗng!")
            return

        if self.find_by_id(item_id):
            print("Mã hàng hóa không được trùng!")
            return

        name = input("Nhập tên hàng hóa: ").strip()
        if name == "":
            print("Tên hàng hóa không được rỗng!")
            return

        category = input("Nhập danh mục hàng hóa: ").strip()
        if category == "":
            print("Danh mục hàng hóa không được rỗng!")
            return

        quantity = input_quantity()
        unit_price = input_non_negative_float("Nhập đơn giá nhập: ")
        storage_fee = input_non_negative_float("Nhập chi phí lưu kho: ")

        item = InventoryItem(
            item_id,
            name,
            category,
            quantity,
            unit_price,
            storage_fee
        )

        self.items.append(item)

        print("Thêm hàng hóa thành công!")

    def show_all(self):
        if not self.items:
            print("Danh sách hàng hóa đang rỗng!")
            return

        print("-" * 150)
        print(
            f"{'Mã hàng hóa':<12}"
            f"{'Tên hàng hóa':<20}"
            f"{'Danh mục':<20}"
            f"{'Số lượng':<12}"
            f"{'Đơn giá nhập':<15}"
            f"{'Chi phí kho':<15}"
            f"{'Tổng giá trị':<20}"
            f"{'Phân loại'}"
        )
        print("-" * 150)

        for item in self.items:
            self.show_item_table(item)

    def update_item(self):
        item_id = input(
            "Nhập mã hàng hóa cần cập nhật: "
        ).strip()

        item = self.find_by_id(item_id)

        if item is None:
            print("Không tìm thấy hàng hóa cần cập nhật!")
            return

        quantity = input_quantity()
        unit_price = input_non_negative_float(
            "Nhập đơn giá nhập mới: "
        )
        storage_fee = input_non_negative_float(
            "Nhập chi phí lưu kho mới: "
        )

        item.quantity = quantity
        item.unit_price = unit_price
        item.storage_fee = storage_fee

        item.calculate_inventory_value()
        item.classify_inventory()

        print("Cập nhật hàng hóa thành công!")

    def delete_item(self):
        item_id = input(
            "Nhập mã hàng hóa cần xóa: "
        ).strip()

        item = self.find_by_id(item_id)

        if item is None:
            print("Không tìm thấy hàng hóa cần xóa!")
            return

        choice = input(
            "Bạn có chắc muốn xóa hàng hóa này không? (Y/N): "
        ).strip()

        if choice.lower() == "y":
            self.items.remove(item)
            print("Xóa hàng hóa thành công!")

        elif choice.lower() == "n":
            print("Đã hủy thao tác!")

        else:
            print("Lựa chọn không hợp lệ!")

    def search_item(self):
        if not self.items:
            print("Danh sách hàng hóa đang rỗng!")
            return

        keyword = input(
            "Nhập tên hoặc danh mục cần tìm: "
        ).strip().lower()

        found_items = []

        for item in self.items:
            if (
                keyword in item.name.lower()
                or keyword in item.category.lower()
            ):
                found_items.append(item)

        if not found_items:
            print("Không tìm thấy hàng hóa phù hợp!")
            return

        print("-" * 150)
        print(
            f"{'Mã hàng hóa':<12}"
            f"{'Tên hàng hóa':<20}"
            f"{'Danh mục':<20}"
            f"{'Số lượng':<12}"
            f"{'Đơn giá nhập':<15}"
            f"{'Chi phí kho':<15}"
            f"{'Tổng giá trị':<20}"
            f"{'Phân loại'}"
        )
        print("-" * 150)

        for item in found_items:
            self.show_item_table(item)


def input_quantity():
    while True:
        try:
            quantity = int(
                input("Nhập số lượng tồn kho: ")
            )

            if 0 <= quantity <= 100000:
                return quantity

            print(
                "Số lượng tồn kho phải từ 0 đến 100000!"
            )

        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")


def input_non_negative_float(message):
    while True:
        try:
            value = float(input(message))

            if value >= 0:
                return value

            print("Giá trị không được âm!")

        except ValueError:
            print("Vui lòng nhập số hợp lệ!")


def show_menu():
    print("\n================ MENU ================")
    print("1. Hiển thị danh sách hàng hóa")
    print("2. Thêm hàng hóa mới")
    print("3. Cập nhật hàng hóa")
    print("4. Xóa hàng hóa")
    print("5. Tìm kiếm hàng hóa")
    print("6. Thoát")
    print("=====================================")


def main():
    manager = InventoryManager()

    while True:
        show_menu()

        choice = input(
            "Nhập lựa chọn của bạn: "
        ).strip()

        if choice == "1":
            manager.show_all()

        elif choice == "2":
            manager.add_item()

        elif choice == "3":
            manager.update_item()

        elif choice == "4":
            manager.delete_item()

        elif choice == "5":
            manager.search_item()

        elif choice == "6":
            print(
                "Cảm ơn bạn đã sử dụng hệ thống quản lý kho hàng!"
            )
            break

        else:
            print("Lựa chọn menu không hợp lệ!")


if __name__ == "__main__":
    main()