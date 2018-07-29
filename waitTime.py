import time
import webbrowser

total_breaks = 3
break_count = 0

print("This programs started on " + time.ctime())
while(break_count < total_breaks):
	time.sleep(10) 
	webbrowser.open("https://yh87714600.wixsite.com/mysite")
	break_count = break_count + 1

