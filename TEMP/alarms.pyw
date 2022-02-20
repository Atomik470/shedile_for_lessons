
import plyer, time
from winsound import Beep

# Ф-ия вывода уведомления вин 10
def alarm(title_alarm, app_name, text):
    title_alarm = str(title_alarm)
    app_name = str(app_name)
    text = str(text)
    Beep(688, 350)
    plyer.notification.notify(message=text,
                              app_name=app_name, 
                              title=title_alarm)
    
    
# Ф-ия получени текущей даты
def current_data_time():
    current_data = time.asctime().split()
    current_data = (current_data[0] +" "+ current_data[3].split(":")[0] +":" +current_data[3].split(":")[1])
    return(current_data)


# Ф-ия чтения расписания и заданий из файла
def read_shedule(file_name):
    f = open(file_name, 'r', encoding="utf-8")
    inp = f.read().split("\n")
    return(inp)


def main():
    time_tasks = read_shedule("schedule.txt")
    while True:
        if current_data_time() in time_tasks:
            task = time_tasks[time_tasks.index(current_data_time())+1].split("/")
            alarm(task[0], " ", task[1])
            time.sleep(60)
        else:
            time.sleep(5)
    
    #timer()
    
if __name__ == "__main__":
    main()