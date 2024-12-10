import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip


#kısaltan fonksiyonumuz
def shorten_url():
    long_url = entry.get()
    #api
    response = requests.get(f'http://tinyurl.com/api-create.php?url={long_url}')
    #kısalttığımız linki bize text olarak verecek
    short_url = response.text
    result_label.config(text=f"Kısaltılmış link:{short_url}")

    ##veriyi kopyalama yeri
    copy_button.config(state=tk.NORMAL)

def copy_to_clipboard():
    #veri bzim belirttiğmiz yerden sonra alacak 11. haneden sonra alıcak
    short_url = result_label.cget("text")[17:]
    pyperclip.copy(short_url) #pypyerclip ile panoya kopyalıyoruz
    messagebox.showinfo("kopyalandı","kısa URL kopyalandı")



#tkinter alanı

app = tk.Tk()
app.title = ("Link Kısaltıcı")

#uzun adreslerin girileceği yer

label = tk.Label(app, text="Uzun Linki Giriniz:")
label.pack(pady=10)
#link girirlecek yer 
entry = tk.Entry(app, width=40)
entry.pack()

#url kısaltma düğmesi
shorten_button = tk.Button(app, text="kısalt", command=shorten_url)
shorten_button.pack()

#kısa urlnin görüneceği yer
result_label = tk.Label(app, text="")
result_label.pack()

#kopyala butonu

copy_button = tk.Button(app, text="kopyala", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack()

app.mainloop()