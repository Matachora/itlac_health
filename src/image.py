import tkinter as tk
from PIL import Image, ImageTk

def display_image(image_path):
    """
    Displays an image in a Tkinter window.

    Args:
        image_path: Path to the image file.
    """

    root = tk.Tk()
    root.title("Image Viewer")

    # Load the image using Pillow
    img = Image.open(image_path)
    img = img.resize((400, 300))  # Resize the image (optional)
    photo = ImageTk.PhotoImage(img)

    # Create a label to display the image
    image_label = tk.Label(root, image=photo)
    image_label.pack()

    root.mainloop()

# Example usage:
if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"  # Replace with the actual path
    display_image(image_path)