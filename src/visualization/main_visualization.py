
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


def subplot_plot_image(ordened_keys, ordened_data):
    fig, axs = plt.subplots(3, 5, figsize=(20,15), sharex="none")
    fig.suptitle("Testes de Oscilação", fontsize=50)
    axs = axs.flatten()
    index = 0
    for key in ordened_keys:
        try:
            axs[index].plot(ordened_data[ordened_keys[index]])
            axs[index].set_title(str(ordened_keys[index]))
        except IndexError:
            pass
        finally:
            index += 1
    # axs[0].plot(ordened_data[ordened_keys[0]])
    # axs[1].plot(ordened_data[ordened_keys[1]])
    # axs[2].plot(ordened_data[ordened_keys[2]])
    plt.savefig("mygraph.png")


if __name__ == "__main__":
    data = load_data()

    ordened_keys = sorted(data.keys())
    ordened_data = {}
    
    for item in ordened_keys:
        ordened_data[item] = sorted([int(rssi) for rssi in data[item]])

    subplot_plot_image(ordened_keys, ordened_data)
    
    # print("Ordened key and data:")
    # for key in ordened_keys:
    #     print("key:", key)
    #     print("Original:", data[key])
    #     print("Ordened:", ordened_data[key])
    #     print("\n")
    