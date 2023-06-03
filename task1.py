from scheduler import *
scheduler = Scheduler()

class Task1:                                                                                                                                                            
    def __init__(self):                                                                                                                                                 
        print("Init task 1")                                                                                                                                            
        return                                                                                                                                                          
                                                                                                                                                                        
    def Task1_Run(self):                                                                                                                                                
        print("Task 1 is activated!!!!")

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)