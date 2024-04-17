# Print out the first 10 lines of the file data/weatherData.csv
with open("data/weatherData.csv", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        print(line.strip())
        if i == 9:
            break
