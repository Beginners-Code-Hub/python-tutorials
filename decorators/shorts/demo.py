import time
from timer import timer

@timer
def slow_download():
    time.sleep(2)

@timer
def resize_images():
    time.sleep(1.2)

@timer
def send_report():
    time.sleep(0.1)

slow_download()
resize_images()
send_report()
