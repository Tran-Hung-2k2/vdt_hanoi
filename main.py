# This is a sample Python script.                                                                                                                                       
                                                                                                                                                                        
# Press Shift+F10 to execute it or replace it with your code.                                                                                                           
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.                                                                      
from scheduler import *                                                                                                                                                 
from task1 import *                                                                                                                                                     
from task2 import *                                                                                                                                                     
from task3 import *                                                                                                                                                     
scheduler = Scheduler()                                                                                                                                                 
scheduler.SCH_Init()                                                                                                                                                    
import time                                                                                                                                                             
                                                                                                                                                                        
def print_hi(name):                                                                                                                                                     
    # Use a breakpoint in the code line below to debug your script.                                                                                                     
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.                                                                                                     
scheduler.SCH_Add_Task(Task1, 2000, 1000)                                                                                                                                 
scheduler.SCH_Add_Task(Task2, 3000, 2000)                                                                                                                               
scheduler.SCH_Add_Task(Task3, 3000, 0)                                                                                                                                  
while True:                                                                                                                                                             
    scheduler.SCH_Update()                                                                                                                                              
    scheduler.SCH_Dispatch_Tasks()                                                                                                                                      
    time.sleep(0.1)                                                                                                                                                     
# Press the green button in the gutter to run the script.                                                                                                               
if __name__ == '__main__':                                                                                                                                              
    print_hi('PyCharm')                                                                                                                                                 
                                                                                                                                                                        
# See PyCharm help at https://www.jetbrains.com/help/pycharm/ 