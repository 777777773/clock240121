import tkinter as tk
from datetime import datetime, timedelta

class FocusClock:
    def __init__(self, master):
        self.master = master
        self.master.title("专注时钟")
        self.master.geometry("400x200")
        
        self.remaining_time = timedelta(minutes=25)
        self.is_running = False

        self.label = tk.Label(self.master, text=self.format_time())
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.master, text="开始", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="停止", command=self.stop_timer)
        self.stop_button.pack(pady=10)
        self.stop_button["state"] = "disabled"

    def format_time(self):
        minutes, seconds = divmod(self.remaining_time.seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def update_timer(self):
        if self.remaining_time > timedelta(seconds=0):
            self.remaining_time -= timedelta(seconds=1)
            self.label["text"] = self.format_time()
            self.master.after(1000, self.update_timer)
        else:
            self.is_running = False
            self.start_button["state"] = "normal"
            self.stop_button["state"] = "disabled"

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button["state"] = "disabled"
            self.stop_button["state"] = "normal"
            self.update_timer()

    def stop_timer(self):
        self.is_running = False
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"
        self.remaining_time = timedelta(minutes=25)
        self.label["text"] = self.format_time()

if __name__ == "__main__":
    root = tk.Tk()
    focus_clock = FocusClock(root)
    root.mainloop()
