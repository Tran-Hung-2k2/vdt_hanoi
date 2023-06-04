import scheduler
import time
import random
import  sys
from  Adafruit_IO import  MQTTClient

count = 0

IO_USERNAME =  "jackwrion12345"
IO_KEY = "aio_bisq78jFskfklOk7jb6e8hVAaSY4"


## MQTT MODULE
client = MQTTClient(IO_USERNAME , IO_KEY)
client.connect()
client.loop_background()



def Test():
    print("Hello\n")
def Test2():
    global count
    count += 1
    print ("Task2\n")

def mqtt_task_1():
    value = random.randint(0, 100)
    client.publish("bbc-led", value)
    print(value)

Sche = scheduler.Scheduler()
Sche.SCH_Init()

task1=Sche.SCH_Add_Task(Test, DELAY= 0, PERIOD=1000)
task2=Sche.SCH_Add_Task(Test2, DELAY= 0, PERIOD=1000)
task3 = Sche.SCH_Add_Task(mqtt_task_1, DELAY=0, PERIOD=5000)


while(1):
    Sche.SCH_Update()
    Sche.SCH_Dispatch_Tasks()
    
    if count == 5:
        Sche.SCH_Delete(task2)
        count += 1

    time.sleep(0.1)


