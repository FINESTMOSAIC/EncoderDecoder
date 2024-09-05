import tkinter as tk
from tkinter import StringVar, ttk
import base64

# Function to encode the message
def encode_message():
    encoding_type = encoding_var.get()
    message = input_text.get("1.0", "end-1c")

    if encoding_type and message:
        if encoding_type == "Base64":
            encoded_message = base64.b64encode(message.encode()).decode()
        elif encoding_type == "Caesar Cipher":
            shift = 3  # You can change the shift value as needed
            encoded_message = caesar_cipher_encode(message, shift)
        else:
            encoded_message = message.encode(encoding_type,'replace')
            encoded_message=base64.b64encode(encoded_message).decode()

        output_text.delete("1.0", "end")
        output_text.insert("1.0", encoded_message)

# Function to decode the message
def decode_message():
    encoding_type = encoding_var.get()
    encoded_message = input_text.get("1.0", "end-1c")

    if encoding_type and encoded_message:
        if encoding_type == "Base64":
            decoded_message = base64.b64decode(encoded_message).decode(errors='replace')
        elif encoding_type == "Caesar Cipher":
            shift = 3  # You can change the shift value as needed
            decoded_message = caesar_cipher_decode(encoded_message, shift)
        else:
            decoded_message = base64.b64decode(encoded_message).decode(encoding_type, errors='replace')

        output_text.delete("1.0", "end")
        output_text.insert("1.0", decoded_message)

# Caesar Cipher functions
def caesar_cipher_encode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_cipher_decode(text, shift):
    return caesar_cipher_encode(text, -shift)

# GUI setup
root = tk.Tk()
root.title("Encoder_Decoder")

# Set the window size and position it in the center of the screen
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Set the window icon
root.iconbitmap("icon.ico")  # Replace "icon.ico" with the path to your icon file

# # Load an image for decoration
image_path = "bg6.png"  # Replace with the path to your image file
image = tk.PhotoImage(file=image_path)
background_label = tk.Label(root, image=image)
background_label.place(relwidth=1, relheight=1)

# Create input text box
input_text = tk.Text(root, wrap=tk.WORD, width=40, height=5)
input_text.place(relx=0.5, rely=0.1, anchor="n")

# Create dropdown for encoding types
encoding_var = StringVar()
encoding_var.set("UTF-8")  # Default encoding type
encoding_dropdown = ttk.Combobox(root, textvariable=encoding_var, values=["UTF-8", "UTF-16", "UTF-32", "Base64", "Caesar Cipher"])
encoding_dropdown.place(relx=0.5, rely=0.46, anchor="n")

# Create Encode button
encode_button = tk.Button(root, text="Encode", command=encode_message)
encode_button.place(relx=0.3, rely=0.45, anchor="n")

# Create Decode button
decode_button = tk.Button(root, text="Decode", command=decode_message)
decode_button.place(relx=0.7, rely=0.45, anchor="n")

# Create output text box
output_text = tk.Text(root, wrap=tk.WORD, width=40, height=5)
output_text.place(relx=0.5, rely=0.7, anchor="n")

# Start the Tkinter event loop
root.mainloop()
