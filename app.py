import xlrd
import tkinter as tk
from tkinter import Frame, StringVar, ttk

voters = []
party_vote_labels = []

valid_parties = {
    'Socks and Crocs Reform League': 0,
    'Pineapple Pizza Party': 0,
    'Pronounced Jiff Union': 0
}

class Voter():
    def __init__(self, first, last, party):
        self.first = first
        self.last = last
        self.party = party
    
    def check_valid(self):
        return (len(self.party.split(',')) == 1)

def clear_votes():
    for party in valid_parties:
        valid_parties[party] = 0

def count_votes():
    clear_votes()
    for voter in voters:
        if voter.check_valid():
            valid_parties[voter.party] = valid_parties[voter.party]+1
    update_votes()

def update_votes():
    for i in range(len(valid_parties)):
        ttk.Label(frame, text=list(valid_parties.values())[i]).grid(column=i, row=3)

def load_data():
    try:
        voting_data = xlrd.open_workbook(data_file.get()+'.xls').sheet_by_index(0)
        for i in range(1, voting_data.nrows):
            double = False
            for voter in voters:
                if (voting_data.cell_value(i, 0) == voter.first) and (voting_data.cell_value(i, 1) == voter.last):
                    double = True
            if not double:
                voters.append(Voter(voting_data.cell_value(i, 0), voting_data.cell_value(i, 1), voting_data.cell_value(i, 2)))
        count_votes()
    except:
        print("File does not exist!")

def vote(first, last, party):
    double = False
    for voter in voters:
        if (first == voter.first) and (last == voter.last):
            double = True
    if not double:
        voters.append(Voter(first, last, party))
    count_votes()

def open_login_page():
    login_page = tk.Toplevel(root)
    login_frame = Frame(login_page)
    login_frame.grid()

    first_name = tk.StringVar()
    ttk.Label(login_frame, text="First Name: ").grid(column=0, row=0, padx=10, pady=10)
    ttk.Entry(login_frame, textvariable=first_name).grid(column=1, row=0, padx=10, pady=10)

    last_name = tk.StringVar()
    ttk.Label(login_frame, text="Last Name: ").grid(column=0, row=1, padx=10)
    ttk.Entry(login_frame, textvariable=last_name).grid(column=1, row=1, padx=10, pady=10)

    ttk.Label(login_frame, text="Photo: ").grid(column=0, row=2, padx=10)

    selected = StringVar()
    ttk.Label(login_frame, text="Party: ").grid(column=0, row=3, padx=10)
    tk.OptionMenu(login_frame, selected, *list(valid_parties)).grid(column=1, row=3, padx=10)

    ttk.Button(login_frame, text="Vote", command=lambda: vote(first_name.get(), last_name.get(), selected.get())).grid(column=1, row=4, padx=10, pady=10)

def video_stream():
    pass

root = tk.Tk()
root.title("Very Secure Voting System (VSVS)")
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Very Secure Voting System (VSVS)").grid(columnspan=len(valid_parties)-1)
ttk.Button(frame, text="Online Voting", command=open_login_page).grid(column=2, row=0, padx=10, pady=10)
data_file = tk.StringVar()
ttk.Label(frame, text="Enter Voting Data File Name: ").grid(column=0, row=1, padx=10, pady=10)
ttk.Entry(frame, textvariable=data_file).grid(column=1, row=1, padx=10, pady=10)
data_button = ttk.Button(frame, text="Load Voter Data", command=load_data).grid(column=2, row=1, padx=10, pady=10)

for i in range(len(valid_parties)):
    ttk.Label(frame, text=list(valid_parties)[i]).grid(column=i, row=2, padx=10, pady=10)
    ttk.Label(frame, text=list(valid_parties.values())[i]).grid(column=i, row=3)

root.mainloop()