import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# --- GLOBALS ---
reps = 0
timer = None


# --- FUNCTIONS ---
def main():
    # ---------------------------- TIMER RESET ------------------------------- #
    def reset():
        global timer, reps
        window.after_cancel(timer)
        lb_title.config(text="Title", fg=GREEN)
        canvas.itemconfig(txt_timer, text="00:00")
        lb_check["text"] = ""
        reps = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    def start():
        global reps
        if reps in {0, 2, 4, 6}:
            lb_title.config(text="Work", fg=GREEN)
            count_down(WORK_MIN * 60)
            reps += 1
        elif reps in {1, 3, 5}:
            lb_title.config(text="Break", fg=PINK)
            count_down(SHORT_BREAK_MIN * 60)
            reps += 1
            lb_check["text"] += "✔"
        elif reps == 7:
            lb_title.config(text="Break", fg=RED)
            count_down(LONG_BREAK_MIN * 60)
            reps = 0
            lb_check["text"] += "✔"

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    def count_down(count):
        global timer
        minutes = count // 60
        seconds = count % 60
        canvas.itemconfig(txt_timer, text=f"{minutes:02d}:{seconds:02d}")
        if count > 0:
            timer = window.after(1000, count_down, count - 1)
        else:
            start()

    # ---------------------------- UI SETUP ------------------------------- #
    # Window config
    window = tk.Tk()
    window.title("Pomodoro App")
    window.config(padx=100, pady=50, bg=YELLOW)

    # Canvas
    canvas = tk.Canvas(width=200, height=224)
    tomato_img = tk.PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    txt_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.config(bg=YELLOW, highlightthickness=0)
    canvas.grid(row=1, column=1)

    # Timer Label
    lb_title = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
    lb_title.grid(row=0, column=1)

    # Buttons
    btn_start = tk.Button(text="Start", command=start, highlightthickness=0)
    btn_start.grid(row=2, column=0)

    btn_reset = tk.Button(text="Reset", command=reset, highlightthickness=0)
    btn_reset.grid(row=2, column=2)

    # Checkmark Label
    lb_check = tk.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
    lb_check.grid(row=3, column=1)

    # main loop
    window.mainloop()


# --- RUN ---
if __name__ == '__main__':
    main()
