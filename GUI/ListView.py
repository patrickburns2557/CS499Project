import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
import GUI.ScrollablePatientList as spl
import Data.System
import GUI.MainWindow

class ListView(ctk.CTkFrame):
    def __init__(self, parentWidget, patientList):
        super().__init__(parentWidget)
        #Variable to hold the text in the search box
        self.search = ctk.StringVar()

        self.searchText = ctk.CTkLabel(self, text="Name:", font=("Courier", 18, "bold"))
        self.searchText.grid(row=0, column=0, padx=10)

        self.textBox = ctk.CTkEntry(
            self,
            width=40,
            font=("Courier", 18, "bold"),
            textvariable=self.search
        )
        self.textBox.grid(row=0, column=1, sticky="ew", pady=6)
        #press enter to do the same thing as the search button
        self.textBox.bind('<Return>', self.searchPatient)

        self.searchButton = ctk.CTkButton(
            self,
            text="Search",
            font=("Courier", 18, "bold"),
            width=100,
            height=35,
            command=self.searchPatient
        )
        self.searchButton.grid(row=0, column=2, sticky="ew", padx=10, pady=6)
        
        #Label at the top showing what each info column means
        self.topLabel = spl.PatientListTopLabel(self)
        self.topLabel.grid(row=1, column=0, columnspan=10, sticky="ew")


        self.scrollable = spl.ScrollablePatientList(self, patientList)
        self.scrollable.grid(row=2, column=0, sticky="news", columnspan=3)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.textBox.focus_set()

    #Filter the patient list to find the one in the search box
    def searchPatient(self, input="", event=None):
        patientList = Data.System.getPatientList()
        filteredList = []
        input = self.search.get()
        for p in patientList:
            if input.lower() in p.firstName.lower() or input.lower() in p.middleName.lower() or input.lower() in p.lastName.lower():
                filteredList.append(p)
        
        #Destroy the current list and load in the filtered one
        for i in self.scrollable.winfo_children():
            i.destroy()
        self.scrollable.destroy()
        self.scrollable = spl.ScrollablePatientList(self, filteredList)
        self.scrollable.grid(row=2, column=0, sticky="news", columnspan=3)
        return filteredList