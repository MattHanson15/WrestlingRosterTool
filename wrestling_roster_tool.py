import tkinter
from tkinter import *
from tkinter import ttk
from company import *

def showNews():
	i = tab_parent.index(tab_parent.select())
	if(i < 6):
		tabs[i].newsTicker()
	else:
		i = wwe.index(wwe.select())
		wwe_tabs[i].newsTicker()
	window.after(300, showNews)
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
def update():
	for company in tabs:
		company.update()
	for brand in wwe_tabs:
		brand.update()

# Main Window
window = tkinter.Tk()
window.title("Wrestling Roster Tool")
window.geometry("800x600")
menu = Menu(window)
window.config(menu=menu)
file = Menu(menu)
file.add_command(label="Save All", command=save)
file.add_command(label="Update All", command=update)
menu.add_cascade(label="File", menu=file)

# Tab setup
tab_parent = ttk.Notebook(window)
	#Create companies
tabs = [
Company("AAA",'https://en.wikipedia.org/wiki/List_of_Lucha_Libre_AAA_Worldwide_personnel',tab_parent,[0],[1],
["AAA Mega Champion","AAA Latin American Champion","AAA World Cruiserweight Champion","AAA Reina de Reinas Champion", 
"AAA World Tag Team Champion","AAA World Trios Champion","AAA World Mixed Tag Team Champion"],'https://www.f4wonline.com/mexico-news'),
Company("AEW",'https://en.wikipedia.org/wiki/List_of_All_Elite_Wrestling_personnel',tab_parent,[0],[1],[
"World Champion","Women's World Champion","TNT Champion","World Tag Team Champion","FTW Champion"],'https://www.f4wonline.com/aew-news'),
Company("Impact",'https://en.wikipedia.org/wiki/List_of_Impact_Wrestling_personnel',tab_parent,[0],[1],[
"World Champion","Knockouts Champion","X Division Champion","World Tag Team Champion"],'https://www.f4wonline.com/tna-news'),
MLW("MLW",'https://en.wikipedia.org/wiki/List_of_Major_League_Wrestling_personnel',tab_parent,[0],[1],[
"MLW World Heavyweight Champion","MLW World Middleweight Champion","MLW National Openweight Champion","MLW World Tag Team Champion"],'https://www.f4wonline.com/tags/mlw'),
NXT("NWA",'https://en.wikipedia.org/wiki/List_of_National_Wrestling_Alliance_personnel',tab_parent,[0],[1],[
"NWA Worlds Heavyweight Champion","NWA World Women's Champion","NWA National Heavyweight Champion","NWA World Tag Team Champion"],'https://www.f4wonline.com/tags/nwa'),
NJPW("NJPW",'https://en.wikipedia.org/wiki/List_of_New_Japan_Pro-Wrestling_personnel',tab_parent,[0],[1],["IWGP Heavyweight Champion",
"IWGP Intercontinental Champion","IWGP United States Champion","NEVER Openweight Champion","IWGP Tag Team Champion",
"IWGP Junior Heavyweight Champion","IWGP Junior Heavyweight Tag Team Champion","NEVER Openweight 6-Man Tag Team Champion"],'https://www.f4wonline.com/japan-news'),
Company("ROH",'https://en.wikipedia.org/wiki/List_of_Ring_of_Honor_personnel',tab_parent,[0],[1],[
"ROH World Champion","ROH World Television Champion","ROH World Tag Team Champion","ROH World Six-Man Tag Team Champion"],'https://www.f4wonline.com/roh-news')
]
	#WWE contains brands so it becomes a parent tab
wwe = ttk.Notebook(tab_parent)
	#Create brands
wwe_tabs = [
WWE("RAW",'https://en.wikipedia.org/wiki/List_of_WWE_personnel',wwe,[1],[2],[
"WWE Champion","Raw Women's Champion","United States Champion","Raw Tag Team Champion","24/7 Champion"],"Raw",'https://www.f4wonline.com/wwe-news'),
WWE("Smackdown",'https://en.wikipedia.org/wiki/List_of_WWE_personnel',wwe,[4],[5],[
"Universal Champion","SmackDown Women's Champion","Intercontinental Champion","SmackDown Tag Team Champion",
"Women's Tag Team Champion"],"SmackDown",'https://www.f4wonline.com/wwe-news'),
WWE("NXT",'https://en.wikipedia.org/wiki/List_of_WWE_personnel',wwe,[7,10,13],[8,11],[
"NXT Champion","NXT Women's Champion","North American Champion","NXT Tag Team Champion","NXT Cruiserweight Champion","NXT United Kingdom Champion",
"NXT UK Women's Champion","NXT UK Tag Team Champion"], "NXT",'https://www.f4wonline.com/tags/nxt')
]

tab_parent.add(tabs[0].frame, text=tabs[0].name)
tab_parent.add(tabs[1].frame, text=tabs[1].name)
tab_parent.add(tabs[2].frame, text=tabs[2].name)
tab_parent.add(tabs[3].frame, text=tabs[3].name)
tab_parent.add(tabs[4].frame, text=tabs[4].name)
tab_parent.add(tabs[5].frame, text=tabs[5].name)
tab_parent.add(wwe,text="WWE")
wwe.add(wwe_tabs[0].frame,text=wwe_tabs[0].name)
wwe.add(wwe_tabs[1].frame, text=wwe_tabs[1].name)
wwe.add(wwe_tabs[2].frame, text=wwe_tabs[2].name)

tab_parent.pack(expand=1, fill='both')

#load rosters
load()

#main loop
showNews()
window.mainloop()