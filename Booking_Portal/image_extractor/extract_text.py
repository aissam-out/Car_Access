from utils import crop, togrey, extact_text

image_path = "images/cin5.jpg"
cropped_image = 'cropped.jpg'
grey_image = "greyscale.png"

def extract_pipeline(image_path, cropped_image, grey_image):
    c_img = crop(image_path, cropped_image)
    g_img = togrey(cropped_image, grey_image)
    text = extact_text(grey_image)

    return text

extract_pipeline(image_path, cropped_image, grey_image)
