
# ===== Pretty printing ========================================================

GRAY = "\u001b[38;5;248m"
CYAN = "\u001b[36m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
RESET = "\u001b[0m"


# ===== CSV output =============================================================


def saveDataToCSV(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for station in data:
            f.write(f"{station};{data[station]["average"]}\n")

    print(f"Data saved to {YELLOW}{filename}{RESET}.")
