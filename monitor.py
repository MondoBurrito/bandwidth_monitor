import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.pyplot as ticker
import speedtest
import time

s = speedtest.Speedtest()

# Creates a csv in a folder.
with open("./bandwidth_monitor/band_mon.csv", mode="w") as speedcsv:
    # Set up csv with three headers and put into a variable.
    csv_writer = csv.DictWriter(speedcsv, fieldnames=["time", "downspeed", "upspeed"])
    csv_writer.writeheader()

    # Writes to csv every time every loop.
    while True:
        # Grabs the current time and formats it.
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        # Measures downspeed/upspeed and divides to get Mb/s. Rounds to 2 decimals.
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        # Prints to the terminal so I can see what's going on.
        print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
        # Write each loop into the csv file.        
        csv_writer.writerow({
            "time": time_now,
            "downspeed": downspeed,
            "upspeed": upspeed,
        })
        # Sets a refresh timer for 60 seconds. 
        time.sleep(60)
    