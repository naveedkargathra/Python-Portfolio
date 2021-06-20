import time

def countdown(t_seconds):
    while t_seconds:
        mins, secs = divmod(t_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end='\r')
        time.sleep(1)
        t_seconds -= 1

    print("Time Out!")

t_seconds = input("Enter time in seconds:")

countdown(int(t_seconds))