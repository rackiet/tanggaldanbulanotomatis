from datetime import datetime, timedelta

# Fungsi untuk konversi bulan ke nama bulan dalam bahasa Indonesia
def get_month_name_in_indonesian(month):
    month_names = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember"
    }
    return month_names.get(month, "Invalid month")

def main():
    try:
        # Meminta pengguna memasukkan tanggal saat program berjalan
        start_date_str = input("Masukkan tanggal awal (dd-mm-yyyy): ")
        end_date_str = input("Masukkan tanggal akhir (dd-mm-yyyy): ")

        # Konversi string ke objek datetime
        start_date = datetime.strptime(start_date_str, '%d-%m-%Y')
        end_date = datetime.strptime(end_date_str, '%d-%m-%Y')

        if start_date > end_date:
            print("Tanggal awal harus lebih kecil atau sama dengan tanggal akhir.")
            return

        # Membuka file untuk menulis output
        with open("tanggal.txt", "w") as file:
            current_date = start_date
            while current_date <= end_date:
                day = current_date.day
                month = get_month_name_in_indonesian(current_date.month)
                date_str = f"{day} {month}"
                print(date_str)
                file.write(date_str + "\n")
                current_date += timedelta(days=1)
        
        print("Tanggal telah diekspor ke tanggal.txt")

    except ValueError:
        print("Format tanggal salah. Mohon masukkan dalam format dd-mm-yyyy.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
