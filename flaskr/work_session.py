import pygetwindow as gw
import time as t

class work_session:
    

    # constructor
    def __init__(self, work_list, app_list, name, session_goals):
        # url variables
        self.specified_work_urls = work_list

        # app variables
        self.specified_app_list = app_list

        # stopwatch variables
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

        self.name = name
        self.session_goals = session_goals


    def start_work_timer():
        # first check if any common 
        # non-work tabs or applications are open
        non_work_tabs = []
        non_app_tabs = []





    
        


# list of tabs we want to be on
# these are usual appications and windows open for school and work
list_of_titles = ['Homepage - Dalhousie University - Google Chrome',
                  'ChatGPT - Google Chrome']

def check_tab():
    list_of_active_titles = gw.getAllTitles()
    for title in list_of_titles:
        if title in list_of_active_titles:
            print(title + " is active")


check_tab()



