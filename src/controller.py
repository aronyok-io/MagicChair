print("MagicChair controller started")

speed = 1

command = input("Enter command: ").lower()

if command == "forward":
    print(f"MagicChair moving forward at speed {speed}")

elif command == "backward":
    print(f"MagicChair moving backward at speed {speed}")

elif command == "left":
    print("MagicChair turning left")

elif command == "right":
    print("MagicChair turning right")

elif command == "stop":
    print("MagicChair stopped")

elif command == "speed up":
    speed = min(speed + 1, 3)
    print(f"Speed level: {speed}")

elif command == "slow down":
    speed = max(speed - 1, 1)
    print(f"Speed level: {speed}")

else:
    print("Unknown command")
