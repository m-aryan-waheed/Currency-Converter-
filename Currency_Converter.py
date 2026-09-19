import tkinter as tk

##########################################################################################

def total_pkr():
    pkr = float(entry_pkr.get() or 0) * 1
    print("PKR: ")
    entry_pk.delete(0, tk.END)
    entry_pk.insert(0, pkr)


def total_usd():
    pkr = float(entry_pkr.get() or 0)
    usd = pkr / 276
    print("USD: ")
    entry_us.delete(0, tk.END)
    entry_us.insert(0, usd)


def total_euro():
    pkr = float(entry_pkr.get() or 0)
    euro = pkr / 319
    print("Euro: ")
    entry_eu.delete(0, tk.END)
    entry_eu.insert(0, euro)


def total_pound():
    pkr = float(entry_pkr.get() or 0)
    pound = pkr / 374
    print("Pound: ")
    entry_pd.delete(0, tk.END)
    entry_pd.insert(0, pound)


def total_sar():
    pkr = float(entry_pkr.get() or 0)
    sar = pkr / 74
    print("SAR: ")
    entry_ksa.delete(0, tk.END)x
    entry_ksa.insert(0, sar)

###########################################################################################

window = tk.Tk()
window.title("Currency Converter")
window.geometry("300x180")

##############################################################################################

label = tk.Label(window, text="PKR          into       Currencies")
label.pack()

#################################################################################################

entry_pkr = tk.Entry(window, width=10) #PKR
entry_pkr.place(x=10, y=20)
entry_pkr.get()

entry_usd = tk.Entry(window, width=10) #USD
entry_usd.place(x=10, y=50)
entry_usd.get()

entry_euro = tk.Entry(window, width=10) #EURO
entry_euro.place(x=10, y=80)
entry_euro.get()

entry_pound = tk.Entry(window, width=10) #POUND
entry_pound.place(x=10, y=110)
entry_pound.get()

entry_sar = tk.Entry(window, width=10) #SAUDI RIYAL
entry_sar.place(x=10, y=140)
entry_sar.get()

################################################################################################

button_pkr = tk.Button(window, text="₨", command=total_pkr)
button_pkr.place(x=110, y=18)

button_usd = tk.Button(window, text="$", command=total_usd)
button_usd.place(x=110, y=48)

button_euro = tk.Button(window, text="€", command=total_euro)
button_euro.place(x=110, y=78)

button_pound = tk.Button(window, text="£", command=total_pound)
button_pound.place(x=110, y=108)

button_sar = tk.Button(window, text="SR", command=total_sar)
button_sar.place(x=100, y=138)

###################################################################################################

entry_pk = tk.Entry(window, width=10) #PKR
entry_pk.place(x=153, y=20)

entry_us = tk.Entry(window, width=10) #USD
entry_us.place(x=153, y=50)

entry_eu = tk.Entry(window, width=10) #EURO
entry_eu.place(x=153, y=80)

entry_pd = tk.Entry(window, width=10) #POUND
entry_pd.place(x=153, y=110)

entry_ksa = tk.Entry(window, width=10) #SAUDI RIYAL
entry_ksa.place(x=153, y=140)
####################################################################################################

window.mainloop()
