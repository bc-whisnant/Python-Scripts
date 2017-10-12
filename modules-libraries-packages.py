#modules, libraries and packages

#module is a .py file if you put two underscores before and after a module you can see its path
#example os __file__

#libraries - collection of numerous .py files - used the same way as modules

#packages - third party modules or libraries - do not come with default installation of python - these are installed
#pip install <package name>


#dates and times

#examples : create scripts that generate files automatically that are named by time and dates
#two modules - date time (manipulate dates) and time (time when script is executed)

import datetime
# print(datetime.datetime.now())

#difference between current time and specific time
yesterday = datetime.datetime(2017, 9, 4, 0, 0, 0)

today = datetime.datetime.now()

print(today - yesterday)
