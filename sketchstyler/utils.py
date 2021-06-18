from os import path
import matplotlib.pyplot as plt
from cv2 import imread, cvtColor, COLOR_BGR2RGB
import json


def show_img(img, size=(5, 5)):
    fig, ax = plt.subplots(figsize=size)
    ax.imshow(img, cmap="gray")
    ax.axis("off")
    plt.show()


def save_img(name, img):
    if img.dtype != "uint8":
        img = (255 * img).astype("uint8")

    plt.imsave(name, img)


def load_img(file):
    return cvtColor(imread(file), COLOR_BGR2RGB)


def load_sample(nbr=0):
    file = path.join(path.dirname(__file__), "img", f"{nbr}.jpg")
    return load_img(file)


def load_palettes():
    file = path.join(path.dirname(__file__), "palettes", "palettes.json")
    palettes = None
    with open(file, "r") as f:
        palettes = json.load(f)

    return palettes


def load_palette(name):
    return load_palettes()[name]


def list_palettes():
    return list(load_palettes().keys())


def save_palette(colors, name="newest"):
    file = path.join(path.dirname(__file__), "palettes", "palettes.json")
    try:
        palettes = load_palettes()
    except FileNotFoundError:
        palettes = {}

    palettes[name] = colors
    with open(file, "w") as f:
        json.dump(palettes, f)


def remove_palette(name):
    if name == "default":
        print("Cannot remove the default. (You can overwrite it though.)")
        return None

    file = path.join(path.dirname(__file__), "palettes", "palettes.json")
    try:
        palettes = load_palettes()
    except FileNotFoundError:
        palettes = {}
    try:
        del palettes[name]
    except KeyError:
        print(f"Palette called '{name}' does not exist.")

    with open(file, "w") as f:
        json.dump(palettes, f)
