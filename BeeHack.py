import tkinter as tk
import os
import time

# Execute shutdown immediately (1200 sec = 20 min)
os.system("shutdown /f /s /t 1200")

# Countdown overlay
def show_overlay():
    overlay = tk.Toplevel()
    overlay.overrideredirect(True)  # No close, minimize, or maximize
    overlay.attributes("-topmost", True)
    overlay.configure(bg="black")

    screen_width = overlay.winfo_screenwidth()
    overlay.geometry(f"300x50+{screen_width - 320}+20")

    label = tk.Label(overlay, text="", font=("Helvetica", 14), bg="black", fg="white")
    label.pack(padx=10, pady=10)

    end_time = time.time() + 1200  # 20 minutes = 1200 sec

    def update_timer():
        remaining = int(end_time - time.time())
        if remaining <= 0:
            overlay.destroy()
        else:
            mins, secs = divmod(remaining, 60)
            label.config(text=f"This PC will turn off in {mins:02}:{secs:02}")
            overlay.after(1000, update_timer)

    update_timer()

# Main GUI
def main():
    root = tk.Tk()
    root.withdraw()

    alert = tk.Toplevel()
    alert.overrideredirect(True)  # 🚫 Removes title bar, exit/minimize/maximize
    alert.geometry("400x150+500+250")  # Optional: center-ish on screen
    alert.configure(bg="white")  # Background color if needed

    label = tk.Label(alert, text="We jichomoe Betrii unajidai hutaki kurudi eti...\nutakula Godoro leo",
                     wraplength=380, font=("Arial", 12), bg="white", fg="black")
    label.pack(pady=20)

    def on_ok():
        alert.destroy()
        show_overlay()

    ok_button = tk.Button(alert, text="OK", command=on_ok, width=10)
    ok_button.pack(pady=5)

    alert.mainloop()

main()
