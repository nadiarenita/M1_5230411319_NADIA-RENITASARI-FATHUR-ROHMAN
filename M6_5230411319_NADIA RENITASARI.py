class Delivery:
    def __init__(self, id, name, information, date, address):
        self._id = id
        self.name = name
        self.information = information
        self.date = date
        self.address = address

    def process_delivery(self):
        print(f"🟢 Processing delivery ID {self._id} for {self.name} on {self.date} to {self.address}\n")


class Order:
    def __init__(self, ID, name, details):
        self._ID = ID
        self.name = name
        self.details = details
        self.deliveries = []

    def set_order(self, delivery):
        # Memastikan yang ditambahkan adalah instance dari kelas Delivery
        if isinstance(delivery, Delivery):
            self.deliveries.append(delivery)
        else:
            print("❌ Objek yang dimasukkan bukan merupakan pengiriman yang valid.")

    def get_order_details(self):
        print(f"\n📦 Order Details 📦")
        print(f"Order ID   : {self._ID}")
        print(f"Order Name : {self.name}")
        print(f"Details    : {self.details}")
        print("Deliveries:")
        if self.deliveries:  # Cek jika ada delivery
            for delivery in self.deliveries:
                print(f" - Delivery ID: {delivery._id}, Date: {delivery.date}, Address: {delivery.address}")
        else:
            print(" - No deliveries yet.")
        print("\n" + "-" * 40)


# Menu Interaktif
def main_menu():
    orders = {}
    while True:
        print("\n" + "=" * 40)
        print("🛒 Welcome to Order Management System 🛒")
        print("=" * 40)
        print("1️⃣ Tambah Order")
        print("2️⃣ Tambah Delivery ke Order")
        print("3️⃣ Lihat Detail Order")
        print("4️⃣ Proses Semua Delivery dalam Order")
        print("5️⃣ Keluar")
        print("=" * 40)

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            print("\n🔹 Tambah Order Baru 🔹")
            try:
                order_id = int(input("Masukkan ID Order       : "))
                if order_id in orders:
                    print("❌ Order dengan ID tersebut sudah ada.")
                    continue
                name = input("Masukkan Nama Order     : ")
                details = input("Masukkan Detail Order   : ")
                orders[order_id] = Order(order_id, name, details)
                print("✅ Order berhasil ditambahkan.\n")
            except ValueError:
                print("❌ ID Order harus berupa angka.")

        elif pilihan == "2":
            print("\n🔹 Tambah Delivery ke Order 🔹")
            try:
                order_id = int(input("Masukkan ID Order       : "))
                if order_id in orders:
                    delivery_id = int(input("Masukkan ID Delivery    : "))
                    name = input("Masukkan Nama Penerima  : ")
                    information = input("Masukkan Informasi      : ")
                    date = input("Masukkan Tanggal        : ")
                    address = input("Masukkan Alamat         : ")
                    delivery = Delivery(delivery_id, name, information, date, address)
                    orders[order_id].set_order(delivery)
                    print("✅ Delivery berhasil ditambahkan ke Order.\n")
                else:
                    print("❌ Order dengan ID tersebut tidak ditemukan.\n")
            except ValueError:
                print("❌ ID harus berupa angka.")

        elif pilihan == "3":
            print("\n🔹 Lihat Detail Order 🔹")
            try:
                order_id = int(input("Masukkan ID Order       : "))
                if order_id in orders:
                    orders[order_id].get_order_details()
                else:
                    print("❌ Order dengan ID tersebut tidak ditemukan.\n")
            except ValueError:
                print("❌ ID harus berupa angka.")

        elif pilihan == "4":
            print("\n🔹 Proses Semua Delivery dalam Order 🔹")
            try:
                order_id = int(input("Masukkan ID Order       : "))
                if order_id in orders:
                    if orders[order_id].deliveries:
                        for delivery in orders[order_id].deliveries:
                            delivery.process_delivery()
                    else:
                        print("❌ Tidak ada delivery yang terdaftar untuk Order ini.\n")
                else:
                    print("❌ Order dengan ID tersebut tidak ditemukan.\n")
            except ValueError:
                print("❌ ID harus berupa angka.")

        elif pilihan == "5":
            print("👋 Terima kasih telah menggunakan sistem ini. Keluar dari program.")
            break
        else:
            print("❗ Opsi tidak valid. Silakan pilih lagi.\n")


# Memulai program
main_menu()