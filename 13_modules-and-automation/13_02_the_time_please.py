# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.
from datetime import datetime

current_time = datetime.now()

print(current_time.strftime("%Y-%m-%d %H:%M:%S"))