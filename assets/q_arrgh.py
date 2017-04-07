import json
import numpy as np
import matplotlib.pyplot as plt


def give_me_data():
    with open('./assets/qrcode_data.json') as j:
        dict = json.load(j)
    return dict


def show(some_2d_array_of_integers):
    np_array = np.array(some_2d_array_of_integers)
    plt.matshow(np_array)
    plt.show()
    return "something"
