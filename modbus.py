import time
import os
from pymodbus.client import ModbusTcpClient
from dotenv import load_dotenv

load_dotenv()

def read_modbus_data():
    # Konfigurasi koneksi Modbus
    modbus_host = os.getenv("IP")
    modbus_port = os.getenv("PORT")

    # Inisialisasi klien Modbus
    client = ModbusTcpClient(modbus_host, port=modbus_port)

    while True:
        # Coba koneksi ke server Modbus
        connection = client.connect()
        if connection:
            pass
        else:
            print("Koneksi gagal")
            break

        # Membaca 2 input register mulai dari address 24
        address = 24
        count = 2
        try:
            result = client.read_input_registers(address, count, slave=1)
            if not result.isError():
                # Menampilkan data yang dibaca
                print(f"Data dari address {address}: {result.registers}")
            else:
                print(f"Gagal membaca data dari Modbus: {result}")
        except Exception as e:
            print(f"Exception: {e}")

        # Tutup koneksi
        client.close()

        # Tunggu selama 5 detik sebelum polling berikutnya
        time.sleep(5)

if __name__ == "__main__":
    read_modbus_data()
