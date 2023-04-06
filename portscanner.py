import tkinter as tk
from tkinter import messagebox
import socket
import threading

def port_tarama():
    hedef_ip = hedef_ip_entry.get()  # Kullanıcıdan hedef IP adresini al
    baslangic_port = int(baslangic_port_entry.get())  # Kullanıcıdan başlangıç portunu al
    bitis_port = int(bitis_port_entry.get())  # Kullanıcıdan bitiş portunu al

    sonuclar.delete(1.0, tk.END)  # Sonuçları temizle

    try:
        # Port taramasını gerçekleştirmek için yardımcı iş parçacığı (thread) oluştur
        def tara():
            for port in range(baslangic_port, bitis_port+1):
                soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                soket.settimeout(1)
                sonuc = soket.connect_ex((hedef_ip, port))
                if sonuc == 0:
                    sonuclar.insert(tk.END, f"{hedef_ip}:{port} portu açık\n")
                soket.close()
            sonuclar.insert(tk.END, "Tarama tamamlandı. FİN\n")

        # Yardımcı iş parçacığı başlat
        t = threading.Thread(target=tara)
        t.start()

    except Exception as e:
        messagebox.showerror("Hata", f"Hata: {e}")

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Port Tarayıcı")

# Kullanıcıdan hedef IP adresini, başlangıç ve bitiş portlarını girebileceği giriş kutularını oluştur
hedef_ip_label = tk.Label(pencere, text="Hedef IP:")
hedef_ip_label.pack()
hedef_ip_entry = tk.Entry(pencere)
hedef_ip_entry.pack()

baslangic_port_label = tk.Label(pencere, text="Başlangıç Port:")
baslangic_port_label.pack()
baslangic_port_entry = tk.Entry(pencere)
baslangic_port_entry.pack()

bitis_port_label = tk.Label(pencere, text="Bitiş Port:")
bitis_port_label.pack()
bitis_port_entry = tk.Entry(pencere)
bitis_port_entry.pack()

# Sonuçları görüntülemek için bir metin kutusu oluştur
sonuclar_label = tk.Label(pencere, text="Sonuçlar:")
sonuclar_label.pack()
sonuclar = tk.Text(pencere)
sonuclar.pack()

# Port tarama butonunu oluştur
tara_button = tk.Button(pencere, text="Portları Tara", command=port_tarama)
tara_button.pack()

pencere.mainloop()
