import os
import random

from alive_progress import alive_bar

import utils

# ===== Driver code ============================================================


def main():
    # Seed the RNG for reproducibility
    random.seed(23)

    # Start by consuming the CSV weather station data
    weatherStationLatitudes = {}
    with open("data/weatherStations.csv", "r", encoding="utf-8") as f:
        for line in f:
            # Lines are formatted as "Station;Latitude"
            station, latitude = line.strip().split(";")
            weatherStationLatitudes[station] = float(latitude)

    print(f"Loaded {utils.CYAN}{len(weatherStationLatitudes)}{
          utils.RESET} weather stations.")

    print("Creating weather data...")

    # Saving so as to not recompute every single time
    listOfKeys = list(weatherStationLatitudes.keys())

    # Delete the weather data file if it exists
    try:
        os.remove("data/weatherData.csv")
        print("Removed previous weather data file.")
    except FileNotFoundError:
        pass

    # Create a file to store the generated data
    with open("data/weatherData.csv", "w", encoding="utf-8") as f:
        f.write("Station;Temperature;Date\n")

        # Iterate 100 million times
        oneHundredMn = 100_000_000
        with alive_bar(oneHundredMn) as bar:
            for i in range(oneHundredMn):
                # Pick a random weather station
                station = random.choice(listOfKeys)

                # A colder temperature occurs at a higher latitude
                tempC = 20 - \
                    abs(weatherStationLatitudes[station]
                        ) / 10 + random.uniform(-5, 5)

                # Write the data to the file
                f.write(f"{station};{tempC}\n")

                bar()

    print("Done!")


if __name__ == "__main__":
    main()
