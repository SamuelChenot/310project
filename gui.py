from tkinter import *
import tkinter.messagebox as tm
import tkinter.ttk as ttk
from PIL import ImageTk, Image

import numpy as np
import pandas as pandas
from matplotlib import pyplot as plt 


import tkinter as tk


def DisplayGraphs(graphName):

    options = ['class','size','distribution','activity','evolution','previous_24_hours','historical_complexity','become_complex','area','area_of_largest_spot','cClassFlares','mClassFlares','xClassFlares']

    df = pandas.read_csv("flare1.csv")


    x = df.dropna(subset=['class'])
    y = df.dropna(subset=['size'])

    if(graphName == 'class'):

        plot_series = df.loc[:,'class'].rename('')
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')

    elif(graphName == 'size'):

        plot_series = df.loc[:,'size'].rename('')
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')
    
    elif(graphName == 'distribution'):

        plot_series = df.loc[:,'distribution'].rename('')
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')
        
    elif(graphName == 'activity'):
        plot_series = df.loc[:,'activity'].rename('')
        plot_series = plot_series.replace({1 : 'reduced', 2 : 'unchanged'})
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')
        
    elif(graphName == 'evolution'):
        plot_series = df.loc[:,'evolution'].rename('')
        plot_series = plot_series.replace({1 : 'decay', 2 : 'no growth', 3 : 'growth'})
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')
        
    elif(graphName == 'previous_24_hours'):
        plot_series = df.loc[:,'previous_24_hours'].rename('')
        plot_series = plot_series.replace({1 : '< M1', 2 : 'M1', 3 : '>M1'})
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')
        
    elif(graphName == 'historical_complexity'):
        plot_series = df.loc[:,'historical_complexity'].rename('')
        plot_series = plot_series.replace({1 : 'Yes', 2 : 'No'})
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')
        
    elif(graphName == 'become_complex'):
        plot_series = df.loc[:,'become_complex'].rename('')
        plot_series = plot_series.replace({1 : 'Yes', 2 : 'No'})
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')
        
    elif(graphName == 'area'):
        plot_series = df.loc[:,'area'].rename('')
        plot_series = plot_series.replace({1 : 'Small', 2 : 'Large'})
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')
        
    elif(graphName == 'area_of_largest_spot'):
        plot_series = df.loc[:,'area_of_largest_spot'].rename('')
        plot_series = plot_series.replace({1 : '<=5', 2 : '>5'})
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')
        
    elif(graphName == 'cClassFlares'):
        plot_series = df.loc[:,'cClassFlares'].rename('')
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')

    elif(graphName == 'mClassFlares'):
        plot_series = df.loc[:,'mClassFlares'].rename('')
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')
        
    elif(graphName == 'xClassFlares'):
        plot_series = df.loc[:,'xClassFlares'].rename('')
        plot_series.value_counts().plot.pie(autopct='%1.0f%%')


    plt.show() 


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Formats the size of the window
        tk.Frame.configure(self,bg="gray45")
        tk.Frame.configure(master,bg="gray45")
        master.geometry('{}x{}'.format(400, 600))




        tk.Label(self, text="Menu",bg="gray45", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Solar Flare Information",bg="gray45",
                  command=lambda: master.switch_frame(SolarFlareFrame)).pack()
        tk.Button(self, text="Graphs",bg="gray45",
                  command=lambda: master.switch_frame(GraphsFrame)).pack()
        tk.Button(self, text="Data Statistics",bg="gray45",
                  command=lambda: master.switch_frame(StatsFrame)).pack()        

class GraphsFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Formats the size of the window
        master.geometry('{}x{}'.format(400, 600))
        tk.Frame.configure(self,bg="gray45")
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


        name = tk.StringVar()
        
        #Add button
        self.logbtn = Button(self, text="Get Class", bg = "gray45", command=lambda: DisplayGraphs('class')).pack()
        self.logbtn = Button(self, text="Get Size", bg = "gray45", command=lambda: DisplayGraphs('size')).pack()
        self.logbtn = Button(self, text="Get Distribution", bg = "gray45", command=lambda: DisplayGraphs('distribution')).pack()
        self.logbtn = Button(self, text="Get activity", bg = "gray45", command=lambda: DisplayGraphs('activity')).pack()
        self.logbtn = Button(self, text="Get evolution", bg = "gray45", command=lambda: DisplayGraphs('evolution')).pack()
        self.logbtn = Button(self, text="Get previous_24_hours", bg = "gray45", command=lambda: DisplayGraphs('previous_24_hours')).pack()
        self.logbtn = Button(self, text="Get historical_complexity", bg = "gray45", command=lambda: DisplayGraphs('historical_complexity')).pack()
        self.logbtn = Button(self, text="Get become_complex", bg = "gray45", command=lambda: DisplayGraphs('become_complex')).pack()
        self.logbtn = Button(self, text="Get area", bg = "gray45", command=lambda: DisplayGraphs('area')).pack()
        self.logbtn = Button(self, text="Get area_of_largest_spot", bg = "gray45", command=lambda: DisplayGraphs('area_of_largest_spot')).pack()
        self.logbtn = Button(self, text="Get cClassFlares", bg = "gray45", command=lambda: DisplayGraphs('cClassFlares')).pack()
        self.logbtn = Button(self, text="Get mClassFlares", bg = "gray45", command=lambda: DisplayGraphs('mClassFlares')).pack()
        self.logbtn = Button(self, text="Get xClassFlares", bg = "gray45", command=lambda: DisplayGraphs('xClassFlares')).pack()


        self.pack()



#Run
if __name__ == "__main__":

    app = SampleApp()
    app.mainloop()