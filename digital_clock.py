#clock program 
import time 


n = int(input("Enter the time for timer in seconds "))
while(n>=0):
    minutes = (n // 60 )%60
    hours = n // 3600 
    seconds = n % 60 
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    if n == 0 : 
        break 
    time.sleep(1)
    n-=1

