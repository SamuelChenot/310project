from tkinter import *
import tkinter.messagebox as tm
import tkinter.ttk as ttk
from PIL import ImageTk, Image

import numpy as np
import pandas as pandas
from matplotlib import pyplot as plt 

import tkinter as tk

graph = ""

def DisplayGraphs(graphName):

    assert(graphName != "")
    graph = graphName.get()
    x = np.arange(1,11) 
    y = 2 * x + 5 
    plt.title("Matplotlib demo") 
    plt.xlabel("x axis caption") 
    plt.ylabel("y axis caption") 
    plt.plot(x,y,"ob") 
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
        # self.photos = []
        # photo = ImageTk.PhotoImage(Image.open("But_Pics/all_mountains.png"))
        # self.photos.append(photo)
        # photo = ImageTk.PhotoImage(Image.open("But_Pics/nearby_mountains.png"))
        # self.photos.append(photo)
        # photo = ImageTk.PhotoImage(Image.open("But_Pics/saved_mountains.png"))
        # self.photos.append(photo)
        # photo = ImageTk.PhotoImage(Image.open("But_Pics/hourly_weather.png"))
        # self.photos.append(photo)
        # photo = ImageTk.PhotoImage(Image.open("But_Pics/user_info.png"))
        # self.photos.append(photo)



        tk.Label(self, text="Menu",bg="gray45", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Solar Flare Information",bg="gray45",
                  command=lambda: master.switch_frame(SolarFlareFrame)).pack()
        tk.Button(self, text="Graphs",bg="gray45",
                  command=lambda: master.switch_frame(GraphsFrame)).pack()
        tk.Button(self, text="Data Statistics",bg="gray45",
                  command=lambda: master.switch_frame(StatsFrame)).pack()        
        # tk.Button(self, text="Edit User Info",bg="gray45", image = self.photos[4],
        #           command=lambda: master.switch_frame(EditUserInfo)).pack()

        # self.photo = ImageTk.PhotoImage(Image.open("mountain.jpg"))
        # tk.Label(self, image = self.photo, compound="top").pack(side="top", fill="x", pady=5)

class GraphsFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Formats the size of the window
        master.geometry('{}x{}'.format(400, 600))
        tk.Frame.configure(self,bg="gray45")
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


        name = tk.StringVar()
        graphLabel = tk.Label(self, text="Enter Graph Wanted").pack()
        graphName = tk.Entry(self, textvariable = name).pack()
        
        #Add button
        self.logbtn = Button(self, text="Get Graph", bg = "gray45", command=lambda: DisplayGraphs(name)).pack()

        self.pack()



#Run
if __name__ == "__main__":

    app = SampleApp()
    app.mainloop()