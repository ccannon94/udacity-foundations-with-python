import time
import webbrowser

timesRun = 0
while(timesRun<3):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=QZHIxvFgevc")
	timesRun=timesRun + 1
