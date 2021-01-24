import tkinter
from tkinter import *
from tkinter import ttk
from company import *

"""
def save():
	for company in tabs:
		company.save()
	for brand in wwe_tabs:
		brand.save()
def load():
	for company in tabs:
		company.load()
	for brand in wwe_tabs:
		brand.load()
"""
def update():
    for company in tabs:
        company.update()
    wweTab.update()

# Main Window
window = tkinter.Tk()
window.title("Wrestling Roster Tool")
window.geometry("800x600")

menu = Menu(window)
window.config(menu=menu)
file = Menu(menu)
#file.add_command(label="Save All", command=save)
file.add_command(label="Update All", command=update)
menu.add_cascade(label="File", menu=file)

# Tab setup
parent_tab = ttk.Notebook(window)
    #Create companies
tabs = [
Company("AAA","https://www.cagematch.net/?id=8&nr=122&page=15",parent_tab,
["AAA Mega Champion","AAA Latin American Champion","AAA World Cruiserweight Champion","AAA Reina de Reinas Champion", 
"AAA World Tag Team Champion","AAA World Trios Champion","AAA World Mixed Tag Team Champion"]),
Company("AEW","https://www.cagematch.net/?id=8&nr=2287&page=15",parent_tab,[
"World Champion","Women's World Champion","TNT Champion","World Tag Team Champion","FTW Champion"]),
Company("Impact","https://www.cagematch.net/?id=8&nr=5&page=15",parent_tab,[
"World Champion","Knockouts Champion","X Division Champion","World Tag Team Champion"]),
Company("MLW","https://www.cagematch.net/?id=8&nr=22&page=15",parent_tab,[
"MLW World Heavyweight Champion","MLW World Middleweight Champion","MLW National Openweight Champion","MLW World Tag Team Champion"]),
Company("NWA","https://www.cagematch.net/?id=8&nr=9&page=15",parent_tab,[
"NWA Worlds Heavyweight Champion","NWA World Women's Champion","NWA National Heavyweight Champion","NWA World Tag Team Champion"]),
Company("NJPW","https://www.cagematch.net/?id=8&nr=7&page=15",parent_tab,["IWGP Heavyweight Champion",
"IWGP Intercontinental Champion","IWGP United States Champion","NEVER Openweight Champion","IWGP Tag Team Champion",
"IWGP Junior Heavyweight Champion","IWGP Junior Heavyweight Tag Team Champion","NEVER Openweight 6-Man Tag Team Champion", "KOPW 2020"]),
Company("ROH","https://www.cagematch.net/?id=8&nr=4&page=15",parent_tab,[
"World Champion","Pure Wrestling Champion","Television Champion","World Tag Team Champion","World Six-Man Tag Team Champion"])
]
wweTab = WWE(parent_tab)

parent_tab.add(tabs[0].frame, text=tabs[0].name)
parent_tab.add(tabs[1].frame, text=tabs[1].name)
parent_tab.add(tabs[2].frame, text=tabs[2].name)
parent_tab.add(tabs[3].frame, text=tabs[3].name)
parent_tab.add(tabs[4].frame, text=tabs[4].name)
parent_tab.add(tabs[5].frame, text=tabs[5].name)
parent_tab.add(tabs[6].frame, text=tabs[6].name)

parent_tab.add(wweTab.notebook,text="WWE")

parent_tab.pack(expand=1, fill='both')

#load rosters
#load()

#main loop
window.mainloop()