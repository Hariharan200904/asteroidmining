let interval;
let running = false;
let roverAngle = 0; // Initial angle of the rover
let roverX = 0;
let roverY = 0;

function getSensorData() {
    // Returns a simulated distance reading in centimeters
    return Math.random() * 100;
}

function moveForward(speed) {
    console.log(`Moving forward at speed ${speed}`);
    const rover = document.getElementById('rover');
    const angleInRadians = roverAngle * (Math.PI / 180);
    roverX += speed * Math.cos(angleInRadians);
    roverY += speed * Math.sin(angleInRadians);
    rover.style.transform = `translate(${roverX}px, ${roverY}px) rotate(${roverAngle}deg)`;
}

function turnRight(angle) {
    console.log(`Turning right by ${angle} degrees`);
    roverAngle += angle;
    roverAngle %= 360;
}

function stop() {
    console.log("Stopping the rover");
}

function startSimulation() {
    if (running) return;
    running = true;

    interval = setInterval(() => {
        const distance = getSensorData();
        document.getElementById('distance').innerText = `Distance to obstacle: ${distance.toFixed(2)} cm`;

        if (distance < 20) {
            stop();
            turnRight(90);
            setTimeout(() => {
                moveForward(10);
            }, 1000);
        } else {
            moveForward(10);
        }
    }, 1000);
}

function stopSimulation() {
    if (!running) return;
    clearInterval(interval);
    stop();
    running = false;
    document.getElementById('distance').innerText = "Simulation stopped";
}

document.getElementById('start-btn').addEventListener('click', startSimulation);
document.getElementById('stop-btn').addEventListener('click', stopSimulation);
