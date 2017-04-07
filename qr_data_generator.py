import numpy as np
# import matplotlib # next two lines needed for me, ubuntu also?
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import qrcode
import random
import csv
import json
# displaying
# plt.imshow(img_object_or_array)
# plt.show()

# array oporations
# for index, item in enumerate(items):
# for index, value in np.ndenumerate(test): print(index, value)
# bin(number)
# bytearray()
# random.sample(list, list_length)


def int_to_string(some_integer):
    a_string = str(some_integer)
    if len(a_string) == 1:
        return str(0) + a_string

    return a_string


def array_to_pairs(some_2d_array):
    list_of_pairs = []
    for y_index, y in enumerate(some_2d_array):
        for x_index, x in enumerate(y):
            coord = int_to_string(x_index) + int_to_string(y_index)
            list_of_pairs = list_of_pairs + [(coord, x)]

    return list_of_pairs


def build_dict(some_2d_array):
    pairs = array_to_pairs(some_2d_array)
    pairs = random.sample(pairs, len(pairs))

    return {key: value for (key, value) in pairs}


def bool_to_int(bool_array):
    array_copy = bool_array[:]
    for y_index, y in enumerate(bool_array):
        for x_index, x in enumerate(y):
            array_copy[y_index][x_index] = int(x)
    return array_copy


def get_qr_matrix(qr_payload, return_type='numpy'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0)

    qr.add_data(payload)
    qr.make(fit=True)

    bool_array = qr.get_matrix()
    int_array = bool_to_int(bool_array)
    np_array = np.array(int_array)

    plt.matshow(np_array)
    plt.show()

    if return_type == 'numpy':
        return bool_array

    if return_type == 'bool':
        return int_array

    if return_type == 'numpy':
        return np_array


def gen_qr_csv_file(payload='this data string is encoded into qrcode'):
    array = get_qr_matrix(payload)
    dictionary = build_dict(array)

    with open('qrcode_data.json', 'w') as data_file:
        json.dump(dictionary, data_file, indent=4)
