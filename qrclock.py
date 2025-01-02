import qrcode
from PIL import Image, ImageTk
import tkinter as tk
import time


def update_qr():
    """Update the QR code with the current epoch time."""
    global qr_img
    epoch_time = int(time.time())  # Get current epoch time
    qr = qrcode.QRCode(box_size=10, border=5)
    qr.add_data(str(epoch_time))
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    resize_qr()  # Resize QR code to fit the window
    
    # Schedule the function to run again in 1000ms
    root.after(1000, update_qr)


def resize_qr(event=None):
    """Resize the QR code image to fit the current window size."""
    global qr_img
    if qr_img:
        # Get the current window dimensions
        window_width = root.winfo_width()
        window_height = root.winfo_height()
        
        # Determine the new size for the QR code
        size = min(window_width, window_height) - 20  # Leave some padding
        size = max(size, 10)  # Ensure it's not too small
        
        # Resize the QR code image
        resized_img = qr_img.resize((size, size), Image.Resampling.LANCZOS)
        tk_img = ImageTk.PhotoImage(resized_img)
        
        # Update the label with the new image
        label.config(image=tk_img)
        label.image = tk_img


# Set up the Tkinter GUI
root = tk.Tk()
root.title("Scalable Epoch QR Code")

# Set an initial size for the window
root.geometry("300x300")

# Make the window resizable
root.resizable(True, True)

# Add a label to display the QR code
label = tk.Label(root)
label.pack(fill="both", expand=True)

# Bind the resize event to update the QR code size
root.bind("<Configure>", resize_qr)

qr_img = None  # Placeholder for the QR code image

# Start the updating process
update_qr()

# Run the Tkinter event loop
root.mainloop()

