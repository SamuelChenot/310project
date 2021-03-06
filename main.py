from tkinter import *
import tkinter.messagebox as tm
import tkinter.ttk as ttk
from PIL import ImageTk, Image

import numpy as np
import pandas as pandas

from matplotlib import pyplot as plt
from tkinter.font import Font

import tkinter as tk

import pandas as pd
from treeviz import tree_print
from sklearn import tree
from sklearn.metrics import accuracy_score
# sklearn provides manipulation of training sets...here we do train/test split
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from bootstrap import bootstrap

df = pandas.read_csv("flare1.csv")
stats = df.describe()
stats.index.name = ''
stats.reset_index(inplace=True)

flareClass = ""
size = ""
distribution = ""
activity = ""
evolution = ""
previous_24_hours = ""
historical_complexity = ""
become_complex = ""
area = ""
area_of_largest_spot = ""
cClassFlares = ""
mClassFlares = ""
xClassFlares = ""

def predict(self, fit=None, features=None, probabilities=False):
        '''
        Predict the class labels (e.g., endmember types) based on an existing
        tree fit and new predictive features. Arguments:
            fit         The result of tree.DecisionTreeClassifier.fit(); uses
                        the last fit model if None.
            features    The new X array/ new predictive features to use;
                        should be (p x n), n samples with p features.
        '''
        if fit is None: fit = self.last_fit
        if features is None: features = self.x_features_array
        if probabilities:
            shp = self.y_raster.shape
            return fit.predict(features.T).T.reshape((self.n_labels, shp[1], shp[2]))

        return fit.predict(features.T).reshape(self.y_raster.shape) 

def predict_flare(flareClass, size, distribution, activity, evolution, previous_24_hours, historical_complexity, become_complex, area, area_of_largest_spot, cClassFlares, mClassFlares, xClassFlares):
    value = 0
    flareClass = int(str(flareClass.get()))
    size = int(str(size.get()))
    #reduced the size of the tree to make this easier
    if(size <= 1.5):
        value = 6
    elif(flareClass <= 0.5):
        if(size <= 2.5):
            value = 3
        else:
            value = 3
    elif(flareClass <= 1.5):
        value = 1
    else:
        value = 2
    

    

    popup = tk.Tk()
    popup.wm_title("Flare Predictor")

    B1 = ttk.Button(popup, text="Exit", command = popup.destroy)
    
    scrollbar = Scrollbar(popup)

    scrollbar.pack( side = RIGHT, fill = Y )

    info = Listbox(popup, yscrollcommand = scrollbar.set )
    info.insert(END, 'Flare Class: ' + str(value))

    info.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = info.yview )

class MsgPanel(ttk.Frame):
    def __init__(self, master, msgtxt):
        ttk.Frame.__init__(self, master)
        self.pack(side=TOP, fill=X)

        msg = Label(self, wraplength='4i', justify=LEFT)
        msg['text'] = ''.join(msgtxt)
        msg.pack(fill=X, padx=5, pady=5)


class SolarFlareFrame(tk.Frame):
    # class variable to track direction of column
    # header sort
    SortDir = True  # descending

    def __init__(self, isapp=True, name='mclistdemo'):
        tk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Multi-Column List Demo')
        self.isapp = isapp
        self._create_demo_panel()
        # Formats the size of the window
        self.master.geometry('{}x{}'.format(800, 1000))
        tk.Frame.configure(self, bg="gray45")
        tk.Button(self, text="Go back to start page",
                  command=lambda: self.master.switch_frame(StartPage)).pack()

    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)

        self._create_treeview(demoPanel)
        self._load_data()

    def _create_treeview(self, parent):
        f = tk.Frame(parent)
        f.pack(side=TOP, fill=BOTH, expand=Y)

        # create the tree and scrollbars
        self.dataCols = tuple(df.columns)
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')

        ysb = tk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        xsb = tk.Scrollbar(orient=HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set

        # add tree and scrollbars to frame
        self.tree.grid(in_=f, row=0, column=0, sticky=NSEW)
        ysb.grid(in_=f, row=0, column=1, sticky=NS)
        xsb.grid(in_=f, row=1, column=0, sticky=EW)

        # set frame resize priorities
        f.rowconfigure(0, weight=1)
        f.columnconfigure(0, weight=1)

    def _load_data(self):

        self.data = list(map(tuple, df.to_numpy()))

        # configure column headings
        for c in self.dataCols:
            self.tree.heading(c, text=c.title(),
                              command=lambda c=c: self._column_sort(c, MCListDemo.SortDir))
            self.tree.column(c, width=Font().measure(c.title()))

        # add data to the tree
        for item in self.data:
            self.tree.insert('', 'end', values=item)

            # and adjust column widths if necessary
            for idx, val in enumerate(item):
                iwidth = Font().measure(val)
                if self.tree.column(self.dataCols[idx], 'width') < iwidth:
                    self.tree.column(self.dataCols[idx], width=iwidth)

    def _column_sort(self, col, descending=False):

        # grab values to sort as a list of tuples (column value, column id)
        # e.g. [('Argentina', 'I001'), ('Australia', 'I002'), ('Brazil', 'I003')]
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]

        # reorder data
        # tkinter looks after moving other items in
        # the same row
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            self.tree.move(item[1], '', indx)  # item[1] = item Identifier

        # reverse sort direction for next sort operation
        MCListDemo.SortDir = not descending

