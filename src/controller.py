MIN_SPEED = 0
MAX_SPEED = 3


def handle_command(command, speed):
    if command == "forward":
        if speed == 0:
            print("MagicChair is stopped. Increase speed to move forward.")
        else:
            print(f"MagicChair moving forward at speed {speed}")

    elif command == "backward":
        if speed == 0:
            print("MagicChair is stopped. Increase speed to move backward.")
        else:
            print(f"MagicChair moving backward at speed {speed}")

    elif command == "left":
        if speed == 0:
            print("MagicChair is stopped. Increase speed before turning.")
        else:
            print(f"MagicChair turning left at speed {speed}")

    elif command == "right":
        if speed == 0:
            print("MagicChair is stopped. Increase speed before turning.")
        else:
            print(f"MagicChair turning right at speed {speed}")

    elif command == "speed up":
        speed = min(speed + 1, MAX_SPEED)
        print(f"Speed level: {speed}")

    elif command == "slow down":
        speed = max(speed - 1, MIN_SPEED)

        if speed == 0:
            print("MagicChair has stopped")
        else:
            print(f"Speed level: {speed}")

    elif command == "stop":
        speed = 0
        print("Emergency stop activated")

    else:
        print("Unknown command")

    return speed


def main():
    print("MagicChair controller started")

    speed = 1

    while True:
        command = input("Enter command: ").lower().strip()

        if command == "exit":
            print("MagicChair controller shutting down")
            break

        speed = handle_command(command, speed)


if __name__ == "__main__":
    main()
