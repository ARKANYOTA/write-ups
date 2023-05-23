# Python 3.11.3
import numpy as np
import tensorflow as tf
from urllib import request
from PIL import Image
from TresTresSecret import drapeau


def main(file):
    je_merite_le_drapeau = True
    chat_modifie = Image.open(file)

    # Modèle utilisé : ResNet50 de TensorFlow
    model = tf.keras.applications.resnet50.ResNet50(weights='imagenet')

    # Mise du chat dans le réseau
    image_raw = tf.io.read_file(file)
    image = tf.image.decode_image(image_raw)

    # Prétraitement de l'image : on utilise directement la fonction de ResNet50
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (224, 224))
    image = tf.keras.applications.resnet50.preprocess_input(image)
    image = image[None, ...]

    # Prédiction de l'image
    image_probs = model.predict(image)
    _, image_class, class_confidence = tf.keras.applications.resnet50.decode_predictions(image_probs, top=1)[0][0]

    for y,i in enumerate(tf.keras.applications.resnet50.decode_predictions(image_probs, top=998)[0]):
        if (i[1] == "teapot"):
            print(y, str(i))
    # On vérifie que c'est bien une théière
    print("class, confidence:", image_class, class_confidence)
    if image_class != 'teapot':
        je_merite_le_drapeau = False
    else:
        print("Ce est un teapot")

    # On cherche le vrai chat
    chat = Image.open('chat.jpg')
    taille = chat.size

    # On utilise la norme L2
    def distance(a, b):
        return np.linalg.norm(np.array(a) - np.array(b))

    # On vérifie enfin si le chat n'a pas été trop ~modifié~~
    eps = 70
    a = 0
    print("pixel not match:")
    for x in range(taille[0]):
        for y in range(taille[1]):
            if distance(chat.getpixel((x, y)), chat_modifie.getpixel((x, y))) > eps:

                a += 1

                print(f"pos: {x},{y} pixel :" ,chat.getpixel((x, y)), chat_modifie.getpixel((x, y)), distance(chat.getpixel((x, y)), chat_modifie.getpixel((x, y))))
                je_merite_le_drapeau = False
                # print(f"({x},{y})", end = "")
    print("\nnb de mauvais pixel = ", a)

    if je_merite_le_drapeau:
        print(f'Je mérite le drapeau. Le voici : {drapeau}')
    else:
        print('Je ne mérite pas le drapeau')


file = "theiere.v4.png"
main(file)
