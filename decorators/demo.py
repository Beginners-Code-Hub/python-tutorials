import time
from decorators import timer

@timer
def load_users():
    time.sleep(0.3)

@timer
def resize_images():
    time.sleep(1.2)

@timer
def send_report():
    time.sleep(0.1)

load_users()
resize_images()
send_report()
