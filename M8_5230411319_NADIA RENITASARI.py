import tkinter as tk  # Untuk GUI
from tkinter import messagebox  # Untuk popup pesan
import csv  # Untuk menyimpan data ke file CSV
import os  # Untuk memeriksa apakah file CSV ada
import matplotlib.pyplot as plt  # Untuk visualisasi data

# List untuk menyimpan rating dan komentar
ratings = []  # Menyimpan angka rating
comments = []  # Menyimpan komentar pengguna

# Fungsi untuk memeriksa apakah file CSV ada, jika tidak buat baru
def check_file():
    if not os.path.isfile("rating_data.csv"):
        with open("rating_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Rating", "Komentar"])  # Header CSV

# Fungsi untuk mengirim rating dan komentar
def submit_rating():
    rating = rating_var.get()  # Ambil rating dari radio button
    comment = comment_box.get("1.0", "end").strip()  # Ambil komentar dari textbox

    # Cek apakah rating dan komentar sudah diisi
    if rating == 0:
        messagebox.showwarning("Peringatan", "Pilih rating dulu, ya!")
    elif not comment:
        messagebox.showwarning("Peringatan", "Isi komentarnya dulu!")
    else:
        # Tambahkan rating dan komentar ke list
        ratings.append(rating)
        comments.append(comment)

        # Hitung rata-rata rating
        avg_rating = sum(ratings) / len(ratings)

        # Tampilkan hasil ke label
        result_label.config(
            text=f"Total Rating: {len(ratings)}\nRata-rata: {avg_rating:.2f}"
        )

        # Simpan data ke file CSV
        try:
            with open("rating_data.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([rating, comment])
            messagebox.showinfo("Sukses", "Rating dan komentar berhasil dikirim!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan data ke file: {e}")
        
        # Reset input
        rating_var.set(0)
        comment_box.delete("1.0", "end")

# Fungsi untuk reset data
def reset_data():
    global ratings, comments
    ratings = []
    comments = []

    # Kosongkan file CSV
    try:
        with open("rating_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Rating", "Komentar"])  # Header
        # Reset tampilan
        result_label.config(text="Belum ada data.")
        messagebox.showinfo("Reset", "Semua data berhasil dihapus!")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal mereset data: {e}")

# Fungsi untuk menampilkan grafik
def show_chart():
    if not ratings:
        messagebox.showwarning("Peringatan", "Belum ada data untuk ditampilkan!")
    else:
        # Hitung distribusi rating
        rating_count = [ratings.count(i) for i in range(1, 6)]

        # Buat grafik batang
        plt.bar(range(1, 6), rating_count, color="skyblue")
        plt.xlabel("Rating (1-5)")
        plt.ylabel("Jumlah")
        plt.title("Distribusi Rating Pelayanan CCTV")
        plt.show()

# GUI utama
root = tk.Tk()
root.title("Rating Pelayanan CCTV")
root.geometry("500x400")

# Periksa dan buat file CSV jika belum ada
check_file()

# Judul
title_label = tk.Label(root, text="Rating Pelayanan CCTV", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Pilihan rating
rating_var = tk.IntVar(value=0)
rating_label = tk.Label(root, text="Pilih Rating Anda:")
rating_label.pack()
for i in range(1, 6):
    tk.Radiobutton(root, text=f"{i} Bintang", variable=rating_var, value=i).pack()

# Input komentar
comment_label = tk.Label(root, text="Masukkan Komentar Anda:")
comment_label.pack(pady=5)
comment_box = tk.Text(root, height=5, width=40)
comment_box.pack(pady=5)

# Tombol Kirim
submit_button = tk.Button(root, text="Kirim", command=submit_rating)
submit_button.pack(pady=5)

# Label hasil
result_label = tk.Label(root, text="Belum ada data.", font=("Arial", 12))
result_label.pack(pady=10)

# Tombol Reset
reset_button = tk.Button(root, text="Reset Data", command=reset_data)
reset_button.pack(pady=5)

# Tombol Tampilkan Grafik
chart_button = tk.Button(root, text="Lihat Grafik", command=show_chart)
chart_button.pack(pady=5)

# Jalankan GUI
root.mainloop()
