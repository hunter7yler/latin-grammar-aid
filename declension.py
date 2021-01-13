import tkinter as tk


# imports list of declensions from declensions.csv and loads window for user review


# button methods

def load():
    new_wordlist = []
    cfile = open("./data/declensions.csv", "r")
    for line in cfile:
        line = line[:-1]
        sl = line.split(", ")
        new_wordlist.append(sl)
    cfile.close()
    return new_wordlist


def check():
    response_set = [snom, sgen, sdat, sacc, sabl, pnom, pgen, pdat, pacc, pabl]
    responses = []
    for response in response_set:
        responses.append(response.get())
    if responses == declensions[data_index]:
        lbl_response["text"] = "Correct!"
    else:
        lbl_response["text"] = "Try again."


def prev():
    global data_index  # don't want to pass arguments into button methods currently
    response_set = [snom, sgen, sdat, sacc, sabl, pnom, pgen, pdat, pacc, pabl]
    for response in response_set:
        response.delete(0, tk.END)
    data_index -= 1
    if data_index == -1:
        data_index = len(declensions) - 1
    lbl_n["text"] = declensions[data_index][0]


def next():
    global data_index  # don't want to pass arguments into button methods currently
    response_set = [snom, sgen, sdat, sacc, sabl, pnom, pgen, pdat, pacc, pabl]
    for response in response_set:
        response.delete(0, tk.END)
    data_index += 1
    if data_index == len(declensions):
        data_index = 0
    lbl_n["text"] = declensions[data_index][0]


# constants
data_index = 0  # keeps track of current word
declensions = load()

# window init
window = tk.Tk()
window.title("Latin Declension")

# frame generation
fl = []
for i in range(9):
    if i < 3:
        window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        fl.append(frame)

# widget generation
lbl_command = tk.Label(master=fl[0], text="Decline:")
lbl_n = tk.Label(master=fl[1], text=declensions[data_index][0])
lbl_sg = tk.Label(master=fl[4], text="sg.")
lbl_pl = tk.Label(master=fl[5], text="pl.")

lbl_nom = tk.Label(master=fl[6], text="nom.")
snom = tk.Entry(master=fl[7], width=10)
pnom = tk.Entry(master=fl[8], width=10)

lbl_gen = tk.Label(master=fl[9], text="gen.")
sgen = tk.Entry(master=fl[10], width=10)
pgen = tk.Entry(master=fl[11], width=10)

lbl_dat = tk.Label(master=fl[12], text="dat.")
sdat = tk.Entry(master=fl[13], width=10)
pdat = tk.Entry(master=fl[14], width=10)

lbl_acc = tk.Label(master=fl[15], text="acc.")
sacc = tk.Entry(master=fl[16], width=10)
pacc = tk.Entry(master=fl[17], width=10)

lbl_abl = tk.Label(master=fl[18], text="abl.")
sabl = tk.Entry(master=fl[19], width=10)
pabl = tk.Entry(master=fl[20], width=10)

btn_convert = tk.Button(master=fl[21], text="check", command=check)
lbl_response = tk.Label(master=fl[22], text="...")

btn_prev = tk.Button(master=fl[24], text="prev", command=prev)
btn_next = tk.Button(master=fl[25], text="next", command=next)

# pack labels
labels = [lbl_command, lbl_n, lbl_sg, lbl_pl, lbl_nom, snom, pnom, lbl_gen, sgen, pgen, lbl_dat, sdat, pdat, lbl_acc,
          sacc, pacc, lbl_abl, sabl, pabl, btn_convert, lbl_response, btn_prev, btn_next]
for label in labels:
    label.pack(padx=5, pady=5)

window.mainloop()
