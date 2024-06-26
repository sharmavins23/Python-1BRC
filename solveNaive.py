import time

from alive_progress import alive_bar

import utils

# ===== Driver code ============================================================


def main():
    # Store all values in a dictionary
    weatherStationStats = {}

    # Read through the lines in the CSV file
    with open("data/weatherData.csv", "r", encoding="utf-8") as f:
        with alive_bar(100_000_000) as bar:
            for line in f:
                # The line is stored as "Station;Temperature"
                station, temp = line.strip().split(";")

                # If the station is not in the dictionary, add it
                if station not in weatherStationStats:
                    weatherStationStats[station] = {
                        "min": temp,
                        "max": temp,
                        "sum": temp,
                        "count": 1
                    }
                # Otherwise, the station is in fact in the dictionary
                else:
                    # Increment the count
                    weatherStationStats[station]["count"] += 1
                    # Update the minimum temperature
                    weatherStationStats[station]["min"] = min(
                        weatherStationStats[station]["min"], temp)
                    # Update the maximum temperature
                    weatherStationStats[station]["max"] = max(
                        weatherStationStats[station]["max"], temp)
                    # Update the sum of all temperatures
                    weatherStationStats[station]["sum"] += temp

                bar()

    # At this point, we just have to compute averages
    for station in weatherStationStats:
        weatherStationStats[station]["average"] = weatherStationStats[station]["sum"] / \
            weatherStationStats[station]["count"]
    # Now sort them alphabetically
    sortedStations = sorted(weatherStationStats)

    # Simply call the util function to save the data to CSV
    utils.saveDataToCSV(sortedStations, "out/weatherStatsNaive.csv")


if __name__ == "__main__":
    # Time the main() function
    start = time.time()
    main()
    end = time.time()

    # Print the time taken
    print(f"Time taken: {utils.CYAN}{end - start:.2f}{utils.RESET} seconds.")
