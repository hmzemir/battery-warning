import psutil
from plyer import notification
import time

battery = psutil.sensors_battery()
while True:
    percent = battery.percent
    notification.notify(
        title="Batarya Yüzdesi",
        message="%"+str(percent)+ " şarj kaldı!",
        timeout=50
        )
    time.sleep(10*10)
    continue