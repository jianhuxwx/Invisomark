'''
        <INVISOMARK - Greatest Watermark Software>
        Copyright (C) <2023>  <YuexuChen>

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <https://www.gnu.org/licenses/>.


'''
import customtkinter as ctk  
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import os
import basic_watermark 
import full_watermark
import line  
import metadata
import signature
import blind
import blur
import ipfs
import webbrowser 
import tracepicture  
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import requests
import re
import io

class CollapsiblePane(ctk.CTkFrame):
    def __init__(self, parent, title="", *args, **kwargs):
        super().__init__(parent, *args, **kwargs) 
        self.title = title
        self.toggle_button = ctk.CTkButton(self, text=self.title, command=self.toggle)
        self.toggle_button.pack(fill="x", pady=2)
        self.content_frame = ctk.CTkFrame(self)
        self.content_visible = False

    def toggle(self):
        if self.content_visible:
            self.content_frame.pack_forget()
            self.content_visible = False
        else:
            self.content_frame.pack(fill="x", expand=True)
            self.content_visible = True

    def add_widget(self, widget):
        widget.pack(fill="x", pady=2)
        
# Necessary method definitions

def copy_to_clipboard(text):
    app.clipboard_clear()
    app.clipboard_append(text)
    messagebox.showinfo("Copy succeeded", "Copied to clipboard")
    
# Update sliders  
def update_sliders(event=None):
    red_value_label.configure(text="Red:"+f"{red_slider.get():.0f}")
    green_value_label.configure(text="Green:"+f"{green_slider.get():.0f}")
    blue_value_label.configure(text="Blue:"+f"{blue_slider.get():.0f}")
    alpha_value_label.configure(text="Transparency:"+f"{alpha_slider.get() / 10:.1f}")
    
# Select file  
def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.set(file_path)
        update_output_path(file_path) 
        update_image_preview(file_path)
    else:
        file_entry.set('')
        output_entry.set('')
        
# Update output file path    
def update_output_path(input_path):
    base, ext = os.path.splitext(input_path)
    output_path = base + '_watermarked.png'
    output_entry.set(output_path)
    
# Update instance    
def update_image_preview(file_path):
    try:
        img = Image.open(file_path) 
        img.thumbnail((200, 200))
        img = ImageTk.PhotoImage(img)
        image_label.configure(image=img)
        image_label.image = img
    except Exception as e:
        image_label.configure(image='')
        image_label.text = 'Image preview unavailable'  
        
# Get picture path
def get_working_file():
    original = file_entry.get()
    watermarked = output_entry.get()  
    if os.path.exists(original) or os.path.exists(watermarked):
        return watermarked if os.path.exists(watermarked) else original 
    else:
        return None
        
# Apply watermarks        
def apply_watermarks():
    working_file = get_working_file()
    if not working_file:
        messagebox.showinfo("Tip", "No valid file selected.")
        return
    output_file = output_entry.get()
    
    try:
        # Blind watermark   
        if blind_watermark_check.get():
            watermark_text = watermark_text_entry.get()
            blind_result = blind.embed_watermark(working_file, watermark_text, output_file)
            if isinstance(blind_result, tuple):
                blind_key = blind_result[0] 
                blind_key_label.set(f"Blind watermark key (keep it safe): {blind_key}")
            else:
                blind_key_label.set(f"Blind watermark key (keep it safe): {blind_result}")
            working_file = output_file
        # Linear watermark
        if line_watermark_check.get():  
            input_text = line_text_entry.get()
            font_size = int(font_size_entry.get()) 
            red = int(red_slider.get())
            green = int(green_slider.get())
            blue = int(blue_slider.get())
            alpha = alpha_slider.get() / 10
            font_color = (red, green, blue, int(alpha * 255))  
            line.write_text_along_path(working_file, input_text, output_file, font_size=font_size, font_color=font_color)
        # Full screen watermark 
        if full_watermark_check.get():
            full_watermark_text = full_watermark_text_entry.get()
            full_watermark.add_watermark(working_file, output_file, full_watermark_text) 
        # Basic watermark
        if basic_watermark_check.get():
            basic_watermark_text = watermark_text_entry.get()
            basic_watermark.add_watermark(working_file, output_file, basic_watermark_text)
        # Blur picture
        if blur_watermark_check.get():
            blur_level = int(blur_level_entry.get())
            blur.blur_image(working_file, output_file, blur_level)
        # Metadata    
        if metadata_check.get():
            artist = artist_entry.get()
            software = software_entry.get()
            image = Image.open(working_file)
            metadata.add_metadata(working_file, {'Artist': artist, 'Software': software})
            output_path = os.path.splitext(working_file)[0] + '_watermarked.png'
            image.save(output_path, format='PNG') 
            output_entry.set(output_path) 
        # Digital signature
        if signature_check.get():
            output_path = os.path.splitext(working_file)[0]+ '.pctf'
            key = signature.generate_key_from_string(signature_key_entry.get())
            signature.generate_signature(working_file, key, output_path)
    # Error output      
    except Exception as e:
        messagebox.showerror("Error", f"Error processing watermark: {e}")  
        return

    messagebox.showinfo("Completed", "Watermark processing completed.")

