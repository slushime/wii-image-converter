git branch -M main
git push -u origin main



from PIL import Image, ImageDraw, ImageTk
import os, tkinter as tk
from tkinter import filedialog
import random


# Define the download folder and output path
download_folder = os.path.join(os.path.expanduser("~"), "Downloads")



# Create a simple GUI to select an image file
def open_file_dialog():
    filepath = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if filepath:
        label.config(text=f"Saved to: {download_folder}")
        try:
            # load image
            image_name = "wii-image-output" + str(random.randint(0, 10**10)) + ".png"
            output_path = os.path.join(download_folder, image_name)
            image = Image.open(filepath).convert("RGBA")


            # create mask with rounded corners
            mask = Image.new("L", image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0, image.width, image.height), radius=89, fill=255)


            # apply mask to image
            image.putalpha(mask)


            # resize image
            image = image.resize((781, 425))
            # save the image
            image.save(output_path, "PNG")
            # image.show()

            label.config(text=f"Image saved as: {image_name}\n\nLocation: {output_path}")

            tk_image = ImageTk.PhotoImage(image)

            image_label.img = tk_image
            image_label.config(image=tk_image)


        except Exception as e:
            print(f"Error processing image: ", e)
            label.config(text="Error processing image. Check console for details.")


# Basic GUI window setup
window = tk.Tk()
window.title("Wii Image Cropper")
window.geometry("900x600")


# Button to open file dialog
button = tk.Button(window, text="Select Image", command=open_file_dialog)
button.pack(pady=20)


# Label to display selected file path
label = tk.Label(window, text="No file selected")
label.pack(pady=10)


image_label = tk.Label(window)
image_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()