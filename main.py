import math

# 1. Tabung Tanpa Tutup
def tabung_tanpa_tutup(r, t):
    volume = math.pi * r**2 * t
    luas = (math.pi * r**2) + (2 * math.pi * r * t)
    return volume, luas

# 2. Setengah Bola
def setengah_bola(r):
    volume = 2/3 * math.pi * r**3
    luas = 3 * math.pi * r**2
    return volume, luas

# 3. Volume Kubus
def volume_kubus(s):
    return s**3

# 4. Luas Balok
def luas_balok(p, l, t):
    return 2 * (p*l + p*t + l*t)

# ===== MENU UTAMA =====
while True:
    print("\n=== KALKULATOR BANGUN RUANG ===")
    print("1. Tabung Tanpa Tutup")
    print("2. Setengah Bola")
    print("3. Volume Kubus")
    print("4. Luas Balok")
    print("5. Keluar")
    
    pilih = input("Pilih (1-5): ")

    if pilih == "1":
        r = float(input("Jari-jari: "))
        t = float(input("Tinggi: "))
        v, l = tabung_tanpa_tutup(r, t)
        print(f"Hasil -> Volume: {v:.2f} | Luas: {l:.2f}")

    elif pilih == "2":
        r = float(input("Jari-jari: "))
        v, l = setengah_bola(r)
        print(f"Hasil -> Volume: {v:.2f} | Luas: {l:.2f}")

    elif pilih == "3":
        s = float(input("Sisi kubus: "))
        v = volume_kubus(s)
        print(f"Hasil -> Volume Kubus: {v}")

    elif pilih == "4":
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        t = float(input("Tinggi: "))
        luas = luas_balok(p, l, t)
        print(f"Hasil -> Luas Balok: {luas}")

    elif pilih == "5":
        print("\nTerima kasih sudah menggunakan kalkulator ini!")
        print("Dibuat oleh : NAURA JANNATI")
        print("Kelas       : X.1")
        break
    else:
        print("Pilihan tidak tersedia, silakan pilih 1-5")
