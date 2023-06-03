# This is a sample Python script.                                                                                                                                       
                                                                                                                                                                        
# Press Shift+F10 to execute it or replace it with your code.                                                                                                           
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.                                                                      
from scheduler import *                                                                                                                                                 
from task1 import *                                                                                                                                                     
from task2 import *                                                                                                                                                     
from task3 import *                                                                                                                                                     
scheduler = Scheduler()    
task1 = Task1()                                                                                                                                             
task2 = Task2()                                                                                                                                             
task3 = Task3()                                                                                                                                             
scheduler.SCH_Init()                                                                                                                                                    
import time                                                                                                                                                             
                                                                                                                                                                        
def print_hi(name):                                                                                                                                                     
    # Use a breakpoint in the code line below to debug your script.                                                                                                     
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.                                                                                                     
scheduler.SCH_Add_Task(task1.Task1_Run, 2000, 5000)                                                                                                                                 
scheduler.SCH_Add_Task(task2.Task2_Run, 1000, 5000)                                                                                                                               
scheduler.SCH_Add_Task(task3.Task3_Run, 3000, 4000)                                                                                                                                  
while True:                                                                                                                                                             
    scheduler.SCH_Update()                                                                                                                                              
    scheduler.SCH_Dispatch_Tasks()                                                                                                                                      
    time.sleep(0.1)                                                                                                                                                     
# Press the green button in the gutter to run the script.                                                                                                               
if __name__ == '__main__':                                                                                                                                              
    print_hi('PyCharm')                                                                                                                                                 
                                                                                                                                                                        
# See PyCharm help at https://www.jetbrains.com/help/pycharm/ 