def upload_to_ipfs():
    file_path = file_entry.get()
    if file_path:
        result = ipfs.upload_to_ipfs(file_path) # 
        if result.get('ok') and 'value' in result and 'cid' in result['value']:
            cid = result['value']['cid']
            ipfs_cid.set(f"IPFS CID: {cid}") 
            ipfs_url.set(f"IPFS link: https://ipfs.io/ipfs/{cid}")
        else:
            ipfs_cid.set("Upload failed or invalid return value")
            ipfs_url.set("")
    else:
        messagebox.showinfo("Tip", "No valid file selected.")
        
def extract_watermark_and_metadata():
    file_path = get_working_file()
    if file_path:
        blind_key = blind_key_entry.get()
        wm_length = int(blind_key)
        extracted_wm = blind.extract_watermark(file_path, wm_length)
        extracted_metadata = metadata.read_metadata(file_path)
        watermark_result.set(f"Extracted watermark: {extracted_wm}")
        metadata_result.set(f"Metadata: {extracted_metadata}")
    else:
        messagebox.showinfo("Tip", "No valid file selected.")
        
def verify_signature():
    signature_file = filedialog.askopenfilename(filetypes=[("PCTF Files", "*.pctf")])
    if signature_file:
        picture_path = get_working_file()
        key = verify_key_entry 
        result = signature.verify_signature(picture_path,key,signature_file)
        signature_result.set("Verification succeeded" if result else "Verification failed")
    else:
        messagebox.showinfo("Tip", "No valid digital signature file selected.")

proxy_url = 'http://node.invisomark.keyfox.xyz/serpapi_search.php'
     
def fetch_and_display_sources(api_key, image_url, display_window):
    try:
        page_token = tracepicture.fetch_google_lens_page_token(api_key, image_url)
        image_sources_results = tracepicture.fetch_google_lens_image_sources(api_key, page_token) 

        for source in image_sources_results['image_sources']:
            source_frame = tk.Frame(display_window)
            source_frame.pack(fill='x', expand=True)
           
            logo = ImageTk.PhotoImage(Image.open(requests.get(source['source_logo'], stream=True).raw))
            logo_label = tk.Label(source_frame, image=logo)
            logo_label.image = logo
            logo_label.pack(side='left')
            
            source_label = tk.Label(source_frame, text=source['source'])
            source_label.pack(side='left')

            link_button = tk.Button(source_frame, text="Open link", command=lambda url=source['link']: webbrowser.open(url))
            link_button.pack(side='left')
      
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}") 
                
