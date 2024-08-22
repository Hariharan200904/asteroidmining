import random
import time

# Simulated sensor data
def get_sensor_data():
    # Returns a simulated distance to surface and temperature reading
    return {
        "distance_to_surface": random.uniform(0, 100),  # Distance in meters
        "temperature": random.uniform(-200, 100),       # Temperature in Celsius
    }

class MiningRobot:
    def __init__(self, id):
        self.id = id
        self.mining_status = False
        self.battery_level = 100  # Simulated battery level

    def start_mining(self):
        if self.battery_level > 20:  # Ensure there's enough battery to mine
            self.mining_status = True
            print(f"Robot {self.id} started mining.")
        else:
            print(f"Robot {self.id} battery too low to start mining.")

    def stop_mining(self):
        self.mining_status = False
        print(f"Robot {self.id} stopped mining.")

    def send_data(self):
        sensor_data = get_sensor_data()
        return {
            "robot_id": self.id,
            "mining_status": self.mining_status,
            "sensor_data": sensor_data,
            "battery_level": self.battery_level,
        }

    def recharge_battery(self):
        self.battery_level = 100
        print(f"Robot {self.id} battery recharged.")

class CentralController:
    def __init__(self):
        self.robots = [MiningRobot(i) for i in range(1, 4)]  # Initialize 3 robots

    def monitor_robots(self):
        while True:
            for robot in self.robots:
                data = robot.send_data()
                print(f"Robot {data['robot_id']} data: {data}")
                if data['sensor_data']['distance_to_surface'] < 10:
                    robot.stop_mining()
                    print(f"Obstacle detected by Robot {robot.id}.")
                elif data['battery_level'] < 20:
                    robot.stop_mining()
                    print(f"Robot {robot.id} battery low.")
            time.sleep(5)  # Delay for simulation purposes

if __name__ == "__main__":
    controller = CentralController()
    controller.monitor_robots()
