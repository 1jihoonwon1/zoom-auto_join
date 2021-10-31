import time
import webbrowser as wb
import os
import platform as pf
import schedule 
import threading
class zoom():
    def __init__(self,name:str,day:int,url:str,while_time:int,start_time:str,id=0,is_on=False):
        self.name = name
        self.day = day
        self.url = url
        self.while_time = while_time
        self.start_time =start_time
        self.schedule = 0
        self.id = id
        if is_on == True:
            self.add_schedule()
    
        

    def killzoom(self):
        time.sleep(self.while_time*60)
        if pf.system()=='Windows':
            os.system('taskkill /f /im zoom.us')
        else:
            print('ok')
            os.system('killall -9 zoom.us')
    def cancel(self):
        try:
            schedule.cancel_job(self.schedule)
        except:
            pass


    
    def openzoom(self):
        try:
            wb.open(self.url)
        except:
            print('opeen zoom error')
        if self.while_time:
            self.killzoom()
    def add_schedule(self):
        r = 0
        if self.day == "Sun.":
            r = schedule.every().sunday.at(self.start_time).do(self.openzoom)
        elif self.day == "Mon.":
            r = schedule.every().monday.at(self.start_time).do(self.openzoom)
        elif self.day == "Tue.":
            r = schedule.every().tuesday.at(self.start_time).do(self.openzoom)
        elif self.day == "Wed.":
            r = schedule.every().wednesday.at(self.start_time).do(self.openzoom)
        elif self.day == "Thu.":
            r = schedule.every().thursday.at(self.start_time).do(self.openzoom)
        elif self.day == "Fri.":
            r = schedule.every().friday.at(self.start_time).do(self.openzoom)
        elif self.day =="Sat.":
            r = schedule.every().saturday.at(self.start_time).do(self.openzoom)
        else:
            r = schedule.every().day.at(self.start_time).do(self.openzoom)
        self.schedule = r

def run_pending():
    runset = threading.Event()
    class scheduleThread(threading.Thread):
        def run(cls):
            while not runset.is_set():
                print(schedule.idle_seconds())
                schedule.run_pending()
                time.sleep(1)
    background = scheduleThread()
    background.start()
    return runset


    


    