def fetch_and_display_sources_proxy(api_key, image_url, display_window):
    response = requests.post(proxy_url, data={'api_key': api_key, 'image_url': image_url})  
    response_text = response.text  
    sources = re.findall(r"\[source\] => (.+?)\n", response_text)
    source_logos = re.findall(r"\[source_logo\] => (.+?)\n", response_text)
    links = re.findall(r"\[link\] => (.+?)\n", response_text)

    for source, source_logo, link in zip(sources, source_logos, links):
        source_frame = tk.Frame(display_window) 
        source_frame.pack(fill='x', expand=True)
      
        # Display source logo  
        logo_response = requests.get(source_logo)
        logo_image = Image.open(io.BytesIO(logo_response.content))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(source_frame, image=logo_photo)
        logo_label.image = logo_photo # Keep reference to image
        logo_label.pack(side='left')

        # Display source
        source_label = tk.Label(source_frame, text=source)
        source_label.pack(side='left')
   
        # Display link 
        link_button = tk.Button(source_frame, text="Open link", command=lambda l=link: webbrowser.open(l))
        link_button.pack(side='left')
        
def trace_image(): 
    api_key = api_key_entry.get()  
    image_url = image_url_entry.get()  
    
    if not api_key:
        messagebox.showinfo("Tip", "Please enter API key.")
        return

    if not image_url:
        messagebox.showinfo("Tip", "Please enter image link.")
        return

    try:
        display_window = tk.Toplevel(app)
        display_window.title("Image trace result")
        display_window.geometry("600x400") 
        
        scrollable_frame = tk.Frame(display_window)  
        scrollable_canvas = tk.Canvas(scrollable_frame)
        scrollbar = tk.Scrollbar(scrollable_frame, orient="vertical", command=scrollable_canvas.yview)
        scrollable_frame.pack(fill='both', expand=True)
        scrollable_canvas.pack(side="left", fill="both", expand=True) 
        scrollbar.pack(side="right", fill="y")   

        scrollable_canvas.configure(yscrollcommand=scrollbar.set)
        scrollable_canvas.bind('<Configure>', lambda e: scrollable_canvas.configure(scrollregion=scrollable_canvas.bbox('all'))) 
          
        if use_proxy.get():
            fetch_and_display_sources_proxy(api_key, image_url, scrollable_canvas)
        else:
            fetch_and_display_sources(api_key, image_url, scrollable_canvas)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
         
def show_developer_info():
    developer_info = "Developer information:\nDeveloper: Keyfox \n Github: https://github.com/jianhuxwx/invisomark/ \nThis project is a free open source project. If you paid to purchase this software, please get a refund immediately!"
    messagebox.showinfo("Developer information", developer_info)
        
app = ctk.CTk() 
app.geometry("400x600")
app.title("INVISOMARK by Keyfox")  

left_frame = ctk.CTkFrame(app, width=200, height=600)  
left_frame.pack(side="left", fill="both", expand=True)  

right_frame = ctk.CTkFrame(app, width=200, height=600)
right_frame.pack(side="right", fill="both", expand=True)

image_label = ctk.CTkLabel(left_frame, text="Image preview")  
image_label.pack(pady=10)

file_entry = ctk.StringVar(app)   
output_entry = ctk.StringVar(app)   

choose_file_button = ctk.CTkButton(right_frame, text="Select file", command=choose_file, width=150, height=25)
choose_file_button.pack(pady=5)  

file_label = ctk.CTkLabel(right_frame, textvariable=file_entry)  
file_label.pack(pady=5)   

output_label = ctk.CTkLabel(right_frame, textvariable=output_entry) 
output_label.pack(pady=5)  

# Blind watermark panel
blind_watermark_pane = CollapsiblePane(right_frame, title="Blind watermark")  
blind_watermark_pane.pack(fill="x", pady=2)
blind_watermark_check = ctk.CTkCheckBox(blind_watermark_pane.content_frame, text="Enable blind watermark")
blind_watermark_pane.add_widget(blind_watermark_check) 
watermark_text_entry = ctk.CTkEntry(blind_watermark_pane.content_frame, placeholder_text="Watermark text")  
blind_watermark_pane.add_widget(watermark_text_entry)   
blind_key_label = ctk.StringVar(app)  
blind_key_display = ctk.CTkLabel(blind_watermark_pane.content_frame, textvariable=blind_key_label)
blind_watermark_pane.add_widget(blind_key_display)  

