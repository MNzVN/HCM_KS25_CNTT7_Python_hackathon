class InventoryItem:
    def __init__(self, id, name, category, quantity, unit_price, storage_fee):
        self.id = id
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

    def find_by_id(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None

    # Thêm hàng hóa
    def add_item(self):
        try:
            id = input("Nhập mã hàng hóa: ").strip()

            if id == "":
                print("Mã hàng hóa không được để trống!")
                return

            if self.find_by_id(id):
                print("Mã hàng hóa đã tồn tại!")
                return

            name = input("Nhập tên hàng hóa: ").strip()
            if name == "":
                print("Tên hàng hóa không được để trống!")
                return

            category = input("Nhập danh mục: ").strip()
            if category == "":
                print("Danh mục không được để trống!")
                return

            quantity = int(input("Nhập số lượng tồn kho: "))
            if quantity < 0 or quantity > 1000:
                print("Số lượng phải từ 0 đến 1000!")
                return

            unit_price = float(input("Nhập đơn giá nhập: "))
            if unit_price <= 0:
                print("Đơn giá phải lớn hơn 0!")
                return

            storage_fee = float(input("Nhập chi phí lưu kho: "))
            if storage_fee <= 0:
                print("Chi phí lưu kho phải lớn hơn 0!")
                return

            item = InventoryItem(
                id,
                name,
                category,
                quantity,
                unit_price,
                storage_fee
            )

            self.items.append(item)
            print("Thêm hàng hóa thành công!")

        except ValueError:
            print("Dữ liệu nhập không hợp lệ!")

    # Hiển thị danh sách
    def show_all(self):
        if len(self.items) == 0:
            print("Danh sách hàng hóa đang rỗng!")
            return

        print("-" * 150)
        print(
            f"{'Mã HH':<10}"
            f"{'Tên hàng hóa':<20}"
            f"{'Danh mục':<15}"
            f"{'Số lượng':<12}"
            f"{'Đơn giá':<15}"
            f"{'Chi phí kho':<15}"
            f"{'Tổng giá trị':<20}"
            f"{'Phân loại'}"
        )
        print("-" * 150)

        for p in self.items:
            print(
                f"{p.id:<10}"
                f"{p.name:<20}"
                f"{p.category:<15}"
                f"{p.quantity:<12}"
                f"{p.unit_price:<15,.0f}"
                f"{p.storage_fee:<15,.0f}"
                f"{p.total_inventory_value:<20,.0f}"
                f"{p.inventory_type}"
            )

    # Cập nhật
    def update_item(self):
        id = input("Nhập mã hàng hóa cần cập nhật: ").strip()

        item = self.find_by_id(id)

        if item is None:
            print("Không tìm thấy hàng hóa!")
            return

        try:
            quantity = int(input("Nhập số lượng mới: "))
            if quantity < 0 or quantity > 1000:
                print("Số lượng phải từ 0 đến 1000!")
                return

            unit_price = float(input("Nhập đơn giá mới: "))
            if unit_price <= 0:
                print("Đơn giá phải lớn hơn 0!")
                return

            storage_fee = float(input("Nhập chi phí lưu kho mới: "))
            if storage_fee <= 0:
                print("Chi phí lưu kho phải lớn hơn 0!")
                return

            item.quantity = quantity
            item.unit_price = unit_price
            item.storage_fee = storage_fee

            item.calculate_inventory_value()
            item.classify_inventory()

            print("Cập nhật thành công!")

        except ValueError:
            print("Dữ liệu nhập không hợp lệ!")

    # Xóa
    def delete_item(self):
        id = input("Nhập mã hàng hóa cần xóa: ").strip()

        item = self.find_by_id(id)

        if item is None:
            print("Không tìm thấy hàng hóa!")
            return

        choice = input("Bạn có chắc muốn xóa? (Y/N): ")

        if choice.lower() == "y":
            self.items.remove(item)
            print("Xóa thành công!")
        else:
            print("Đã hủy thao tác!")

    # Tìm kiếm
    def search_item(self):
        keyword = input("Nhập tên hàng hóa cần tìm: ").lower()

        found = False

        for item in self.items:
            if keyword in item.name.lower():
                found = True

                print("-" * 80)
                print("Mã hàng hóa:", item.id)
                print("Tên hàng hóa:", item.name)
                print("Danh mục:", item.category)
                print("Số lượng:", item.quantity)
                print("Đơn giá:", format(item.unit_price, ",.0f"))
                print("Chi phí kho:", format(item.storage_fee, ",.0f"))
                print(
                    "Tổng giá trị:",
                    format(item.total_inventory_value, ",.0f")
                )
                print("Phân loại:", item.inventory_type)

        if not found:
            print("Không tìm thấy hàng hóa!")


# MAIN
manager = InventoryManager()

while True:
    print("\n============= MENU =============")
    print("1. Hiển thị danh sách hàng hóa")
    print("2. Thêm hàng hóa mới")
    print("3. Cập nhật hàng hóa")
    print("4. Xóa hàng hóa")
    print("5. Tìm kiếm hàng hóa")
    print("6. Thoát")
    print("================================")

    try:
        choice = int(input("Nhập lựa chọn: "))

        match choice:
            case 1:
                manager.show_all()
            case 2:
                manager.add_item()
            case 3:
                manager.update_item()
            case 4:
                manager.delete_item()
            case 5:
                manager.search_item()
            case 6:
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

    except ValueError:
        print("Vui lòng nhập số từ 1 đến 6!")