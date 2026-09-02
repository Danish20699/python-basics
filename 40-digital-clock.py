import tkinter as tk
from time import strftime

# 1. Function to update time every second
def update_time():
    time_string = strftime('%H:%M:%S %p')
    label.config(text=time_string)
    label.after(1000, update_time)

# 2. Create the Window
window = tk.Tk()
window.title("Digital Clock")

# 3. Create the Time Label
label = tk.Label(window, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(padx=30, pady=30)

# 4. Start the Clock and Event Loop
update_time()
window.mainloop()