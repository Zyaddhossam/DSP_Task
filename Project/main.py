import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageFont
import cv2
import numpy as np

SEED = 50000
np.random.seed(SEED)


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")
        self.root.geometry("1050x400")
        self.root.configure(bg='#ffffff')

        self.folder_path = tk.StringVar()
        self.status_text = tk.StringVar()

        self.font = ("Arial", 12)
        self.btn_color = "#8668ae"
        self.fg_color = "#000000"

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=self.font, padding=10)
        style.map("TButton", background=[('active', '#30cfcf')])

        # Folder selection
        path_frame = tk.Frame(self.root, bg='#ffffff')
        path_frame.pack(pady=10)
        tk.Button(path_frame, text="Choose Folder", font=self.font, bg=self.btn_color, fg=self.fg_color,
                  command=self.select_folder).pack(side=tk.LEFT, padx=10)
        tk.Label(path_frame, textvariable=self.folder_path, font=self.font, bg='#ffffff').pack(side=tk.LEFT)

        # Operations Frame
        self.buttons_frame = tk.LabelFrame(self.root, text="Choose Operation", font=self.font, bg='#ffffff')
        self.buttons_frame.pack(pady=10, fill="x", padx=20)

        operations = [
            ("Resize", self.show_resize_inputs),
            ("Grayscale", self.grayscale_images),
            ("Rotate", self.show_rotate_inputs),
            ("Brightness", self.show_brightness_inputs),
            ("Add Text", self.show_text_inputs),
            ("Blur", self.blur_images),
            ("Invert Colors", self.invert_images),
            ("Add Gaussian Noise", self.add_gaussian_noise),
            ("Remove Gaussian Noise", self.remove_gaussian_noise),
        ]

        for op, cmd in operations:
            btn = tk.Button(self.buttons_frame, text=op, font=self.font, bg=self.btn_color, fg=self.fg_color,
                            command=cmd)
            btn.pack(side=tk.LEFT, padx=8, pady=5)

        # Parameters Frame
        self.param_frame = tk.Frame(self.root, bg='#ffffff')
        self.param_frame.pack(pady=10)

        # Status
        self.status_label = tk.Label(self.root, textvariable=self.status_text, font=self.font, bg='#ffffff')
        self.status_label.pack(pady=10)

    def select_folder(self):
        path = filedialog.askdirectory()
        self.folder_path.set(path)
        self.status_text.set("")

    def clear_param_frame(self):
        for widget in self.param_frame.winfo_children():
            widget.destroy()

    def get_images(self):
        folder = self.folder_path.get()
        return [os.path.join(folder, f) for f in os.listdir(folder)
                if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    def process_and_save(self, op_name, processor_func):
        folder = self.folder_path.get()
        if not folder:
            self.status_text.set("Please select a folder first.")
            self.status_label.config(fg="red")
            return

        out_dir = os.path.join(folder, op_name.replace(" ", "_"))
        os.makedirs(out_dir, exist_ok=True)

        count = 0
        for img_path in self.get_images():
            img = Image.open(img_path)
            processed = processor_func(img)
            filename = os.path.basename(img_path)
            processed.save(os.path.join(out_dir, filename))
            count += 1
        self.status_text.set(f"{op_name} completed on {count} image(s).")
        self.status_label.config(fg="green")

    # --- Resize ---
    def show_resize_inputs(self):
        self.clear_param_frame()
        tk.Label(self.param_frame, text="Width:", bg='#ffffff', font=self.font).grid(row=0, column=0)
        width = tk.Entry(self.param_frame, font=self.font)
        width.grid(row=0, column=1)

        tk.Label(self.param_frame, text="Height:", bg='#ffffff', font=self.font).grid(row=0, column=2)
        height = tk.Entry(self.param_frame, font=self.font)
        height.grid(row=0, column=3)

        tk.Button(self.param_frame, text="Apply", font=self.font, bg=self.btn_color, fg=self.fg_color,
                  command=lambda: self.process_and_save("Resized", lambda img: img.resize(
                      (int(width.get()), int(height.get()))))).grid(row=0, column=4, padx=10)

    # --- Grayscale ---
    def grayscale_images(self):
        self.clear_param_frame()
        self.process_and_save("Grayscale", lambda img: img.convert("L"))

    # --- Rotate ---
    def show_rotate_inputs(self):
        self.clear_param_frame()
        tk.Label(self.param_frame, text="Angle (0-360):", bg='#ffffff', font=self.font).grid(row=0, column=0)
        angle = tk.Entry(self.param_frame, font=self.font)
        angle.grid(row=0, column=1)

        tk.Button(self.param_frame, text="Apply", font=self.font, bg=self.btn_color, fg=self.fg_color,
                  command=lambda: self.process_and_save("Rotated", lambda img: img.rotate(float(angle.get())))).grid(
            row=0, column=2, padx=10)

    # --- Brightness ---
    def show_brightness_inputs(self):
        self.clear_param_frame()
        tk.Label(self.param_frame, text="Factor (0.1 to 2):", bg='#ffffff', font=self.font).grid(row=0, column=0)
        factor = tk.Entry(self.param_frame, font=self.font)
        factor.grid(row=0, column=1)

        tk.Button(self.param_frame, text="Apply", font=self.font, bg=self.btn_color, fg=self.fg_color,
                  command=lambda: self.process_and_save("Brightness_Changed",
                                                        lambda img: ImageEnhance.Brightness(img).enhance(
                                                            float(factor.get())))).grid(row=0, column=2, padx=10)

    # --- Add Text ---
    def show_text_inputs(self):
        self.clear_param_frame()
        tk.Label(self.param_frame, text="Text:", bg='#ffffff', font=self.font).grid(row=0, column=0)
        text = tk.Entry(self.param_frame, font=self.font)
        text.grid(row=0, column=1)

        tk.Button(self.param_frame, text="Apply", font=self.font, bg=self.btn_color, fg=self.fg_color,
                  command=lambda: self.process_and_save("Text_Added", lambda img: self.add_text(img, text.get()))).grid(
            row=0, column=2, padx=10)

    def add_text(self, img, content):
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", size=100)
        draw.text((10, 10), content, font=font, fill="white")
        return img

    # --- Blur ---
    def blur_images(self):
        self.clear_param_frame()
        self.process_and_save("Blurred", lambda img: img.filter(ImageFilter.GaussianBlur(5)))

    # --- Invert ---
    def invert_images(self):
        self.clear_param_frame()
        self.process_and_save("Inverted", lambda img: ImageOps.invert(img.convert("RGB")))

    # --- Gaussian Noise ---
    def add_gaussian_noise(self):
        self.clear_param_frame()

        def apply_noise(img_path):
            img = Image.open(img_path)
            img_array = np.array(img)

            mean = 0
            stddev = 25
            noise = np.random.normal(mean, stddev, img_array.shape)

            noisy_img_array = img_array + noise
            noisy_img_array = np.clip(noisy_img_array, 0, 255).astype(np.uint8)

            noisy_img = Image.fromarray(noisy_img_array)
            return noisy_img

        self.process_and_save("Gaussian_Noise", lambda img: apply_noise(img.filename))

    # --- Remove Gaussian Noise ---
    def remove_gaussian_noise(self):
        self.clear_param_frame()

        def denoise(img_path):
            img = Image.open(img_path).convert("RGB")
            img_array = np.array(img)

            bgr_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

            denoised_bgr = cv2.fastNlMeansDenoisingColored(bgr_img, None, 10, 8, 7, 21)

            denoised_rgb = cv2.cvtColor(denoised_bgr, cv2.COLOR_BGR2RGB)

            return Image.fromarray(denoised_rgb)

        self.process_and_save("Gaussian_Noise_Removed", lambda img: denoise(img.filename))


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
