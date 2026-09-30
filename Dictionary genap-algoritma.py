# a) Data awal: minimal 3 kontak (nama -> nomor HP)
buku_kontak = {
    "Budi": "081234567890",
    "Andi": "089876543210",
    "Siti": "085612345678"
}

# c) Gunakan while loop untuk menu berulang
while True:
    print("\n=== MENU BUKU KONTAK ===")
    print("1. Lihat Semua Kontak")
    print("2. Cari Kontak Berdasarkan Nama")
    print("3. Tambah Kontak Baru")
    print("4. Hapus Kontak")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    # b) Menu: Lihat semua kontak
    if pilihan == "1":
        print("\n--- Daftar Semua Kontak ---")
        if not buku_kontak:
            print("Buku kontak masih kosong.")
        else:
            for nama, nomor in buku_kontak.items():
                print(f"- {nama}: {nomor}")
                
    # b) Menu: Cari kontak & d) Gunakan .get() saat mencari kontak
    elif pilihan == "2":
        print("\n--- Cari Kontak ---")
        nama_cari = input("Masukkan nama yang dicari: ")
        # Menggunakan .get() dengan default value jika tidak ditemukan
        hasil = buku_kontak.get(nama_cari, "Kontak tidak ditemukan.")
        
        if hasil == "Kontak tidak ditemukan.":
            print(hasil)
        else:
            print(f"Nomor HP {nama_cari}: {hasil}")
            
    # b) Menu: Tambah kontak baru
    elif pilihan == "3":
        print("\n--- Tambah Kontak Baru ---")
        nama_baru = input("Masukkan nama baru: ")
        nomor_baru = input("Masukkan nomor HP baru: ")
        buku_kontak[nama_baru] = nomor_baru
        print(f"Kontak {nama_baru} berhasil ditambahkan!")
        
    # b) Menu: Hapus kontak
    elif pilihan == "4":
        print("\n--- Hapus Kontak ---")
        nama_hapus = input("Masukkan nama kontak yang ingin dihapus: ")
        if nama_hapus in buku_kontak:
            del buku_kontak[nama_hapus]
            print(f"Kontak {nama_hapus} berhasil dihapus.")
        else:
            print("Nama tidak ditemukan di buku kontak.")
            
    # b) Menu: Keluar
    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan program buku kontak!")
        break
        
    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-5.")
