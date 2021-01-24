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
        self.listbox_roster = Listbox(self.frame, width=35)
        self.button_update = Button(self.frame, text="Update", command=self.update)
        self.label_champHeader = Label(self.frame, text="Current Champions")
        self.label_roster = Label(self.frame, text="Roster")
        
        self.label_roster.grid(row=1, column=0, padx=(90,0), pady=(5,0), sticky=W)
        self.listbox_roster.grid(row=2, column=0, padx=(15,0), pady=(0,30), sticky=W)
        self.button_update.grid(row=3, column=0, padx=(0,80), sticky=E)
        self.label_champHeader.grid(row=4,column=0, padx=15, pady=5)
        i=0
        while i < len(self.belts):
            self.champs.append(Label(self.frame,text=self.belts[i]+": "))
            self.champs[i].grid(row=4+i+1, column=0, columnspan=2, padx=15, pady=2, sticky=W)
            i+=1    
    def update(self):
        try:
            page = requests.get(self.url, headers={'Accept-Encoding': 'identity'})
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print("Error occured while updating")
            return()
        
        i=0
        while i < len(self.champs):
            self.champs[i].configure(text=self.belts[i]+": ")
            i+=1
        
        self.listbox_roster.delete(0,END)
        
        table = soup.find('table')
        if not (table):
            print("Could not find table")
            return()
            
        rows = table.findAll('tr')
        if not (rows):
            print("Found table but no rows")
            return()
        
        for row in rows:
            cells = row.findAll('td')
            if not (cells):
                continue
            if(len(cells) < 4):
                continue
            if(cells[3].text.find("Wrestler") >= 0):
                self.listbox_roster.insert(END, cells[2].text)

class WWE():
    def __init__(self, parent_tab):
        self.name = "WWE"
        self.url = "https://www.cagematch.net/?id=8&nr=1&page=15"
        self.notebook = ttk.Notebook(parent_tab)
        self.brands = [
                Company("RAW"," ",self.notebook,[
                    "WWE Champion","Raw Women's Champion","United States Champion","Raw Tag Team Champion","Women's Tag Team Champion","24/7 Champion"]),
                Company("Smackdown"," ",self.notebook,[
                    "Universal Champion","SmackDown Women's Champion","Intercontinental Champion","SmackDown Tag Team Champion",
                    "Women's Tag Team Champion","24/7 Champion"]),
                Company("NXT"," ",self.notebook,[
                    "NXT Champion","NXT Women's Champion","North American Champion","NXT Tag Team Champion","Women's Tag Team Champion","NXT Cruiserweight Championship"]),
                Company("NXT UK"," ",self.notebook,[
                    "NXT United Kingdom Champion","NXT UK Women's Champion","NXT UK Tag Team Champion", "NXT Cruiserweight Champion", "Heritage Cup Champion"])
                ]
        for brand in self.brands:
            self.notebook.add(brand.frame,text=brand.name)
            brand.button_update.configure(command=self.update)
            i=0    
            while i < len(brand.champs):
                brand.champs[i].configure(text=brand.belts[i]+": ")
                i+=1   
    def update(self):
        try:
            page = requests.get("https://www.cagematch.net/?id=8&nr=1&page=15", headers={'Accept-Encoding': 'identity'})
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print("Error occured while updating")
            return()
        
        table = soup.find('table')
        if not (table):
            print("Could not find table")
            return()
        rows = table.findAll('tr')
        if not (rows):
            print("Found table but no rows")
            return()
        
        for brand in self.brands:
            for row in rows:
                cells = row.findAll('td')
                if not (cells):
                    continue
                if(cells[4].text.casefold() == brand.name.casefold() and cells[3].text.find("Wrestler") >= 0):
                    brand.listbox_roster.insert(END, cells[2].text)
                    
                
        
            
                    