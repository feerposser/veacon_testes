import os
import csv

from constant_ble_read import ReadBLE

files_path = os.path.join(os.getcwd(), 'files')

while True:
    try:
        start = input("Iniciar teste s/n: ")
        if start.upper() != "S":
            break

        name = input("Número do teste: ")
        read_time_sec = int(input("Tempo de leitura (segundos - mínimo 10): "))
        if read_time_sec < 10:
            read_time_sec = 10

        path_file = os.path.join(files_path, "{}.csv".format(name))

        csv_file = open(path_file, "w")

        rssi_list = ReadBLE(read_time_sec, "edd1ebeac04e5defa017").read_ble()

        if not rssi_list:
            raise Exception("Lista de rssi vazia.")

        with csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(rssi_list)
    except Exception as e:
        print("Erro: ", e)
