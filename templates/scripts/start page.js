var startButton = document.getElementById('sButton');
var pointInput = document.getElementById('pointInput');
var errorDisplay = document.getElementById('errorInput');
var invalidOutput = "Invalid input. Please enter an appropriate integer.";

startButton.addEventListener('click',process);

function prepInput() {    
    pointInput.value = "";
    pointInput.style.color = 'black';
    
}

function checkinput(result) {
    if (result != "no") {
        window.location.replace("main.html");
    } else {
        errorDisplay.textContent = invalidOutput;
    }

}
function process() {
	let s = pointInput.value;
    eel.process_py(s)(checkinput)
}

function assignPointText(points) {
    document.getElementById('pointsText').textContent = points;
}

function getPoints() {
    eel.getPoints_py()(assignPointText);
}