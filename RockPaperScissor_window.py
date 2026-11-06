import random
import tkinter as tk
from tkinter import font as tkfont

import figures

CHOICES = ("Rock", "Paper", "Scissor")
WIN = {(0, 2), (1, 0), (2, 1)}


class RockPaperScissor:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissor")
        self.root.minsize(640, 480)
        self.root.configure(bg="#1e2430")

        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.started = False

        self.title_font = tkfont.Font(family="DejaVu Sans", size=22, weight="bold")
        self.body_font = tkfont.Font(family="DejaVu Sans", size=12)
        self.figure_font = tkfont.Font(family="DejaVu Sans Mono", size=11)
        self.result_font = tkfont.Font(family="DejaVu Sans", size=16, weight="bold")

        self.container = tk.Frame(root, bg="#1e2430", padx=24, pady=20)
        self.container.pack(fill="both", expand=True)

        self._build_welcome()

    def _clear(self):
        for child in self.container.winfo_children():
            child.destroy()

    def _build_welcome(self):
        self._clear()
        self.started = False

        tk.Label(
            self.container,
            text="Rock Paper Scissor",
            font=self.title_font,
            bg="#1e2430",
            fg="#f4f7fb",
        ).pack(pady=(12, 8))

        tk.Label(
            self.container,
            text="What's your name?",
            font=self.body_font,
            bg="#1e2430",
            fg="#c5d0de",
        ).pack(pady=(24, 8))

        self.name_var = tk.StringVar()
        entry = tk.Entry(
            self.container,
            textvariable=self.name_var,
            font=self.body_font,
            width=28,
            justify="center",
            bg="#2b3344",
            fg="#f4f7fb",
            insertbackground="#f4f7fb",
            relief="flat",
        )
        entry.pack(ipady=6)
        entry.focus_set()
        entry.bind("<Return>", lambda _event: self._start())

        self.welcome_message = tk.StringVar()
        tk.Label(
            self.container,
            textvariable=self.welcome_message,
            font=self.body_font,
            bg="#1e2430",
            fg="#f0a07a",
        ).pack(pady=(10, 0))

        tk.Button(
            self.container,
            text="I'm ready",
            font=self.body_font,
            command=self._start,
            bg="#3d8bfd",
            fg="#ffffff",
            activebackground="#2f74d8",
            activeforeground="#ffffff",
            relief="flat",
            padx=16,
            pady=8,
            cursor="hand2",
        ).pack(pady=24)

    def _start(self):
        name = self.name_var.get().strip()
        if not name:
            self.welcome_message.set("Please enter your name.")
            return
        self.username = name.capitalize()
        self.wins = self.losses = self.draws = 0
        self._build_game()

    def _build_game(self):
        self._clear()
        self.started = True

        header = tk.Frame(self.container, bg="#1e2430")
        header.pack(fill="x")

        tk.Label(
            header,
            text=f"Hello {self.username}!",
            font=self.title_font,
            bg="#1e2430",
            fg="#f4f7fb",
        ).pack(side="left")

        tk.Button(
            header,
            text="Quit",
            font=self.body_font,
            command=self.root.destroy,
            bg="#3a4254",
            fg="#f4f7fb",
            activebackground="#4a5568",
            activeforeground="#f4f7fb",
            relief="flat",
            padx=12,
            pady=4,
            cursor="hand2",
        ).pack(side="right")

        tk.Label(
            self.container,
            text="Choose rock, paper, or scissor.",
            font=self.body_font,
            bg="#1e2430",
            fg="#c5d0de",
        ).pack(anchor="w", pady=(8, 16))

        buttons = tk.Frame(self.container, bg="#1e2430")
        buttons.pack(fill="x")
        for index, label in enumerate(CHOICES):
            tk.Button(
                buttons,
                text=label,
                font=self.body_font,
                command=lambda choice=index: self._play(choice),
                bg="#3d8bfd",
                fg="#ffffff",
                activebackground="#2f74d8",
                activeforeground="#ffffff",
                relief="flat",
                padx=18,
                pady=8,
                cursor="hand2",
            ).pack(side="left", padx=(0, 10))

        board = tk.Frame(self.container, bg="#1e2430")
        board.pack(fill="both", expand=True, pady=18)
        board.columnconfigure(0, weight=1)
        board.columnconfigure(1, weight=1)

        self.player_figure = self._figure_panel(board, self.username, 0)
        self.computer_figure = self._figure_panel(board, "Computer", 1)

        self.result_var = tk.StringVar(value="Make your choice.")
        self.result_label = tk.Label(
            self.container,
            textvariable=self.result_var,
            font=self.result_font,
            bg="#1e2430",
            fg="#f4f7fb",
        )
        self.result_label.pack(pady=(0, 8))

        self.score_var = tk.StringVar()
        self._update_score()
        tk.Label(
            self.container,
            textvariable=self.score_var,
            font=self.body_font,
            bg="#1e2430",
            fg="#c5d0de",
        ).pack()

    def _figure_panel(self, parent, title, column):
        frame = tk.Frame(parent, bg="#2b3344", padx=12, pady=10)
        frame.grid(row=0, column=column, sticky="nsew", padx=6)
        tk.Label(
            frame,
            text=title,
            font=self.body_font,
            bg="#2b3344",
            fg="#9ec1ff",
        ).pack(anchor="w")
        art = tk.Label(
            frame,
            text="",
            font=self.figure_font,
            bg="#2b3344",
            fg="#f4f7fb",
            justify="left",
            anchor="nw",
        )
        art.pack(fill="both", expand=True, pady=(8, 0))
        return art

    def _play(self, choice):
        computer = random.randint(0, 2)
        self.player_figure.config(text=figures.figures[choice])
        self.computer_figure.config(text=figures.figures[computer])

        game = (choice, computer)
        if choice == computer:
            self.draws += 1
            self.result_var.set("It's a draw!")
            self.result_label.config(fg="#f0c36a")
        elif game in WIN:
            self.wins += 1
            self.result_var.set("You won!")
            self.result_label.config(fg="#7dcea0")
        else:
            self.losses += 1
            self.result_var.set("You lost")
            self.result_label.config(fg="#f0a07a")

        self._update_score()

    def _update_score(self):
        self.score_var.set(
            f"Wins {self.wins}    Losses {self.losses}    Draws {self.draws}"
        )


def main():
    root = tk.Tk()
    RockPaperScissor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
