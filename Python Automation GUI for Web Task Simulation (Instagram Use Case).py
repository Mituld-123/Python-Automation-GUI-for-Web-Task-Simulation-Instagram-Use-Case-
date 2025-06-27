import customtkinter as ctk
import pyautogui as pg
import time as t
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")  

app = ctk.CTk()
app.title("📱 Instagram Reel Liker Bot")
app.geometry("500x400")
app.resizable(False, False)

stop_flag = False

#Functions 
def start_bot():
    global stop_flag
    stop_flag = False
    try:
        reels_count = int(entry_reels.get())
        if reels_count <= 0:
            label_status.configure(text="⚠️ Enter a positive number.")
            return
    except:
        label_status.configure(text="⚠️ Enter a valid number.")
        return

    def run_bot():
        progress_bar.set(0)
        t.sleep(1)
        pg.press("win")
        t.sleep(1)
        pg.write("chrome")
        t.sleep(1)
        pg.press("enter")
        t.sleep(3)
        pg.write("https://www.instagram.com/reels")
        pg.press("enter")
        t.sleep(8)

        for i in range(reels_count):
            if stop_flag:
                break
            pg.click(1341, 590)
            pg.click(1341, 590)
            t.sleep(2)
            pg.scroll(-500)
            t.sleep(2)
            progress_bar.set((i+1)/reels_count)

        label_status.configure(text="✅ Finished processing reels.")

    threading.Thread(target=run_bot).start()

def stop_bot():
    global stop_flag
    stop_flag = True
    label_status.configure(text="⏹️ Bot stopped by user.")

# UI Layout
frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

label_title = ctk.CTkLabel(frame, text="Instagram Reel Liker Bot 🤖", font=("Arial", 22, "bold"))
label_title.pack(pady=(10, 5))

label_sub = ctk.CTkLabel(frame, text="Automate Instagram Reel Likes using Python & UI", font=("Arial", 12))
label_sub.pack(pady=(0, 15))

entry_reels = ctk.CTkEntry(frame, placeholder_text="Enter number of reels to like", width=250, height=35)
entry_reels.pack(pady=10)

btn_start = ctk.CTkButton(frame, text="▶️ Start", command=start_bot, width=120)
btn_start.pack(pady=5)

btn_stop = ctk.CTkButton(frame, text="⏹️ Stop", command=stop_bot, width=120)
btn_stop.pack(pady=5)

progress_bar = ctk.CTkProgressBar(frame, width=300)
progress_bar.set(0)
progress_bar.pack(pady=15)

label_status = ctk.CTkLabel(frame, text="", text_color="white")
label_status.pack(pady=10)

# Run App 
app.mainloop()