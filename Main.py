import matplotlib.pylab as plt
from API import transfer_style
import os

if __name__ == "__main__":

    # Path of the pre-trained TF model 
    model_path = r"magenta_arbitrary-image-stylization-v1-256_2"

    # NOTE : Works only for '.jpg' and '.png' extensions,other formats may give error
    content_image_dir = "images"
    style_image_dir = "styles"
    save_dir = "results"
    # style_name = "scream.jpg"
    for i, img_name in enumerate(os.listdir(content_image_dir)):
        for style_name in os.listdir(style_image_dir):
            content_image_path = os.path.join(content_image_dir, img_name)
            style_image_path = os.path.join(style_image_dir, style_name)

            img = transfer_style(content_image_path, style_image_path, model_path)
            # Saving the generated image
            plt.imsave(os.path.join(save_dir, str(i) + "_" + style_name.split(".")[0] + ".jpg"), img)
            plt.imshow(img)
    print("Done!!")
