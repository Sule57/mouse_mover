import pyautogui
import time
import random
import argparse

def convert_to_seconds(timer_str):
    timer = 0
    time_units = {"h": 3600, "m": 60, "s": 1}

    for unit in time_units:
        if unit in timer_str:
            value = int(timer_str.split(unit)[0])
            timer += value * time_units[unit]

    return timer

def move_mouse_randomly(timer=None):
    try:
        start_time = time.time()

        while True:
            # Get the screen size
            screen_width, screen_height = pyautogui.size()

            # Generate random coordinates within the screen size
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)

            # Move the mouse to the random coordinates
            pyautogui.moveTo(x, y, duration=0.25)

            # Check if timer is provided and elapsed time exceeds the specified time
            if timer and (time.time() - start_time) >= timer:
                print("\nTimer expired. Exiting...")
                break

            # Wait for 5 seconds before the next move
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nScript interrupted. Exiting...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move the mouse randomly on the screen.")
    parser.add_argument("-t", "--timer", help="Set the timer in the format of 'XhYmZs'. E.g., '1h30m', '10s', '2h'")
    args = parser.parse_args()

    print("Welcome to:")
    print("___________________________")
    print("███    ███  ██████  ██    ██ ███████ ███████     ███    ███  ██████  ██    ██ ███████ ██████  ")
    print("████  ████ ██    ██ ██    ██ ██      ██          ████  ████ ██    ██ ██    ██ ██      ██   ██ ")
    print("██ ████ ██ ██    ██ ██    ██ ███████ █████       ██ ████ ██ ██    ██ ██    ██ █████   ██████  ")
    print("██  ██  ██ ██    ██ ██    ██      ██ ██          ██  ██  ██ ██    ██  ██  ██  ██      ██   ██ ")
    print("██      ██  ██████   ██████  ███████ ███████     ██      ██  ██████    ████   ███████ ██   ██ ")
    print("___________________________")
    print("by: Sul3")
    print("___________________________")

    if args.timer:
        timer = convert_to_seconds(args.timer)
        print(f"Running for {args.timer}.")
    else:
        timer = None
        print("Running indefinitely. Press Ctrl+C to stop.")

    move_mouse_randomly(timer)