def DisplayGraphs(graphName):

    options = ['class','size','distribution','activity','evolution','previous_24_hours','historical_complexity','become_complex','area','area_of_largest_spot','cClassFlares','mClassFlares','xClassFlares']

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
    # class variable to track direction of column header sort
    SortDir = True # descending

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.draw_MsgPanel()
        self.switch_frame(InitialPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        self._frame.master.title('Solar Flare Data')

    def draw_MsgPanel(self):
        MsgPanel(self,
                 ["This app is intended to display solar flare data ",
                  "the data you can currently see is class, size, distribution, activity",
                  "evolution, previous 24 hours, historical complexity, became complex, area",
                  "area of largest spot, number of C-class, M-class, and X-class flares.\n\n",
                  "Within the solar flare data tab we have the direct list of data available for the flare.",
                  "The app also contains pie charts of each value, with a data statistics page as well."])

        # self._create_demo_panel()


class InitialPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Formats the size of the window
        tk.Frame.configure(self,bg="gray45")
        tk.Frame.configure(master,bg="gray45")
        master.geometry('{}x{}'.format(800, 1000))

        self.photo = ImageTk.PhotoImage(Image.open("img/flare_start.jpg"))
        tk.Button(self, image = self.photo, compound="top",command=lambda: master.switch_frame(StartPage)).pack(side="top", fill="x", pady=5)


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Formats the size of the window
        tk.Frame.configure(self,bg="gray45")
        tk.Frame.configure(master,bg="gray45")
        master.geometry('{}x{}'.format(800, 1000))




        tk.Label(self, text="Solar Flares",bg="gray45", font=('Helvetica', 18, "bold"), padx=10, pady=10).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Solar Flare Data", bg="gray45", padx=10, pady=10,
                  command=lambda: master.switch_frame(SolarFlareFrame)).pack()
        self.logbtn = Label(self, bg="gray45").pack()
        tk.Button(self, text="Graphs", bg="gray45", padx=10, pady=10,
                  command=lambda: master.switch_frame(GraphsFrame)).pack()
        self.logbtn = Label(self, bg="gray45").pack()
        tk.Button(self, text="Data Statistics", bg="gray45", padx=10, pady=10,
                  command=lambda: master.switch_frame(StatsFrame)).pack()
        self.logbtn = Label(self, bg="gray45").pack()
        tk.Button(self, text="Flare Class Predictor", bg="gray45", padx=10, pady=10,
                  command=lambda: master.switch_frame(ClassPredictor)).pack()
        self.logbtn = Label(self, bg="gray45").pack()
        self.photo = ImageTk.PhotoImage(Image.open("img/flare_start.jpg"))
        tk.Label(self, image=self.photo, compound="top").pack(side="top", fill="x", pady=5)

class GraphsFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Formats the size of the window
        master.geometry('{}x{}'.format(800, 1000))
        tk.Frame.configure(self,bg="gray45")
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


        name = tk.StringVar()
        
        #Add button
        self.logbtn = Button(self, text="Get Class", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('class')).pack()
        self.logbtn = Button(self, text="Get Size", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('size')).pack()
        self.logbtn = Button(self, text="Get Distribution", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('distribution')).pack()
        self.logbtn = Button(self, text="Get activity", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('activity')).pack()
        self.logbtn = Button(self, text="Get evolution", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('evolution')).pack()
        self.logbtn = Button(self, text="Get previous_24_hours", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('previous_24_hours')).pack()
        self.logbtn = Button(self, text="Get historical_complexity", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('historical_complexity')).pack()
        self.logbtn = Button(self, text="Get become_complex", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('become_complex')).pack()
        self.logbtn = Button(self, text="Get area", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('area')).pack()
        self.logbtn = Button(self, text="Get area_of_largest_spot", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('area_of_largest_spot')).pack()
        self.logbtn = Button(self, text="Get cClassFlares", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('cClassFlares')).pack()
        self.logbtn = Button(self, text="Get mClassFlares", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('mClassFlares')).pack()
        self.logbtn = Button(self, text="Get xClassFlares", bg = "gray45", padx=5, pady=5, command=lambda: DisplayGraphs('xClassFlares')).pack()


        self.pack()

