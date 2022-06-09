from PIL import Image
import zbarlight
import base64
import numpy as np
import os

img = 'cbimage.png'


def main():
    img_data = input("imgdata:").encode()
    with open(img, "wb") as fh:
        fh.write(base64.decodebytes(img_data))

    file_path = img
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()

    np_array = np.array(image)
    f = (["1" if i[0] < 128 else "0" for i in np_array[0]])

    data = "".join(f)

    with open("table.md", "r") as f:
        table = [[a.strip() for a in i.split("│")] for i in f.readlines()]

    l = []
    codetable = [i[8] if len(i) != 1 else None for i in table]
    # print(codetable)
    outut = ""
    while len(data) >= 11:
        ind = codetable.index(data[:11])
        data = data[11:]
        try:
            l.append(int(table[ind][6]))
        except:
            print("N'est pas passé", table[ind][5])
    for i in l:
        outut += chr(i)
    os.system(f"echo '{outut}' | xsel --clipboard")
    print()


while 1:
    main()