from PIL import Image
def Is_sadness():
    sad_eyes_img = Image.open('sad_eyes.png')
    sad_lids_img = Image.open('sad_lids.png')
    return (sad_eyes_img.show(),sad_lids_img.show())

def Is_joy():
    joy_eyes_img = Image.open('joy_eyes.png')
    joy_lids_img = Image.open('joy_lids.png')
    return (joy_eyes_img.show(),joy_lids_img.show())

def Is_neutral():
    neutral_eyes_img = Image.open('neutral_eyes.png')
    neutral_lids_img = Image.open('neutral_lids.png')
    return (neutral_eyes_img.show(),neutral_lids_img.show())