# This file looks to the csv for data, then populates that data to a graph.
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Sets up empty arrays. Will be populated with data from the csv file.
times = []
download = []
upload = []

# Open the csv file and start parsing data.
with open("./band_mon.csv", "r") as csvfile:
    # Puts the rows of csv file into variable plots. Delimiter used to separate fields.
    plots = csv.reader(csvfile, delimiter=",")
    # next(csvfile) skips the first line/row of headers. (Don't need them as data.)
    next(csvfile)
    # For every row, populate arrays with time, downspeed, upspeed date.
    for row in plots:
        # In plots, look at row and add to each each array. This will loop for however many
        # rows are in plots.
        times.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))

print(times, "\n", download, "\n", upload)

# This next code is matplotlib. Creates the graph.
plt.figure(30)
plt.plot(times, download, label="download", color="r")
plt.plot(times, upload, label="upload", color="b")
plt.xlabel("Time")
plt.ylabel("Speed (Mb/s)")
plt.title("Internet Speed")
plt.legend()
# Saves the data to a jpg file.
# bbox_inches="tight" removes extra white space around the figure.
plt.savefig("test_graph.jpg", bbox_inches="tight")