import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def create_app():
    # Initialize the main window
    root = tk.Tk()
    root.title("Simple Image & Metadata Viewer")

    # Open a file dialog to select an image
    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    # Check if a file was actually selected
    if not image_path:
        messagebox.showwarning("No File", "No image was selected. Closing app.")
        root.destroy()
        return

    try:
        # 1. Load the image using Pillow
        img = Image.open(image_path)
        
        # Extract basic metadata
        metadata_text = (
            f"Filename: {image_path.split('/')[-1]}\n"
            f"Format: {img.format}\n"
            f"Size: {img.width}x{img.height}\n"
            f"Mode: {img.mode}"
        )

        # Optional: Resize for display if the image is huge
        display_img = img.copy()
        display_img.thumbnail((500, 500)) 
        photo = ImageTk.PhotoImage(display_img)

        # 2. Create Layout (Frames)
        img_frame = tk.Frame(root, padx=20, pady=20)
        img_frame.pack(side="right")

        meta_frame = tk.Frame(root, padx=20, pady=20)
        meta_frame.pack(side="left", fill="y")

        # 3. Add Widgets
        img_label = tk.Label(img_frame, image=photo)
        img_label.image = photo  # Critical: Keep a reference to avoid garbage collection
        img_label.pack()

        tk.Label(meta_frame, text="Metadata", font=("Arial", 14, "bold")).pack(anchor="w")
        tk.Label(meta_frame, text=metadata_text, justify="left", font=("Consolas", 10)).pack(anchor="w", pady=10)

        root.mainloop()

    except Exception as e:
        messagebox.showerror("Error", f"Could not open image: {e}")
        root.destroy()

# Run the app
if __name__ == "__main__":
    create_app()