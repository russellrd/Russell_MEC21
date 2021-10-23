import xlrd
from tkinter import *
from tkinter import ttk

voters = []
party_vote_labels = []

valid_parties = {
    'Socks and Crocs Reform League': 0,
    'Pineapple Pizza Party': 0,
    'Pronounced Jiff Union': 0
}

voting_data = xlrd.open_workbook('MEC Competition Voting Data.xls').sheet_by_index(0)

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Very Secure Voting System (VSVS)").grid(columnspan=len(valid_parties))

class Voter():
    def __init__(self, first, last, party):
        self.first = first
        self.last = last
        self.party = party
    
    def check_valid(self):
        return (len(self.party.split(',')) == 1)

def count_votes():
    for voter in voters:
        if voter.check_valid():
            valid_parties[voter.party] = valid_parties[voter.party]+1

        
for i in range(1, voting_data.nrows):
    double = False
    for voter in voters:
        if (voting_data.cell_value(i, 0) == voter.first) and (voting_data.cell_value(i, 1) == voter.last):
            double = True
    if not double:
        voters.append(Voter(voting_data.cell_value(i, 0), voting_data.cell_value(i, 1), voting_data.cell_value(i, 2)))

count_votes()

for i in range(len(valid_parties)):
    ttk.Label(frame, text=list(valid_parties)[i]).grid(column=i, row=1, padx=10, pady=10)
    party_vote_labels.append(ttk.Label(frame, text=list(valid_parties.values())[i]).grid(column=i, row=2))



root.mainloop()