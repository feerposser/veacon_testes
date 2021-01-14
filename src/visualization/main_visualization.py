
import csv, os
import matplotlib.pyplot as plt
from pathlib  import Path


def load_data():
    files_path = os.path.join(Path(os.getcwd()).parent, 'files')
    files = {}
    for file in os.listdir(files_path):
        file_path = os.path.join(files_path, file)
        with open(file_path, 'r') as csv_file:
            data = list(csv.reader(csv_file))
            if data != []:
                file_number = int(file[:file.find(".")])
                files[file_number] = data[0]
    return files


def ordened_subplot_plot_image(data):
    ordened_keys = sorted(data.keys())
    ordened_data = {}

    for item in ordened_keys:
        ordened_data[item] = sorted([int(rssi) for rssi in data[item]])

    fig, axs = plt.subplots(3, 5, figsize=(20,15), sharex="none")
    fig.suptitle("Testes de Oscilação", fontsize=50)
    axs = axs.flatten()
    index = 0
    for key in ordened_keys:
        try:
            axs[index].plot(ordened_data[ordened_keys[index]])
            axs[index].set_title(str(ordened_keys[index]))
            axs[index].xaxis.set_visible(False)
        except IndexError:
            pass
        finally:
            index += 1
    plt.savefig("ordened.png")


def unordained_subplot_plot_image(data):
    ordened_keys = sorted(data.keys())

    fig, axs = plt.subplots(3, 5, figsize=(20, 15), sharex="none")
    fig.suptitle("Testes de Oscilação", fontsize=50)
    axs = axs.flatten()
    index = 0
    for key in data:
        try:
            axs[index].plot(data[ordened_keys[index]])
            axs[index].set_title(str(ordened_keys[index]))
            axs[index].xaxis.set_visible(False)
        except IndexError:
            pass
        finally:
            index += 1
    plt.axis("off")
    plt.savefig("unordained.png")


if __name__ == "__main__":
    data = load_data()

    while True:
        option = input("o: gráfico ordenado\nu: gráfico não ordenado\n: ").upper()
        if option == "O":
            ordened_subplot_plot_image(data)
        elif option == "U":
            unordained_subplot_plot_image(data)
        else:
            break
