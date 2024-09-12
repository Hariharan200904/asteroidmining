<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rover Control Panel</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Rover Control Panel</h1>

        <!-- Rover status -->
        <div class="status-box">
            <h2>Rover Status: <span id="rover-status">Stopped</span></h2>
        </div>

        <!-- Obstacle distance -->
        <div class="distance-box">
            <h2>Distance to Obstacle: <span id="distance">N/A</span> km</h2>
            <div class="progress-bar">
                <div id="progress" class="progress"></div>
            </div>
        </div>

        <!-- Control Panel -->
        <div class="control-panel">
            <button id="start-btn" class="control-btn">Start Rover</button>
            <button id="stop-btn" class="control-btn">Stop Rover</button>
        </div>

        <!-- Console for movements -->
        <div class="console">
            <h3>Rover Actions</h3>
            <ul id="action-log"></ul>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
