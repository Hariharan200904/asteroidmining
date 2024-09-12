let robots = [
    { id: 1, mining: false, battery: 100 },
    { id: 2, mining: false, battery: 100 },
    { id: 3, mining: false, battery: 100 }
];

function renderRobots() {
    const robotContainer = document.getElementById('robots');
    robotContainer.innerHTML = '';
    robots.forEach(robot => {
        const robotElement = document.createElement('div');
        robotElement.className = 'robot';
        robotElement.innerHTML = `
            <p>Robot ${robot.id}</p>
            <p>Battery: ${robot.battery}%</p>
            <p>Mining: ${robot.mining ? 'Yes' : 'No'}</p>
        `;
        robotContainer.appendChild(robotElement);
    });
}

function startMining() {
    robots.forEach(robot => {
        if (robot.battery > 20) {
            robot.mining = true;
        }
    });
    renderRobots();
}

function stopMining() {
    robots.forEach(robot => {
        robot.mining = false;
    });
    renderRobots();
}

document.getElementById('start-btn').addEventListener('click', startMining);
document.getElementById('stop-btn').addEventListener('click', stopMining);

setInterval(() => {
    robots.forEach(robot => {
        if (robot.mining && robot.battery > 0) {
            robot.battery -= 5; // Simulate battery drain
            if (robot.battery < 20) {
                robot.mining = false; // Stop mining if battery too low
            }
        }
    });
    renderRobots();
}, 1000);

renderRobots();
