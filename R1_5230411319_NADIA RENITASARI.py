# Class Pegawai
class Pegawai:
    def __init__(self, nip, nama, alamat):
        self.nip = nip
        self.nama = nama
        self.alamat = alamat

    def info(self):
        return f"NIP: {self.nip}, Nama: {self.nama}, Alamat: {self.alamat}"

# Class Produk (Parent Class)
class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk

    def info(self):
        return f"Kode Produk: {self.kode_produk}, Nama Produk: {self.nama_produk}, Jenis Produk: {self.jenis_produk}"

# Child class for Snack
class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk)  # Perbaikan di sini
        self.harga = harga

    # Method overriding
    def info(self):
        return f"Snack - {super().info()}, Harga: {self.harga}"

# Child class for Makanan
class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, porsi, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk)  # Perbaikan di sini
        self.porsi = porsi
        self.harga = harga

    # Method overriding
    def info(self):
        return f"Makanan - {super().info()}, Porsi: {self.porsi}, Harga: {self.harga}"

# Child class for Minuman
class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, volume, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk)  # Perbaikan di sini
        self.volume = volume
        self.harga = harga

    # Method overriding
    def info(self):
        return f"Minuman - {super().info()}, Volume: {self.volume}ml, Harga: {self.harga}"

# Class Transaksi
class Transaksi:
    def __init__(self, no_transaksi, pegawai, produk_list):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.produk_list = produk_list  # List of Produk objects

    def total_harga(self):
        total = sum([produk.harga for produk in self.produk_list])
        return total

    def info(self):
        produk_info = "\n".join([produk.info() for produk in self.produk_list])
        return f"No Transaksi: {self.no_transaksi}\nPegawai: {self.pegawai.info()}\nProduk:\n{produk_info}\nTotal Harga: {self.total_harga()}"

# Class Struk
class Struk:
    def __init__(self, transaksi):
        self.transaksi = transaksi

    def print_struk(self):
        print("=== STRUK PEMBELIAN ===")
        print(self.transaksi.info())
        print("=======================")

# Main menu to choose options
def main_menu():
    # Data Pegawai
    pegawai1 = Pegawai("12", "John Doe", "Merdeka")
    
    # Data Produk
    produk_list = [
        Snack("S001", "Chips", "Snack", 5000),
        Makanan("M001", "Nasi Goreng", "Makanan", "1 porsi", 15000),
        Minuman("D001", "Es Teh", "Minuman", 250, 5000)
    ]
    
    # Membuat transaksi
    transaksi1 = Transaksi("T001", pegawai1, produk_list)
    struk1 = Struk(transaksi1)
    
    while True:
        print("\n=== Menu ===")
        print("1. Tampilkan semua produk")
        print("2. Tampilkan produk berdasarkan jenis")
        print("3. Tampilkan data pegawai")
        print("4. Tampilkan struk transaksi")
        print("5. Keluar")
        
        choice = input("Pilih menu: ")
        
        if choice == '1':
            print("\nDaftar Semua Produk:")
            for produk in produk_list:
                print(produk.info())
        
        elif choice == '2':
            jenis = input("Masukkan jenis produk (Snack/Makanan/Minuman): ")
            print(f"\nDaftar Produk {jenis}:")
            for produk in produk_list:
                if produk.jenis_produk.lower() == jenis.lower():
                    print(produk.info())
        
        elif choice == '3':
            print("\nData Pegawai:")
            print(pegawai1.info())
        
        elif choice == '4':
            print("\nStruk Transaksi:")
            struk1.print_struk()
        
        elif choice == '5':
            print("Terima kasih! Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Run the main menu
main_menu()
