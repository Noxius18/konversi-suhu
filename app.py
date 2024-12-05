from suhu import Celcius, Fahrenheit, Reamur, Kelvin
from rich.console import Console; from rich.table import Table; from rich.prompt import Prompt
import os; import platform


console = Console()

def clear():
    os.system("cls") if platform.system() == "Windows" else os.system("clear")

def main():
    while(True):
        clear()
    
        console.print(f"Konversi Suhu", style="bold underline")
        console.print("=" * 10)
        console.print(f"1. Dalam Celsius")
        console.print(f"2. Dalam Fahrenheit")
        console.print(f"3. Dalam Reamur")
        console.print(f"4. Dalam Kelvin")

        print("Pilih Opsi")
        pilihan = Prompt.ask("> ", choices=["1", "2", "3", "4"])

        if pilihan == '1':
            suhu_celsius = Prompt.ask("Masukkan suhu dalam Celsius", default="0", show_default=True)
            celcius = Celcius(float(suhu_celsius))
            hasil = [
                ("Celcius (°C)",    f"{float(suhu_celsius):.2f}"),
                ("Fahrenheit (°F)", f"{celcius.fahrenheit():.2f}"),
                ("Reamur (°R)",     f"{celcius.reamur():.2f}"),
                ("Kelvin (°K)",     f"{celcius.kelvin():.2f}")
            ]

        elif pilihan == '2':
            suhu_fahrenheit = Prompt.ask("Masukkan suhu dalam Fahrenheit", default="0", show_default=True)
            fahrenheit = Fahrenheit(float(suhu_fahrenheit))
            hasil = [
                ("Fahrenheit (°F)", f"{float(suhu_fahrenheit):.2f}"),
                ("Celcius (°C)",    f"{fahrenheit.celcius():.2f}"),
                ("Reamur (°R)",     f"{fahrenheit.reamur():.2f}"),
                ("Kelvin (°K)",     f"{fahrenheit.kelvin():.2f}")
            ]

        elif pilihan == '3':
            suhu_reamur = Prompt.ask("Masukkan suhu dalam Reamur", default="0", show_default=True)
            reamur = Reamur(float(suhu_reamur))
            hasil = [
                ("Reamur (°R)",     f"{float(suhu_reamur):.2f}"),
                ("Celcius (°C)",    f"{reamur.celcius():.2f}"),
                ("Fahrenheit (°F)", f"{reamur.fahrenheit():.2f}"),
                ("Kelvin (°K)",     f"{reamur.kelvin():.2f}")
            ]

        elif pilihan == '4':
            suhu_kelvin = Prompt.ask("Masukkan suhu dalam Kelvin", default="0", show_default=True)
            kelvin = Kelvin(float(suhu_kelvin))
            hasil = [
                ("Kelvin (°K)",     f"{float(suhu_kelvin):.2f}"),
                ("Celcius (°C)",    f"{kelvin.celcius():.2f}"),
                ("Fahrenheit (°F)", f"{kelvin.fahrenheit():.2f}"),
                ("Reamur (°R)",     f"{kelvin.reamur():.2f}")
            ]

        else:
            console.print("Pilihan tidak valid!", style="bold red")
            return

        tabel = Table(title="Hasil Konversi Suhu")
        
        
        for judul, _ in hasil: # Menambahkan kolom ke tabel
            tabel.add_column(judul, style="cyan")
        tabel.add_row(*[str(nilai) for _, nilai in hasil]) # Menambahkan baris ke tabel
        console.print(tabel)

        # Input untuk user jika user ingin melakukan konversi lagi
        ulang = Prompt.ask("Apakah ingin melakukan konversi lagi? (y/n)", choices=["y", "n"])
        if(ulang == "n"):
            console.print("Terima Kasih telah menggunakan program ini", style="bold green")
            break

if __name__ == "__main__":
    main()