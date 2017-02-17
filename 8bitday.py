#!/usr/bin/env python
import datetime
import os
import shutil

# https://www.reddit.com/r/wallpapers/comments/1tqe9k/update_new_version_of_the_8bit_day_wallpaper_set/

time = datetime.datetime.now().hour  # no need for string parsing to get the hour
     
# Gets out the new wallpaper based on time
if 0 <= time <= 5:
    shutil.copy('12-Late-Night.png', 'now.png')
elif 5 <= time <= 7:
    shutil.copy('01-Early-Morning.png', 'now.png')
elif 7 < time <= 10:
    shutil.copy('02-Mid-Morning.png', 'now.png')
elif 10 < time <= 11:
    shutil.copy('03-Late-Morning.png', 'now.png')
elif 11 < time <= 13:
    shutil.copy('04-Early-Afternoon.png', 'now.png')
elif 13 < time <= 15:
    shutil.copy('05-Mid-Afternoon.png', 'now.png')
elif 15 < time <= 16:
    shutil.copy('06-Late-Afternoon.png', 'now.png')
elif 16 < time <= 17:
    shutil.copy('07-Early-Evening.png', 'now.png')
elif 17 < time <= 18:
    shutil.copy('08-Mid-Evening.png', 'now.png')
elif 18 < time <= 19:
    shutil.copy('09-Late-Evening.png', 'now.png')    
elif 19 < time <= 21:
    shutil.copy('10-Early-Night.png', 'now.png')  
elif 21 < time <= 23:
    shutil.copy('11-Mid-Night.png', 'now.png')  

# Refreshes the desktop
os.system("xfdesktop --reload")
