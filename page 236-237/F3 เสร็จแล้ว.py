import schedule
import webbrowser


# link youtube ที่ระบุไว้ในหนังสือเสียไปแล้ว จึงใช้ link ใหม่แทน

def job():
    webbrowser.open('https://www.youtube.com/watch?v=jMf9dV6I6Bw')


schedule.every(10).seconds.do(job)


while True:
    schedule.run_pending()
