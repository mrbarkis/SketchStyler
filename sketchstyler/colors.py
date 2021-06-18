from skimage.morphology import area_opening, area_closing
from cv2 import cvtColor, inRange, bitwise_or, COLOR_RGB2HSV, COLOR_HSV2RGB
from matplotlib.colors import rgb_to_hsv
import numpy as np


def rgb_masks(img):
    hsv_img = cvtColor(img, COLOR_RGB2HSV)
    # hue range 0-180 in cv
    reds_l = inRange(hsv_img, (0, 0, 0), (30, 255, 240))
    greens = inRange(hsv_img, (31, 0, 0), (90, 255, 240))
    blues = inRange(hsv_img, (91, 0, 0), (150, 255, 240))
    reds_u = inRange(hsv_img, (151, 0, 0), (180, 255, 240))
    reds = bitwise_or(reds_l, reds_u)

    return (reds, greens, blues) 


def change_color(img, color, mask):
    if mask.dtype == "uint8":
        mask = mask / 255

    if isinstance(color[0], int):
        color = [c / 255 for c in color]

    hue, saturation, val = rgb_to_hsv(color)
    hsv_img = cvtColor(img, COLOR_RGB2HSV)

    # Replace hue
    hue_scale = 180
    hsv_img[:, :, 0] = (
        np.multiply(hsv_img[:, :, 0], (1 - mask)) + (mask * hue * hue_scale)
    ).astype("uint8")

    # Scale saturation
    sat_scale = 255 * saturation / np.max(np.multiply(hsv_img[:, :, 1], mask))
    hsv_img[:, :, 1] = (
        np.multiply(hsv_img[:, :, 1], (1 - mask))
        + np.multiply(hsv_img[:, :, 1], mask) * sat_scale
    ).astype("uint8")

    # Scale value
    val_scale = 255 * val / np.max(np.multiply(hsv_img[:, :, 2], mask))
    hsv_img[:, :, 2] = (
        np.multiply(hsv_img[:, :, 2], (1 - mask))
        + np.multiply(hsv_img[:, :, 2], mask) * val_scale
    ).astype("uint8")

    return cvtColor(hsv_img, COLOR_HSV2RGB)


def combine_masks(masks):
    background = masks[0]
    for mask in masks:
        background = bitwise_or(background, mask)

    return area_opening(background,area_threshold=64) 


def rgb2(img, subs_r, subs_g, subs_b):
    colors = (subs_r, subs_g, subs_b)
    masks = rgb_masks(img)

    adjusted_img = img
    for c, m in zip(colors, masks):
        if c != None:
            adjusted_img = change_color(adjusted_img, c, m)

    return np.dstack((adjusted_img, combine_masks(masks)))  # add alpha
