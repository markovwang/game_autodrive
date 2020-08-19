import os
import numpy as np
import cv2


def read_file(path: str, label: bool):
    """
    the function is to read the datas and label them (if it is avaliabel)
    path:the path you store you pics
    label : if you have some labels
    returns : if labeled: pic_data and label
              else :pic_data
    """
    img_dir = sorted(os.listdir(path))
    pic_datas = np.zeros((len(img_dir), 300, 400, 3), dtype=np.uint8)
    labels = np.zeros((len(img_dir)), dtype=np.uint8)
    # print(pic_datas.shape)
    for i, file in enumerate(img_dir):
        if i % 500 == 0:
            print("already imported {}".format(i), " images")
        img = cv2.imread(os.path.join(path, file))
        pic_datas[i, :, :] = img
        if label:
            labels[i] = int(file.split("_")[0])
    if label:
        return pic_datas, labels
    else:
        return pic_datas


if __name__ == '__main__':
    path = r'screen'
    trainX, trainY = read_file(path=path, label=True)

    print(trainX.shape)
    print(trainY.shape)
