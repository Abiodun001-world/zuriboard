class ObstructionDetector {
    constructor(speed, distance) {
        this.speed = speed;
        this.distance = distance;
    }

    calculateExpectedTime() {
        const expectedTime = this.distance / this.speed;
        return expectedTime;
    }

    hasImpenetrableObstruction(actualTime, tolerance = 60) {
        const expectedTime = this.calculateExpectedTime();
        const timeDifference = actualTime - expectedTime;

        if (timeDifference > tolerance) {
            return true;
        } else {
            return false;
        }
    }
}

// Example usage
const actualTime = 78; // Simulated time from another module (in minutes)
const speed = 0.1; // Speed of the machine (in miles per minute)
const distance = 5.0; // Distance between points A and B (in miles)

// Create an instance of the ObstructionDetector class
const obstructionDetector = new ObstructionDetector(speed, distance);

// Check for impenetrable obstructions
const isImpenetrable = obstructionDetector.hasImpenetrableObstruction(actualTime);

if (isImpenetrable) {
    console.log("There is an impenetrable obstruction.");
} else {
    console.log("There is no impenetrable obstruction.");
}
