import tkinter as tk
from PIL import Image, ImageDraw, ImageTk, ImageGrab
import subprocess

class ScreenSnipper(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes("-fullscreen", True)
        self.overrideredirect(True)  # Remove window decorations
        self.wait_visibility(self)  # Wait for the window to be visible
        self.attributes("-alpha", 0.2)  # Set window transparency (0.0 to 1.0)
        self.attributes('-toolwindow', False)
        self.config(cursor="crosshair")

        # Create a transparent image as the overlay background
        self.overlay_image = Image.new("RGBA", (self.winfo_screenwidth(), self.winfo_screenheight()), (0, 0, 0, 0))
        self.overlay_draw = ImageDraw.Draw(self.overlay_image)

        # Bind Shift key events to handle multiple rectangles
        self.bind("<Control_L>", self.on_ctrl_press)
        self.bind("<Control_R>", self.on_ctrl_press)
        self.bind("<KeyRelease-Control_L>", self.on_ctrl_release)  # For left Control key release
        self.bind("<KeyRelease-Control_R>", self.on_ctrl_release)  # For right Control key release

        # Bind mouse events
        self.bind("<ButtonPress-1>", self.start_rect)
        self.bind("<B1-Motion>", self.draw_rect)
        self.bind("<ButtonRelease-1>", self.end_rect)

        # Enter for multiple snip
        self.bind("<Return>", self.on_enter)

        # on FocusOut events destroy app
        self.bind("<FocusOut>", self.destroy_app)

        # stores snips
        self.snips = []

        # Variables to store rectangle coordinates
        self.rect_start_x = None
        self.rect_start_y = None
        self.rect_end_x = None
        self.rect_end_y = None

        # Create a label with the transparent overlay image
        self.overlay_label = tk.Label(self, image="", bg="black", bd=0, highlightthickness=0)
        self.overlay_label.pack(fill=tk.BOTH, expand=True)

        # rectangle coords
        self.selections  = []
        self.enable_multiple_selection = False

        # Aspect ratio correction for mapping screenshot with tkinter coords
        self.wf = None
        self.hf = None
        self.aspectratio()

        # Auto Output ON/OFF (If cmd then save at end)
        self.cmdMode = False

        # Update the overlay image on the label
        self.update_overlay()

    def start_rect(self, event):
        self.rect_start_x = event.x
        self.rect_start_y = event.y

        if not self.enable_multiple_selection:
            self.clear_selection()

    def draw_rect(self, event):
        if self.rect_start_x is not None and self.rect_start_y is not None:
            self.rect_end_x = event.x
            self.rect_end_y = event.y
            self.update_overlay()

    def end_rect(self, event):
        # Perform any actions needed after drawing the rectangle
        # For this example, we'll just reset the rectangle coordinates
        self.update_overlay()
        # self.print_coordinates()

        if self.rect_start_x is not None and self.rect_start_y is not None and self.rect_end_x is not None and self.rect_end_y is not None:
            # Sort the x and y coordinates separately to ensure correct rectangle drawing
            x0, x1 = sorted([self.rect_start_x, self.rect_end_x])
            y0, y1 = sorted([self.rect_start_y, self.rect_end_y])

            self.selections.append((x0, y0, x1, y1))

            # is single snip just give output
            if not self.enable_multiple_selection:
                self.capture()
        
        # clear variables
        self.rect_start_x = None
        self.rect_start_y = None
        self.rect_end_x = None
        self.rect_end_y = None

        # print("selections", self.selections)
    
    def on_ctrl_press(self, event):
        self.enable_multiple_selection = True

    def on_ctrl_release(self, event):
        self.enable_multiple_selection = False
    
    def clear_selection(self):
        self.overlay_draw.rectangle((0, 0, self.winfo_screenwidth(), self.winfo_screenheight()), fill=(0, 0, 0, 0))
        self.selections = []
    
    def destroy_app(self, event):
        self.destroy()

    def update_overlay(self):
        # Get the overlay window position (x, y)
        overlay_x = self.winfo_x()
        overlay_y = self.winfo_y()

        # clears the canvas before draw
        if not self.enable_multiple_selection:
            self.clear_selection()
        
        if self.rect_start_x is not None and self.rect_start_y is not None and self.rect_end_x is not None and self.rect_end_y is not None:
            # Sort the x and y coordinates separately to ensure correct rectangle drawing
            x0, x1 = sorted([self.rect_start_x, self.rect_end_x])
            y0, y1 = sorted([self.rect_start_y, self.rect_end_y])

            # Adjust coordinates based on the overlay window position
            x0 += overlay_x
            x1 += overlay_x
            y0 += overlay_y
            y1 += overlay_y
            
            self.overlay_draw.rectangle((x0, y0, x1, y1), outline=(0,0,255), fill=(255, 255, 255, 255), width=2)

        # Convert the transparent image to a PhotoImage for display on the Label
        image_tk = ImageTk.PhotoImage(self.overlay_image)
        self.overlay_label.configure(image=image_tk)
        self.overlay_label.image = image_tk

    def on_configure(self, event):
        # When the window is resized or moved, update the overlay
        self.update_overlay()
    
    def hide_app(self):
        if not self.enable_multiple_selection:
            self.withdraw()
    
    def aspectratio(self):
        img = ImageGrab.grab()
        current_width, current_height = img.size
        new_width, new_height = (self.winfo_screenwidth(), self.winfo_screenheight())

        self.hf = current_height / new_height
        self.wf = current_width / new_width
    
    def on_enter(self, event):
        self.capture()

    def capture(self):
        self.hide_app()

        for coords in self.selections:
            bbox = (coords[0]*self.wf, coords[1]*self.hf, coords[2]*self.wf, coords[3]*self.hf)
            img = ImageGrab.grab(bbox)

            self.snips.append(img)
        
        if self.cmdMode:
            self.save_snips()

        # return self.snips
        self.destroy()

    def save_snips(self):
        j = 0
        for i in self.snips:
            if len(self.snips) < 2:
                i.save('output.png')
            else:
                # print('saving : output_'+str(j)+'.png')
                i.save('output_'+str(j)+'.png')
                j += 1
        self.snips = []
        
    def snip(self):
        self.mainloop()
        return self.snips

if __name__ == "__main__":
    app = ScreenSnipper()
    app.cmdMode = True
    app.mainloop()
