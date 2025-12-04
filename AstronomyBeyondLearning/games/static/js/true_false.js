let timeLeft = 10;
let timerElement = document.getElementById("timer");

let countdown = setInterval(function() {
    timeLeft--;
    timerElement.textContent = timeLeft;

    if (timeLeft <= 0) {
        clearInterval(countdown);
        document.getElementById("timeUpForm").submit();
    }
}, 1000);