# Linear watermark panel
line_watermark_pane = CollapsiblePane(right_frame, title="Linear watermark") 
line_watermark_pane.pack(fill="x", pady=2)   
line_watermark_check = ctk.CTkCheckBox(line_watermark_pane.content_frame, text="Enable linear watermark")
line_watermark_pane.add_widget(line_watermark_check)
line_text_entry = ctk.CTkEntry(line_watermark_pane.content_frame, placeholder_text="Text for line watermark")  
line_watermark_pane.add_widget(line_text_entry) 
font_size_entry = ctk.CTkEntry(line_watermark_pane.content_frame, placeholder_text="Font size")  
line_watermark_pane.add_widget(font_size_entry) 
red_slider = ctk.CTkSlider(line_watermark_pane.content_frame, from_=0, to=255, command=update_sliders)
line_watermark_pane.add_widget(red_slider)
green_slider = ctk.CTkSlider(line_watermark_pane.content_frame, from_=0, to=255, command=update_sliders)
line_watermark_pane.add_widget(green_slider)
blue_slider = ctk.CTkSlider(line_watermark_pane.content_frame, from_=0, to=255, command=update_sliders) 
line_watermark_pane.add_widget(blue_slider)
alpha_slider = ctk.CTkSlider(line_watermark_pane.content_frame, from_=0, to=10, command=update_sliders)
line_watermark_pane.add_widget(alpha_slider)
red_value_label = ctk.CTkLabel(line_watermark_pane.content_frame, text="0")  
line_watermark_pane.add_widget(red_value_label)
green_value_label = ctk.CTkLabel(line_watermark_pane.content_frame, text="0")
line_watermark_pane.add_widget(green_value_label)
blue_value_label = ctk.CTkLabel(line_watermark_pane.content_frame, text="0")
line_watermark_pane.add_widget(blue_value_label)
alpha_value_label = ctk.CTkLabel(line_watermark_pane.content_frame, text="0.0")
line_watermark_pane.add_widget(alpha_value_label)

# Full screen watermark panel 
full_watermark_pane = CollapsiblePane(right_frame, title="Full screen watermark")    
full_watermark_pane.pack(fill="x", pady=2)  
full_watermark_check = ctk.CTkCheckBox(full_watermark_pane.content_frame, text="Enable full screen watermark")  
full_watermark_pane.add_widget(full_watermark_check)
full_watermark_text_entry = ctk.CTkEntry(full_watermark_pane.content_frame, placeholder_text="Full screen watermark text")
full_watermark_pane.add_widget(full_watermark_text_entry)  

# Basic watermark panel
basic_watermark_pane = CollapsiblePane(right_frame, title="Basic watermark")
basic_watermark_pane.pack(fill="x", pady=2)   
basic_watermark_check = ctk.CTkCheckBox(basic_watermark_pane.content_frame, text="Enable basic watermark")
basic_watermark_pane.add_widget(basic_watermark_check)

# Blur watermark panel  
blur_watermark_pane = CollapsiblePane(right_frame, title="Blur watermark")
blur_watermark_pane.pack(fill="x", pady=2)  
blur_watermark_check = ctk.CTkCheckBox(blur_watermark_pane.content_frame, text="Enable blur watermark") 
blur_watermark_pane.add_widget(blur_watermark_check)
blur_level_entry = ctk.CTkEntry(blur_watermark_pane.content_frame, placeholder_text="Blur level")
blur_watermark_pane.add_widget(blur_level_entry)

# Metadata panel
metadata_pane = CollapsiblePane(right_frame, title="Metadata")  
metadata_pane.pack(fill="x", pady=2)
metadata_check = ctk.CTkCheckBox(metadata_pane.content_frame, text="Enable metadata")  
metadata_pane.add_widget(metadata_check) 
artist_entry = ctk.CTkEntry(metadata_pane.content_frame, placeholder_text="Artist name")  
metadata_pane.add_widget(artist_entry)  
software_entry = ctk.CTkEntry(metadata_pane.content_frame, placeholder_text="Software name")
metadata_pane.add_widget(software_entry)   

