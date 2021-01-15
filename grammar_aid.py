import tkinter as tk
from tkinter.filedialog import askopenfilename

class WindowNav(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("Choose file to review")
        self.frames = {}
        self.current_data = []
        self.data_index = 0

        for F in (StartPage, ConjPage, DeclPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        if cont in [DeclPage, ConjPage]:
            frame.lbl_n["text"] = self.current_data[self.data_index][0]
        frame.tkraise()

    def open_file(self):
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.csv"), ("All Files", "*.*")]
        )
        if not filepath:
            return

        with open(filepath, "r") as input_file:
            text = input_file.read()
            lines = text.split("\n")
            for line in lines:
                sl = line.split(", ")
                self.current_data.append(sl)

        if len(self.current_data[0]) == 10:
            self.show_frame(DeclPage)
        elif len(self.current_data[0]) == 6:
            self.show_frame(ConjPage)
        else:
            print("Unrecognized file format")
            quit()

        self.title("Reviewing: {}".format(filepath.split("/")[-1]))

    def prev(self, child):
        for response in child.response_set:
             response.delete(0, tk.END)
        self.data_index -= 1
        if self.data_index == -1:
            self.data_index = len(self.current_data) - 1
        if len(self.current_data[self.data_index]) == 10:
            self.show_frame(DeclPage)
        elif len(self.current_data[self.data_index]) == 6:
            self.show_frame(ConjPage)
        else:
            print("Unrecognized file format")
            quit()

    def next(self, child):
        for response in child.response_set:
             response.delete(0, tk.END)
        self.data_index += 1
        if self.data_index == len(self.current_data):
            self.data_index = 0
        if len(self.current_data[self.data_index]) == 10:
            self.show_frame(DeclPage)
        elif len(self.current_data[self.data_index]) == 6:
            self.show_frame(ConjPage)
        else:
            print("Unrecognized file format")
            quit()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = tk.Button(self, text="Load Data", command=lambda: controller.open_file())
        button1.pack()

class DeclPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.cont = controller
        # frame generation
        fl = []
        for i in range(10):  # generate grid of frames
            if i < 3:
                self.columnconfigure(i, weight=1, minsize=75)
            self.rowconfigure(i, weight=1, minsize=50)
            for j in range(0, 3):
                frame = tk.Frame(master=self, borderwidth=1)
                frame.grid(row=i, column=j, padx=5, pady=5)
                fl.append(frame)

        # widget define
        lbl_command = tk.Label(master=fl[0], text="Decline:")
        self.lbl_n = tk.Label(master=fl[1], text="...")
        lbl_sg = tk.Label(master=fl[4], text="sg.")
        lbl_pl = tk.Label(master=fl[5], text="pl.")

        lbl_nom = tk.Label(master=fl[6], text="nom.")
        self.snom = tk.Entry(master=fl[7], width=10)
        self.pnom = tk.Entry(master=fl[8], width=10)

        lbl_gen = tk.Label(master=fl[9], text="gen.")
        self.sgen = tk.Entry(master=fl[10], width=10)
        self.pgen = tk.Entry(master=fl[11], width=10)

        lbl_dat = tk.Label(master=fl[12], text="dat.")
        self.sdat = tk.Entry(master=fl[13], width=10)
        self.pdat = tk.Entry(master=fl[14], width=10)

        lbl_acc = tk.Label(master=fl[15], text="acc.")
        self.sacc = tk.Entry(master=fl[16], width=10)
        self.pacc = tk.Entry(master=fl[17], width=10)

        lbl_abl = tk.Label(master=fl[18], text="abl.")
        self.sabl = tk.Entry(master=fl[19], width=10)
        self.pabl = tk.Entry(master=fl[20], width=10)

        btn_convert = tk.Button(master=fl[21], text="Check", command=self.check)
        self.lbl_response = tk.Label(master=fl[22], text="...")

        btn_prev = tk.Button(master=fl[24], text="Prev", command=lambda: controller.prev(self))
        btn_next = tk.Button(master=fl[25], text="Next", command=lambda: controller.next(self))

        # widget place
        labels = [lbl_command, self.lbl_n, lbl_sg, lbl_pl, lbl_nom, self.snom, self.pnom, lbl_gen, self.sgen, self.pgen, lbl_dat, self.sdat, self.pdat, lbl_acc, self.sacc, self.pacc, lbl_abl, self.sabl, self.pabl, btn_convert, self.lbl_response, btn_prev, btn_next]
        for label in labels:
            label.pack(padx=5, pady=5)

        self.response_set = [self.snom, self.sgen, self.sdat, self.sacc, self.sabl, self.pnom, self.pgen, self.pdat, self.pacc, self.pabl]

    def check(self):
        responses = []
        for response in self.response_set:
            responses.append(response.get())
        if responses == self.cont.current_data[self.cont.data_index]:
            self.lbl_response["text"] = "Correct!"
        else:
            self.lbl_response["text"] = "Try again."

class ConjPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.cont = controller
        # frame generation
        fl = []
        for i in range(7):
            if i < 3:
                self.columnconfigure(i, weight=1, minsize=75)
            self.rowconfigure(i, weight=1, minsize=50)
            for j in range(0, 3):
                frame = tk.Frame(master=self, borderwidth=1)
                frame.grid(row=i, column=j, padx=5, pady=5)
                fl.append(frame)

        # widget generation
        lbl_command = tk.Label(master=fl[0], text="Conjugate:")
        self.lbl_n = tk.Label(master=fl[1], text="...")

        lbl_sg = tk.Label(master=fl[4], text="sg.")
        lbl_pl = tk.Label(master=fl[5], text="pl.")

        lbl_first = tk.Label(master=fl[6], text="1st")
        self.sfirst = tk.Entry(master=fl[7], width=10)
        self.pfirst = tk.Entry(master=fl[8], width=10)

        lbl_second = tk.Label(master=fl[9], text="2nd")
        self.ssecond = tk.Entry(master=fl[10], width=10)
        self.psecond = tk.Entry(master=fl[11], width=10)

        lbl_third = tk.Label(master=fl[12], text="3rd")
        self.sthird = tk.Entry(master=fl[13], width=10)
        self.pthird = tk.Entry(master=fl[14], width=10)

        btn_convert = tk.Button(master=fl[15], text="check", command=self.check)
        self.lbl_response = tk.Label(master=fl[16], text="...")

        btn_prev = tk.Button(master=fl[18], text="Prev", command=lambda: controller.prev(self))
        btn_next = tk.Button(master=fl[19], text="Next", command=lambda: controller.next(self))

        # pack labels
        labels = [lbl_command, self.lbl_n, lbl_sg, lbl_pl, lbl_first, self.sfirst, self.pfirst, lbl_second, self.ssecond, self.psecond, lbl_third, self.sthird, self.pthird, btn_convert, self.lbl_response, btn_prev, btn_next]
        for label in labels:
            label.pack(padx=5, pady=5)

        self.response_set = [self.sfirst, self.ssecond, self.sthird, self.pfirst, self.psecond, self.pthird]

    def check(self):
        responses = []
        for response in self.response_set:
            responses.append(response.get())
        if responses == self.cont.current_data[self.cont.data_index]:
            self.lbl_response["text"] = "Correct!"
        else:
            self.lbl_response["text"] = "Try again."


app = WindowNav()
app.mainloop()