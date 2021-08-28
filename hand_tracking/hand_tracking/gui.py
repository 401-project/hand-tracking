import tkinter
from PIL import ImageTk, Image

# Create object
root = tkinter.Tk()

# Adjust size
root.geometry("800x500")

# Add image file
# bg = tkinter.PhotoImage(file="5.png")
# my_img=ImageTk.PhotoImage(Image.open("5.png"))

# Show image using label
# label1 = tkinter.Label(root, image=my_img)
# label1.place(x=0, y=0)
# label1.pack()
bg = ImageTk.PhotoImage(file="5.png")

# Create a Canvas
canvas = tkinter.Canvas(root, width=700, height=3500)
canvas.pack(fill="both", expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

# Function to resize the window
def resize_image(e):
   global image, resized, image2
   # open image to resize it
   image = Image.open("5.png")
   # resize the image with width and height of root
   resized = image.resize((e.width, e.height), Image.ANTIALIAS)

   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

# # Bind the function to configure the parent window
root.bind("<Configure>", resize_image)

def main():
   print("x")
draw_button = tkinter.Button(root, text="draw", command=main)
button1_window = canvas.create_window(30,30, anchor="nw", window=draw_button)
# # button1_window.grid(row=10,column=10)
draw_button.place(relx=0.5, rely=0.9)
# # draw_button.pack()
root.mainloop()