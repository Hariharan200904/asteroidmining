document.addEventListener('DOMContentLoaded', () => {
    const roverStatus = document.getElementById('rover-status');
    const distanceElement = document.getElementById('distance');
    const progressElement = document.getElementById('progress');
    const actionLog = document.getElementById('action-log');
    const startBtn = document.getElementById('start-btn');
    const stopBtn = document.getElementById('stop-btn');

    let intervalId = null;
    let isRoverRunning = false;

    // Start the rover simulation
    startBtn.addEventListener('click', () => {
        if (!isRoverRunning) {
            roverStatus.textContent = 'Running';
            isRoverRunning = true;

            intervalId = setInterval(() => {
                const distance = getSensorData();
                updateDistance(distance);

                if (distance < 5) {
                    addLog('Obstacle detected: Stopping and turning...');
                    stopRover();
                    setTimeout(() => {
                        const direction = Math.random() < 0.5 ? 'left' : 'right';
                        addLog(`Turning ${direction}`);
                        updateRoverStatus(`Turning ${direction}`);
                    }, 1000);
                } else {
                    moveForward(30);
                }
            }, 3000); // Simulating rover actions every 3 seconds
        }
    });

    // Stop the rover simulation
    stopBtn.addEventListener('click', () => {
        if (isRoverRunning) {
            clearInterval(intervalId);
            stopRover();
            isRoverRunning = false;
        }
    });

    // Simulate sensor data (random distance between 0 and 25 km)
    function getSensorData() {
        return (Math.random() * 25).toFixed(2);
    }

    // Update the distance and progress bar
    function updateDistance(distance) {
        distanceElement.textContent = distance;
        const progress = (distance / 25) * 100;
        progressElement.style.width = `${progress}%`;
        if (distance < 5) {
            progressElement.style.backgroundColor = 'red';
        } else {
            progressElement.style.backgroundColor = 'green';
        }
    }

    // Update rover status
    function updateRoverStatus(status) {
        roverStatus.textContent = status;
    }

    // Log actions in the console
    function addLog(message) {
        const li = document.createElement('li');
        li.textContent = message;
        actionLog.appendChild(li);
    }

    // Rover control functions
    function moveForward(speed) {
        addLog(`Moving forward at ${speed} km/h`);
        updateRoverStatus('Moving Forward');
    }

    function stopRover() {
        addLog('Rover stopped');
        updateRoverStatus('Stopped');
    }
});
