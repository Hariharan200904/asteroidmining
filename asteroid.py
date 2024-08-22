import random
import time

# Simulated sensor data
def get_sensor_data():
    # Returns a simulated distance reading in kilometers
    return random.uniform(0, 25)

# Move the rover forward
def move_forward(speed):
    print(f"Moving forward at speed {speed}")

# Move the rover backward
def move_backward(speed):
    print(f"Moving backward at speed {speed}")

# Turn the rover
def turn_left(angle):
    print(f"Turning left by {angle} degrees")

def turn_right(angle):
    print(f"Turning right by {angle} degrees")

# Stop the rover
def stop():
    print("Stopping the rover")

def main():
    try:
        while True:
            distance = get_sensor_data()
            print(f"Distance to obstacle: {distance} cm")

            if distance < 5:
                # Obstacle detected, stop and turn
                stop()
                turn_right(90)
                time.sleep(1)  # Wait for a second before moving again
                move_forward(40) #moving forward for 40 kilometer per hour
            else:
                move_forward()

            time.sleep(1)  # Adjust delay as needed
    except KeyboardInterrupt:
        stop()
        print("Program terminated by user")

if __name__ == "__main__":
    main()
