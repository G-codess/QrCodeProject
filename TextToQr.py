# IMPORTING NECCESSARY MODULES

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import qrcode
import sys

class MyQrCode():
    
    def __init__(self):
        
        # INITIALIZE WINDOW
        self.window = tk.Tk()
        self.window.title("TTQR IMAGE")
        self.window.geometry("400x300")
        self.window.configure(bg='LightSteelBlue4')
        self.window.resizable(True,True)
        
        # USER TEXT AND LABEL
        self.user_label = tk.Label(self.window,text="ENTER TEXT TO CONVERT QR : ",bg='LightSteelBlue4',fg='white',font=("Lucida Fax", "14"))
        self.user_label.grid(row=1,column=1,padx=20,pady=10)
        self.user_entry = tk.Entry(self.window,bg='white')
        self.user_entry.configure(font=("Arial", 14), width=30)
        self.user_entry.grid(row=1, column=2,padx=20,pady=10)
        
        # GENERATE QR CODE BUTTON
        self.qr_button = tk.Button(self.window, text='GENERATE QR IMAGE',font=("Lucida Fax", "14"),command=self.generate_QR)
        self.qr_button.grid(row=2, column=2, padx=20,pady=10)
        
        # DEFINE VARIABLES TO CHECK
        self.error_label = None
        self.image_label = None
        self.image_entry = None
        
        # SAVE AND EXIT BUTTON FUNCTION
    def buttons(self):
        
        # SAVE BUTTON
        self.save_button = tk.Button(self.window, text='SAVE',font=("Lucida Fax", "14"),command = self.save_image)
        self.save_button.grid(row=5, column=2, padx=20,pady=10)
        
        # EXIT BUTTON
        self.qr_button = tk.Button(self.window, text='EXIT',font=("Lucida Fax", "14"),command = self.exit)
        self.qr_button.grid(row=5, column=3, padx=20,pady=10)
      
    # QR CODE GENERATE FUNCTION
    def generate_QR(self):
        
        # QR CODE CONFIGURATION
        qr = qrcode.QRCode(version=1 ,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        try:
            user_data = self.user_entry.get()
            if not user_data:
                if self.error_label:
                    self.error_label.destroy()
                raise ValueError
        except:
            self.error_label = tk.Label(self.window, text="PLEASE ENTER A TEXT!!!",font=("Lucida Fax", "14"))
            self.error_label.grid(row=3, column=2, padx=20, pady=10)
        else:
            if self.error_label:
                # REMOVE PREVIOUS ERROR LABEL IF IT EXISTS
                self.error_label.destroy()
                
            # ADD DATA TO QR CODE
            qr.add_data(user_data)
            qr.make(fit=True)
            self.qr_image = qr.make_image(fill_color='black', back_color='white')
            
            if self.image_label:
                # REMOVE PREVIOUS IMAGE LABEL IF IT EXISTS
                self.image_label.destroy()
                
            # QR CODE LABEL
            self.image_label = tk.Label(self.window, text="QR IMAGE",font=("Lucida Fax", "14"))
            self.image_label.grid(row=3, column=2, padx=20, pady=10)
            
            if self.image_entry:
                # REMOVE PREVIOUS IMAGE ENTRY IF IT EXISTS
                self.image_entry.destroy() 
                
            # FIT PHOTO IMAGE OF QR CODE
            self.Qr_image = ImageTk.PhotoImage(self.qr_image)
            
            # QR CODE ENTRY
            self.image_entry = ttk.Label(self.window,text='QR IMAGE',background='black',foreground ='white',image=self.Qr_image)
            self.image_entry.image = self.Qr_image
            self.image_entry.grid(row=4, column=2, columnspan=2, padx=20, pady=10)
            
            # CALLING BUTTONS FUNCTION AFTER DISPLAYING QR IMAGE
            self.buttons()
    
    # SAVING QR IMAGE FUNCTION
    def save_image(self):
        self.qr_image.save("QRCODEIMAGE.png")
        
        # SAVED MESSAGE LABEL
        self.final_image = tk.Label(self.window, text="IMAGE HAS SUCCESSFULLY SAVED!!!",font=("Lucida Fax", "14"))
        self.final_image.grid(row=6, column=2, padx=20, pady=10)
        
    # EXIT FUNCTION 
    def exit(self):
        sys.exit()
        
    # THIS FUNCTION IS TO START THIS EVENT
    def run(self):
        self.window.mainloop()



QRProject = MyQrCode()
QRProject.run()