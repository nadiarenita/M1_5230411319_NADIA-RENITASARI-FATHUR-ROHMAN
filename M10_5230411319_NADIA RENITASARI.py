import mysql.connector

# Koneksi ke database
conn = mysql.connector.connect(
    user="root",
    host="localhost",
    password="",
    database="penjualan"
)

cur = conn.cursor()

# Membuat Tabel Pegawai
cur.execute("""
CREATE TABLE IF NOT EXISTS Pegawai (
    NIK CHAR(4) NOT NULL PRIMARY KEY,
    Nama VARCHAR(50), 
    Alamat VARCHAR(255)
)""")

# Membuat Tabel Produk
cur.execute("""
CREATE TABLE IF NOT EXISTS Produk (
    Kode_Produk CHAR(4) NOT NULL PRIMARY KEY,
    Nama_Produk VARCHAR(50), 
    Jenis_Produk VARCHAR(20),
    Harga FLOAT NOT NULL
)""")

# Membuat Tabel Transaksi
cur.execute("""
CREATE TABLE IF NOT EXISTS Transaksi (
    No_Transaksi INT AUTO_INCREMENT PRIMARY KEY,
    NIK_Pegawai CHAR(4) NOT NULL,
    Tanggal_Transaksi DATE,
    FOREIGN KEY (NIK_Pegawai) REFERENCES Pegawai(NIK)
)""")

# Membuat Tabel Detail Transaksi
cur.execute("""
CREATE TABLE IF NOT EXISTS Detail_Transaksi (
    No_Detail INT AUTO_INCREMENT PRIMARY KEY,
    No_Transaksi INT NOT NULL,
    Kode_Produk CHAR(4) NOT NULL,
    Jumlah_Produk INT,
    Total_Harga FLOAT,
    FOREIGN KEY (No_Transaksi) REFERENCES Transaksi(No_Transaksi),
    FOREIGN KEY (Kode_Produk) REFERENCES Produk(Kode_Produk)
)""")

def tambah_pegawai():
    nik = input("Masukkan NIK Pegawai (4 karakter): ")
    nama = input("Masukkan Nama Pegawai: ")
    alamat = input("Masukkan Alamat Pegawai: ")

    if len(nik) != 4:
        print("NIK harus terdiri dari 4 karakter.")
        return

    try:
        cur.execute("INSERT INTO Pegawai (NIK, Nama, Alamat) VALUES (%s, %s, %s)", (nik, nama, alamat))
        conn.commit()
        print("Pegawai berhasil ditambahkan.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

def tambah_produk():
    kode_produk = input("Masukkan Kode Produk (4 karakter): ")
    nama_produk = input("Masukkan Nama Produk: ")
    jenis_produk = input("Masukkan Jenis Produk (Snack/Makanan/Minuman): ")
    harga = input("Masukkan Harga Produk: ")

    if len(kode_produk) != 4:
        print("Kode produk harus terdiri dari 4 karakter.")
        return

    try:
        cur.execute("INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga) VALUES (%s, %s, %s, %s)", (kode_produk, nama_produk, jenis_produk, harga))
        conn.commit()
        print("Produk berhasil ditambahkan.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")

def lakukan_transaksi():
    nik_pegawai = input("Masukkan NIK Pegawai yang melakukan transaksi: ")
    try:
        cur.execute("INSERT INTO Transaksi (NIK_Pegawai, Tanggal_Transaksi) VALUES (%s, CURDATE())", (nik_pegawai,))
        conn.commit()
        no_transaksi = cur.lastrowid
        print(f"Transaksi berhasil dibuat dengan No Transaksi: {no_transaksi}")

        while True:
            print("\nDaftar Produk:")
            cur.execute("SELECT * FROM Produk")
            produk_list = cur.fetchall()
            for p in produk_list:
                print(f"{p[0]}. {p[1]} - {p[2]} - Rp{p[3]}")

            kode_produk = input("Masukkan Kode Produk (atau ketik 's' untuk selesai): ")
            if kode_produk.lower() == 's':
                break

            try:
                jumlah = int(input("Masukkan Jumlah Produk: "))
                cur.execute("SELECT Harga FROM Produk WHERE Kode_Produk = %s", (kode_produk,))
                result = cur.fetchone()
                if result:
                    harga = result[0]
                    total_harga = harga * jumlah

                    cur.execute("INSERT INTO Detail_Transaksi (No_Transaksi, Kode_Produk, Jumlah_Produk, Total_Harga) VALUES (%s, %s, %s, %s)",
                                (no_transaksi, kode_produk, jumlah, total_harga))
                    conn.commit()

                    print(f"Produk {kode_produk} sebanyak {jumlah} berhasil ditambahkan ke transaksi.")
                else:
                    print("Produk tidak ditemukan.")
            except ValueError:
                print("Input jumlah tidak valid.")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

def cetak_struk():
    no_transaksi = input("Masukkan No Transaksi yang ingin dicetak: ")
    try:
        cur.execute("""
        SELECT t.No_Transaksi, t.Tanggal_Transaksi, p.Nama, d.Jumlah_Produk, pr.Nama_Produk, pr.Jenis_Produk, d.Total_Harga
        FROM Transaksi t
        JOIN Detail_Transaksi d ON t.No_Transaksi = d.No_Transaksi
        JOIN Pegawai p ON t.NIK_Pegawai = p.NIK
        JOIN Produk pr ON d.Kode_Produk = pr.Kode_Produk
        WHERE t.No_Transaksi = %s
        """, (no_transaksi,))

        transaksi = cur.fetchall()
        if not transaksi:
            print("Transaksi tidak ditemukan.")
            return

        print("\n--- Struk Transaksi ---")
        print(f"No Transaksi: {transaksi[0][0]}")
        print(f"Tanggal: {transaksi[0][1]}")
        print(f"Pegawai: {transaksi[0][2]}")
        print("Produk yang dibeli:")
        for t in transaksi:
            print(f"- {t[4]} ({t[5]}), Jumlah: {t[3]}, Total Harga: Rp{t[6]}")
        print("------------------------")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

# Main menu loop
while True:
    print("\nMenu:")
    print("1. Tambah Pegawai")
    print("2. Tambah Produk")
    print("3. Lakukan Transaksi")
    print("4. Cetak Struk")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pegawai()
    elif pilihan == "2":
        tambah_produk()
    elif pilihan == "3":
        lakukan_transaksi()
    elif pilihan == "4":
        cetak_struk()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Menutup koneksi
cur.close()
conn.close()