# Digital signature panel  
signature_pane = CollapsiblePane(right_frame, title="Digital signature")
signature_pane.pack(fill="x", pady=2)
signature_check = ctk.CTkCheckBox(signature_pane.content_frame, text="Enable digital signature")
signature_pane.add_widget(signature_check)  
signature_key_entry = ctk.CTkEntry(signature_pane.content_frame, placeholder_text="Digital signature key")  
signature_pane.add_widget(signature_key_entry)

# Verification panel
verification_pane = CollapsiblePane(right_frame, title="Verification") 
verification_pane.pack(fill="x", pady=2)  

ipfs_cid = ctk.StringVar(app)   
ipfs_url = ctk.StringVar(app)
watermark_result = ctk.StringVar(app)
metadata_result = ctk.StringVar(app)
signature_result = ctk.StringVar(app)
upload_to_ipfs_button = ctk.CTkButton(verification_pane.content_frame, text="Upload to IPFS", command=upload_to_ipfs, width=150, height=25)
upload_to_ipfs_button.pack(pady=5)
# Add button to copy CID in UI 
copy_cid_button = ctk.CTkButton(verification_pane.content_frame, text="Copy CID", command=lambda: copy_to_clipboard(ipfs_cid.get()))  
copy_cid_button.pack(pady=5)  
ipfs_cid_label = ctk.CTkLabel(verification_pane.content_frame, textvariable=ipfs_cid)
# Add button to copy CID link in UI
copy_cid_url_button = ctk.CTkButton(verification_pane.content_frame, text="Copy CID link", command=lambda: copy_to_clipboard(ipfs_url.get()))
copy_cid_url_button.pack(pady=5) 
ipfs_cid_label.pack(pady=5)
ipfs_url_label = ctk.CTkLabel(verification_pane.content_frame, textvariable=ipfs_url)
ipfs_url_label.pack(pady=5)  

blind_key_entry = ctk.CTkEntry(verification_pane.content_frame, placeholder_text="Please enter blind watermark key")  
blind_key_entry.pack(pady=5)
extract_wm_button = ctk.CTkButton(verification_pane.content_frame, text="Extract watermark and metadata", command=extract_watermark_and_metadata, width=150, height=25) 
extract_wm_button.pack(pady=5)
watermark_result_label = ctk.CTkLabel(verification_pane.content_frame, textvariable=watermark_result)  
watermark_result_label.pack(pady=5)
metadata_result_label = ctk.CTkLabel(verification_pane.content_frame, textvariable=metadata_result) 
metadata_result_label.pack(pady=5)   

verify_key_entry = ctk.CTkEntry(verification_pane.content_frame, placeholder_text="Please enter verification key")
verify_key_entry.pack(pady=5) 
verify_signature_button = ctk.CTkButton(verification_pane.content_frame, text="Verify digital signature", command=verify_signature, width=150, height=25)  
verify_signature_button.pack(pady=5)
signature_result_label = ctk.CTkLabel(verification_pane.content_frame, textvariable=signature_result)
signature_result_label.pack(pady=5)  

# Image trace panel 
trace_pane = CollapsiblePane(right_frame, title="Image trace")
use_proxy = tk.BooleanVar(value=False) 
proxy_checkbutton = ctk.CTkCheckBox(trace_pane.content_frame, text="Use proxy server", variable=use_proxy)  
proxy_checkbutton.pack(pady=5)
trace_pane.pack(fill="x", pady=2)
api_key_entry = ctk.CTkEntry(trace_pane.content_frame, placeholder_text="Please enter your API key")  
api_key_entry.pack(pady=5)
image_url_entry = ctk.CTkEntry(trace_pane.content_frame, placeholder_text="Enter image link")
image_url_entry.pack(pady=5)
trace_button = ctk.CTkButton(trace_pane.content_frame, text="Image trace", command=trace_image)
trace_button.pack(pady=5) 

developer_info_button = ctk.CTkButton(left_frame, text="Show developer info", command=show_developer_info) 
developer_info_button.pack(pady=5)  

# Apply watermarks panel
apply_watermarks_button = ctk.CTkButton(right_frame, text="Apply watermarks", command=apply_watermarks, width=150, height=25)  
apply_watermarks_button.pack(pady=10)  

app.mainloop()
