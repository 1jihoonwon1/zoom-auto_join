from genericpath import getatime
from tkinter import *
from tkinter import ttk
from backend import *
import tkinter as tk
from tkinter import messagebox


schedule_pending= 0
def gettime(z:zoom):
    st = int(z.start_time[0])*60 +int(z.start_time[1])
    zt = z.day*1500+st+z.while_time
    return zt


class schedule_list:
    def __init__(self):
        self.scheduel_list =[]
        self.order_list =[]
        
    def add(self,sche_info:list):
        z = zoom(*sche_info,is_on=is_on)
        zoom_time = gettime(z)
        index = self.add_index(z,zoom_time)
        z.id = zoom_time
        sche_info.append(zoom_time)
        self.scheduel_list.insert(index,z)

        # count = 0
        # size = len(self.scheduel_list)
        # for v in self.scheduel_list:
        #     if  size < count:
        #         mytree.insert("","end",iid=size,values=[])
        #         size +=1
        #     if index == count:
        #         mytree.set
        #     mytree.set(count-1,)
        mytree.insert(parent="",index=index,values=sche_info,iid=zoom_time)
        
        
    def add_index(self,zoo:zoom,zoom_time):
        zoom_time = gettime(zoo)
        self.order_list.append(zoom_time)
        self.order_list.sort()
        index = self.order_list.index(zoom_time)

        return index
        



        
        
        
sche = schedule_list()


            

root = Tk()
root.title('Azoom')

class time_set(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.hourstr=tk.StringVar(self,'10')
        self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=self.hourstr,width=2,state="readonly")
        self.minstr=tk.StringVar(self,'30')
        self.minstr.trace("w",self.trace_var)
        self.last_value = ""
        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=2,state="readonly")
        self.hour.grid()
        self.min.grid(row=0,column=1)

    def trace_var(self,*args):
        if self.last_value == "59" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
        self.last_value = self.minstr.get()

def  add():
    popup = Toplevel(root)
    popup.geometry("350x300")
    name ,url,while_time, = StringVar(),StringVar(),StringVar()
    Label(popup, text = "name : ").grid(row = 0, column = 0, padx = 10, pady = 10)
    Label(popup, text = "day : ").grid(row = 1, column = 0, padx = 10, pady = 10)
    Label(popup, text = "url : ").grid(row = 2, column = 0, padx = 10, pady = 10)
    Label(popup, text = "while time : ").grid(row = 3, column = 0, padx = 10, pady = 10)
    Label(popup, text = "start time : ").grid(row = 4, column = 0, padx = 10, pady = 10)

    Entry(popup, textvariable = name).grid(row = 0, column = 1, padx = 10, pady = 10)
    

    combobox = ttk.Combobox(popup,height=7,values=[
        "every.",
        "Sun.",
        "Mon.",
        "Tue.",
        "Wed.",
        "Thu.",
        "Fri",
        "Sat."
    ],state="readonly")
    combobox.current(0)
    combobox.grid(row = 1, column = 1)
    
    Entry(popup, textvariable = url).grid(row = 2, column = 1, padx = 10, pady = 10)
    Entry(popup, textvariable = while_time).grid(row = 3, column = 1, padx = 10, pady = 10)
    timeset = time_set(popup)
    timeset.grid(row = 4, column = 1, padx = 10, pady = 10)
    

    def add_sche():
        try:
            w = int(while_time.get())
        except:
            messagebox.showinfo('while_time error','"while time" is not integer')
        s = [timeset.hourstr.get().zfill(2),timeset.minstr.get().zfill(2)]

        sche_info =[name.get(),combobox.get(),url.get(),w,s]
        sche.add(sche_info)
        popup.destroy()
        
    Button(popup, text = "add", command =add_sche).grid(row = 5, column = 1, padx = 10, pady = 10)

click_index = None

def click(event):
    global click_index
    click_index = mytree.focus()
    



def cut():
    global click_index
    if click_index:
        print(click_index)
        id  = mytree.item(click_index).get('values')
        print(id)

        index = sche.order_list.index(id[5])
        print(index)
        print(sche.order_list)
        print(sche.scheduel_list)
        del sche.order_list[index]
        del sche.scheduel_list[index]
        print("-----------------")
        print(sche.order_list)
        print(sche.scheduel_list)
        mytree.delete(id[5])
        print(schedule.get_jobs())



        

    
    


b1 = Button(root, text='add',command=add)
b3 = Button(root, text='del',command=cut)
b1.grid(row=5, column=0,sticky='ew')
b3.grid(row=5, column=1,sticky='ew')


on = PhotoImage(file=f'{os.path.dirname(__file__)}/on.png')
off = PhotoImage(file=f'{os.path.dirname(__file__)}/off.png')

is_on = False
schedule_pending = run_pending()


def switch():
    global schedule_pending
    global is_on
    if is_on:
        onoff.config(image = off)
        is_on = False
        for i in sche.scheduel_list:
            i.cancel()
    else:
        for i in sche.scheduel_list:
            i.addschedule()
        onoff.config(image = on)
        is_on = True


onoff = Button(root,image=off,bd=0,command=switch)
onoff.grid(row=6,column=0,columnspan=2)


mytree= ttk.Treeview(root)
mytree['columns'] = ("name","day","url","while_time","start_time","select_id")
mytree.column('#0', width=0, stretch=NO)
mytree.column("name",width=150,anchor='center')
mytree.column("day",width=50,anchor='center')
mytree.column("url",width=300,anchor='center')
mytree.column("while_time",width=120,anchor='center')
mytree.column("start_time",width=120,anchor='center')
mytree.column("select_id",width=120,anchor="center")


mytree.heading('#0', text='', anchor=CENTER)
mytree.heading("name",text='name',anchor='center')
mytree.heading("day",text='day',anchor='center')
mytree.heading("url",text='url',anchor='center')
mytree.heading("while_time",text="while time",anchor='center')
mytree.heading("start_time",text="start time",anchor='center')
mytree.heading("select_id",text='select id',anchor="center")


mytree.grid(row=0,column=0,columnspan=2,sticky='ew')

mytree.bind('<ButtonRelease-1>',click)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        schedule_pending.set()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()
