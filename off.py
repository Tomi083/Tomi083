import os
import time

def prank_hp_mati():
    os.system("clear")  # bersihin layar
    print("\033[40m")   # set background hitam
    print("\033[30m")   # set teks jadi hitam juga (jadi gak keliatan)
    for _ in range(100):  # spam layar biar full
        print(" " * 100)
    time.sleep(10000)  # tahan lama biar keliatan "mati"

try:
    prank_hp_mati()
except KeyboardInterrupt:
    print("\033[0m")  # reset warna kalau keluar
    print("PRANK SELESAI")
