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
        plot_series.value_counts().plot.pie()

    elif(graphName == 'size'):

        plot_series = df.loc[:,'size'].rename('')
        plot_series.value_counts().plot.pie()
    
    elif(graphName == 'distribution'):

        plot_series = df.loc[:,'distribution'].rename('')
        plot_series.value_counts().plot.pie()
        
    elif(graphName == 'activity'):
        df.loc[:,'activity'].plot.kde()
        
    elif(graphName == 'evolution'):
        df.loc[:,'activity'].plot.kde()
        
    elif(graphName == 'previous_24_hours'):
        df.loc[:,'activity'].plot.kde()
        
    elif(graphName == 'historical_complexity'):
        df.loc[:,'activity'].plot.kde()
        
    elif(graphName == 'become_complex'):
        df.loc[:,'activity'].plot.kde()
        
    elif(graphName == 'area'):
        df.loc[:,'activity'].plot.kde()
        
    elif(graphName == 'area_of_largest_spot'):
        df.loc[:,'activity'].plot.kde()
        
    elif(graphName == 'cClassFlares'):
        df.loc[:,'activity'].plot.kde()

    elif(graphName == 'mClassFlares'):
        df.loc[:,'activity'].plot.kde()
        
    elif(graphName == 'xClassFlares'):
        df.loc[:,'activity'].plot.kde()

    # df.loc[:,'activity'].plot.kde()
    # df.loc[:,'activity'].plot.hist(bins=5)
    # df.loc[:,'activity'].value_counts().plot.bar()
    # df.loc[:,'activity'].value_counts().plot.pie()
    # df.plot.scatter(x='activity', y='evolution')
    #plt.figure(); df.plot(); plt.legend(loc='activity')

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