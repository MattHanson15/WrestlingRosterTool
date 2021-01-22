import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import requests
from bs4 import BeautifulSoup
import csv

class Company:    
    def __init__(self, name, url, parent_tab, belts):
        self.name = name
        self.url = url
        self.belts = belts
        self.champs = []
        self.frame = ttk.Frame(parent_tab)
        self.listbox_male = Listbox(self.frame, width=35)
        self.listbox_female = Listbox(self.frame, width=35)
        self.button_update = Button(self.frame, text="Update", command=self.update)
        self.label_champHeader = Label(self.frame, text="Current Champions")
        self.label_men = Label(self.frame, text="Men")
        self.label_women = Label(self.frame, text="Women")
        
        self.label_men.grid(row=1, column=0, padx=(90,0), pady=(5,0), sticky=W)
        self.label_women.grid(row=1,column=1, padx=(90,0), pady=(5,0), sticky=W)
        self.listbox_male.grid(row=1+1, column=0, padx=(15,0), pady=(0,30), sticky=W)
        self.listbox_female.grid(row=1+1, column=1, padx=(0,0), pady=(0,30), sticky=W)
        self.button_update.grid(row=2+1, column=0, padx=(0,80), sticky=E)
        self.label_champHeader.grid(row=3+1,column=0, padx=15, pady=5)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        i=0
        while i < len(self.belts):
            self.champs.append(Label(self.frame,text=self.belts[i]+": "))
            self.champs[i].grid(row=4+i+1, column=0, columnspan=2, padx=15, pady=2, sticky=W)
            i+=1
    #Methods
    def getWrestlers(self, soup, category, listbox):
        listbox.delete(0,END)
        table = soup.find(id=category).findNext('table')
        rows = table.findAll('tr')
        for row in rows:
            data = row.findAll('td')
            if(len(data) > 0):
                name = data[0].text.strip().split('[')[0]
                listbox.insert(END, name)
                notes = data[2].findAll('a')
                if(len(notes) > 0):
                    k=0
                    for belt in self.belts:
                        for note in notes:
                            if (note.text.strip().split('[')[0] == belt or note.get('title') == belt ):
                                self.champs[k].configure(text=self.champs[k]["text"]+name+"  ")
                        k = k + 1
    def update(self):
        try:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print("Error occured while updating")
            return()
        i=0
        while i < len(self.champs):
            self.champs[i].configure(text=self.belts[i]+": ")
            i+=1
        self.getWrestlers(soup, "Male_wrestlers", self.listbox_male)
        self.getWrestlers(soup,"Female_wrestlers",self.listbox_female)
    def save(self):
        found = 0
        count = 0
        male_roster = ""
        female_roster = ""
        champ_roster = ""
        
        for wrestler in self.listbox_male.get(0,END):
            if(count > 0):
                male_roster = male_roster + ","+wrestler
            else:
                male_roster = wrestler
            count += 1
        count = 0
        for wrestler in self.listbox_female.get(0,END):
            if(count > 0):
                female_roster = female_roster + ","+wrestler
            else:
                female_roster = wrestler
            count += 1
        count = 0
        for wrestler in self.champs:
            if(count > 0):
                champ_roster = champ_roster + ","+wrestler['text']
            else:
                champ_roster = wrestler['text']
            count += 1
        count = 0
        try:
            f = open('data.csv', 'r')
            contents = f.readlines()
            f.close()
        except:
            contents=[]
        for line in contents:
            if(found == 0):
                if(self.name == line.strip()):
                    found = 1
                count +=1
        print("Saving local "+self.name+" data")
        if(found == 1):
            contents[count]=male_roster+'\n'
            contents[count+1]=female_roster+'\n'
            contents[count+2]=champ_roster+'\n'
        if(found == 0):
            contents.append(self.name+'\n')
            contents.append(male_roster+'\n')
            contents.append(female_roster+'\n')
            contents.append(champ_roster+'\n')
            
        f = open('data.csv', 'w')
        f.writelines(contents)
        f.close()
    def load(self):
        try:
            f = open('data.csv', 'r+', newline='')
        except:
            print("Unable to load data.csv")
            return()
        count=0
        found=0
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            if(found == 0):
                if(len(row) > 0):
                    if (self.name == row[0].strip()):
                        found=1
                        print("Loading local "+self.name+" data")
                        break
        if(found == 1):
            for wrestler in next(csv_reader):
                self.listbox_male.insert(END,wrestler)
            for wrestler in next(csv_reader):
                self.listbox_female.insert(END,wrestler)
            for wrestler in next(csv_reader):
                self.champs[count].configure(text=self.champs[count]['text']+wrestler.split(": ")[1])
                count+=1

class MLW(Company):
    def update(self):
        try:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print("Error occured while updating")
            return()
        i=0
        while i < len(self.champs):
            self.champs[i].configure(text=self.belts[i]+": ")
            i+=1
        self.getWrestlers(soup, "Male_Wrestlers", self.listbox_male)
        self.getWrestlers(soup,"Female_Wrestlers",self.listbox_female)
class NJPW(Company):
    def __init__(self, name, url, parent_tab, belts):
        Company.__init__(self, name, url, parent_tab, belts)
        self.label_men.configure(text="Heavyweights")
        self.label_women.configure(text="Junior Heavyweghts")
        self.label_men.grid(row=1, column=0, padx=(81,0), pady=(5,0), sticky=W)
        self.label_women.grid(row=1,column=1, padx=(50,0), pady=(5,0), sticky=W)
    def getWrestlers(self, soup, category, listbox):
        listbox.delete(0,END)
        table = soup.find(id=category).findNext('table')
        rows = table.findAll('tr')
        for row in rows:
            data = row.findAll('td')
            if(len(data) > 0):
                name = data[0].text.strip().split('[')[0]
                listbox.insert(END, name)
                notes = data[3].findAll('a')
                if(len(notes) > 0):
                    k=0
                    for belt in self.belts:
                        for note in notes:
                            if (note.text.strip().split('[')[0] == belt or note.get('title') == belt ):
                                self.champs[k].configure(text=self.champs[k]["text"]+name+"  ")
                        k = k + 1
    def update(self):
        try:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print("Error occured while updating")
            return()
        i=0
        while i < len(self.champs):
            self.champs[i].configure(text=self.belts[i]+": ")
            i+=1
        self.getWrestlers(soup, "Heavyweight_division", self.listbox_male)
        self.getWrestlers(soup,"Junior_heavyweight_division",self.listbox_female)
class WWE(Company):
    def __init__(self, name, url, parent_tab, belts, brand):
        Company.__init__(self, name, url, parent_tab, belts)
        self.brand = brand
    def getWrestlers(self, soup, category, listbox):
        listbox.delete(0,END)
        if(self.brand == "SmackDown"):
            category = category+"_2"
        elif(self.brand == "NXT"):
            category = category+"_3"
        elif(self.brand == "NXT_UK"):
            category = category+"_4"
        table = soup.find(id=self.brand).findNext(id=category).findNext('table')
        rows = table.findAll('tr')
        for row in rows:
            data = row.findAll('td')
            if(len(data) > 0):
                name = data[0].text.strip().split('[')[0]
                listbox.insert(END, name)
                notes = data[2].findAll('a')
                if(len(notes) > 0):
                    k=0
                    for belt in self.belts:
                        for note in notes:
                            if (note.text.strip().split('[')[0] == belt or note.get('title') == belt):
                                self.champs[k].configure(text=self.champs[k]["text"]+name+"  ")
                        k = k + 1