import pygetwindow as gw

print(gw.getAllTitles())


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