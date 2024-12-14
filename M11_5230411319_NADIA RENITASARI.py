import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Fungsi untuk memuat data dan preprocessing
def muat_dan_preprocessing(nama_file):
    try:
        # Membaca file Excel
        data = pd.read_excel(nama_file)
        print("Data berhasil dimuat!")

        # Mengisi nilai kosong pada kolom numerik dengan mean
        for kolom in data.select_dtypes(include=['number']).columns:
            data[kolom].fillna(data[kolom].mean(), inplace=True)

        # Mengisi nilai kosong pada kolom non-numerik dengan mode
        for kolom in data.select_dtypes(exclude=['number']).columns:
            data[kolom].fillna(data[kolom].mode()[0], inplace=True)

        print("Nilai kosong telah diganti dengan mean (numerik) atau mode (kategori).")

        # Asumsikan kolom terakhir adalah target, sisanya fitur
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]

        # Jika target numerik, lakukan binning menjadi kategori
        if y.dtype in ['float64', 'int64']:
            y = pd.cut(y, bins=3, labels=[0, 1, 2])  # Contoh: Membagi menjadi 3 kategori

        # Validasi data tidak kosong
        if X.empty or y.empty:
            raise ValueError("Data atau target kosong setelah preprocessing.")

        print("Preprocessing selesai. Data siap digunakan.")
        return X, y

    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan. Pastikan file berada di direktori yang benar.")
        return None, None
    except Exception as e:
        print(f"Terjadi kesalahan saat memuat data: {e}")
        return None, None

# Fungsi untuk menjalankan algoritma yang dipilih pengguna
def jalankan_algoritma(X, y, algoritma):
    try:
        # Bagi data menjadi data latih dan data uji
        X_latih, X_uji, y_latih, y_uji = train_test_split(X, y, test_size=0.2, random_state=42)

        # Pilih algoritma berdasarkan input pengguna
        if algoritma == '2':
            model = RandomForestClassifier(random_state=42)
        elif algoritma == '3':
            model = LogisticRegression(max_iter=1000, random_state=42)  # Tambahkan max_iter untuk kestabilan
        else:
            print("Pilihan algoritma tidak valid.")
            return

        # Latih model
        model.fit(X_latih, y_latih)

        # Prediksi dan hitung akurasi
        y_pred = model.predict(X_uji)
        akurasi = accuracy_score(y_uji, y_pred)
        print(f"Akurasi: {akurasi:.2f}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menjalankan algoritma: {e}")

# Loop utama untuk terminal
def main():
    X, y = None, None  # Inisialisasi variabel global
    while True:
        print("\n=== Analisis Kualitas Udara ===")
        print("1. Muat dan preprocessing data")
        print("2. Jalankan Random Forest Classifier")
        print("3. Jalankan Logistic Regression")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            nama_file = input("Masukkan nama file Excel: ")
            X, y = muat_dan_preprocessing(nama_file)
        elif pilihan in ['2', '3']:
            if X is not None and y is not None:
                jalankan_algoritma(X, y, pilihan)
            else:
                print("Silakan muat data terlebih dahulu (pilih 1).")
        elif pilihan == '4':
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program
if __name__ == "__main__":
    main()
