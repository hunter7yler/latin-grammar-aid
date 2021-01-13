import tkinter as tk


# imports list of conjugations from conjugations.csv and loads window for user review


# button methods

def load():
    new_wordlist = []
    cfile = open("./data/conjugations.csv", "r")
    for line in cfile:
        line = line[:-1]
        sl = line.split(", ")
        new_wordlist.append(sl)
    cfile.close()
    return new_wordlist


def check():
    response_set = [sfirst, ssecond, sthird, pfirst, psecond, pthird]
    responses = []
    for response in response_set:
        responses.append(response.get())
    if responses == conjugations[data_index]:
        lbl_response["text"] = "Correct!"
    else:
        lbl_response["text"] = "Try again."


def prev():
    global data_index  # don't want to pass arguments into button methods currently
    response_set = [sfirst, ssecond, sthird, pfirst, psecond, pthird]
    for response in response_set:
        response.delete(0, tk.END)
    data_index -= 1
    if data_index == -1:
        data_index = len(conjugations) - 1
    lbl_n["text"] = conjugations[data_index][0]


def next():
    global data_index  # don't want to pass arguments into button methods currently
    response_set = [sfirst, ssecond, sthird, pfirst, psecond, pthird]
    for response in response_set:
        response.delete(0, tk.END)
    data_index += 1
    if data_index == len(conjugations):
        data_index = 0
    lbl_n["text"] = conjugations[data_index][0]


# constants
data_index = 0  # keeps track of current word
conjugations = load()

# window init
window = tk.Tk()
window.title("Latin Conjugations")

# frame generation
fl = []
for i in range(7):
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
lbl_command = tk.Label(master=fl[0], text="Conjugate:")
lbl_n = tk.Label(master=fl[1], text=conjugations[data_index][0])

lbl_sg = tk.Label(master=fl[4], text="sg.")
lbl_pl = tk.Label(master=fl[5], text="pl.")

lbl_first = tk.Label(master=fl[6], text="1st")
sfirst = tk.Entry(master=fl[7], width=10)
pfirst = tk.Entry(master=fl[8], width=10)

lbl_second = tk.Label(master=fl[9], text="2nd")
ssecond = tk.Entry(master=fl[10], width=10)
psecond = tk.Entry(master=fl[11], width=10)

lbl_third = tk.Label(master=fl[12], text="3rd")
sthird = tk.Entry(master=fl[13], width=10)
pthird = tk.Entry(master=fl[14], width=10)

btn_convert = tk.Button(master=fl[15], text="check", command=check)
lbl_response = tk.Label(master=fl[16], text="...")

btn_prev = tk.Button(master=fl[18], text="prev", command=prev)
btn_next = tk.Button(master=fl[19], text="next", command=next)

# pack labels
labels = [lbl_command, lbl_n, lbl_sg, lbl_pl, lbl_first, sfirst, pfirst, lbl_second, ssecond, psecond, lbl_third, sthird, pthird, btn_convert, lbl_response, btn_prev, btn_next]
for label in labels:
    label.pack(padx=5, pady=5)

window.mainloop()