class StatsFrame(tk.Frame):
    # class variable to track direction of column
    # header sort
    SortDir = True  # descending

    def __init__(self, isapp=True, name='mclistdemo'):
        tk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Multi-Column List Demo')
        self.isapp = isapp
        self._create_demo_panel()
        # Formats the size of the window
        self.master.geometry('{}x{}'.format(800, 1000))

        tk.Frame.configure(self, bg="gray45")
        tk.Button(self, text="Go back to start page",
                  command=lambda: self.master.switch_frame(StartPage)).pack()

    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)

        self._create_treeview(demoPanel)
        self._load_data()

    def _create_treeview(self, parent):
        f = tk.Frame(parent)
        f.pack(side=TOP, fill=BOTH, expand=Y)

        # create the tree and scrollbars
        self.dataCols = tuple(stats.columns)
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')

        ysb = tk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        xsb = tk.Scrollbar(orient=HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set

        # add tree and scrollbars to frame
        self.tree.grid(in_=f, row=0, column=0, sticky=NSEW)
        ysb.grid(in_=f, row=0, column=1, sticky=NS)
        xsb.grid(in_=f, row=1, column=0, sticky=EW)

        # set frame resize priorities
        f.rowconfigure(0, weight=1)
        f.columnconfigure(0, weight=1)

    def _load_data(self):
        self.data = list(map(tuple, stats.to_numpy()))

        # configure column headings
        for c in self.dataCols:
            self.tree.heading(c, text=c.title(),
                              command=lambda c=c: self._column_sort(c, MCListDemo.SortDir))
            self.tree.column(c, width=Font().measure(c.title()))

        # add data to the tree
        for item in self.data:
            self.tree.insert('', 'end', values=item)

            # and adjust column widths if necessary
            for idx, val in enumerate(item):
                iwidth = Font().measure(val)
                if self.tree.column(self.dataCols[idx], 'width') < iwidth:
                    self.tree.column(self.dataCols[idx], width=iwidth)

    def _column_sort(self, col, descending=False):

        # grab values to sort as a list of tuples (column value, column id)
        # e.g. [('Argentina', 'I001'), ('Australia', 'I002'), ('Brazil', 'I003')]
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]

        # reorder data
        # tkinter looks after moving other items in
        # the same row
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            self.tree.move(item[1], '', indx)  # item[1] = item Identifier

        # reverse sort direction for next sort operation
        MCListDemo.SortDir = not descending

class ClassPredictor(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #Formats the size of the window
        master.geometry('{}x{}'.format(800, 1000))
        tk.Frame.configure(self,bg="gray45")
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

        flareClass = tk.StringVar()
        size = tk.StringVar()
        distribution = tk.StringVar()
        activity = tk.StringVar()
        evolution = tk.StringVar()
        previous_24_hours = tk.StringVar()
        historical_complexity = tk.StringVar()
        become_complex = tk.StringVar()
        area = tk.StringVar()
        area_of_largest_spot = tk.StringVar()
        cClassFlares = tk.StringVar()
        mClassFlares = tk.StringVar()
        xClassFlares = tk.StringVar()

        label_class = Label(self, text = 'Class').pack()
        flare_entry = tk.Entry(self, textvariable = flareClass).pack()

        label_size = Label(self, text = 'Size').pack()
        size_entry = tk.Entry(self, textvariable = size).pack()

        label_distribution = Label(self, text = 'Distribution').pack()
        distribution_entry = tk.Entry(self, textvariable = distribution).pack()

        label_activity = Label(self, text = 'Activity').pack()
        activity_entry = tk.Entry(self, textvariable = activity).pack()

        label_evolution = Label(self, text = 'Evolution').pack()
        evolution_entry = tk.Entry(self, textvariable = evolution).pack()

        label_previous_24_hours = Label(self, text = 'Previous 24 Hours').pack()
        previous_24_hours_entry = tk.Entry(self, textvariable = previous_24_hours).pack()

        label_historical_complexity = Label(self, text = 'historical_complexity').pack()
        historical_complexity_entry = tk.Entry(self, textvariable = historical_complexity).pack()

        label_become_complex = Label(self, text = 'become_complex').pack()
        become_complex_entry = tk.Entry(self, textvariable = become_complex).pack()

        label_area = Label(self, text = 'area').pack()
        area_entry = tk.Entry(self, textvariable = area).pack()

        label_area_of_largest_spot = Label(self, text = 'area_of_largest_spot').pack()
        area_of_largest_spot_entry = tk.Entry(self, textvariable = area_of_largest_spot).pack()

        label_cClassFlares = Label(self, text = 'cClassFlares').pack()
        cClassFlares_entry = tk.Entry(self, textvariable = cClassFlares).pack()

        label_mClassFlares = Label(self, text = 'mClassFlares').pack()
        mClassFlares_entry = tk.Entry(self, textvariable = mClassFlares).pack()

        label_xClassFlares = Label(self, text = 'xClassFlares').pack()
        xClassFlares_entry = tk.Entry(self, textvariable = xClassFlares).pack()


        self.logbtn = Button(self, text="Predict", bg = "gray45", command=lambda: predict_flare(flareClass, size, distribution, activity, evolution, previous_24_hours, historical_complexity, become_complex, area, area_of_largest_spot, cClassFlares, mClassFlares, xClassFlares)).pack()


        self.pack()
        

        

#Run
if __name__ == "__main__":
    SampleApp().mainloop()