function compute() {
    var data = document.getElementById("data").value
    eel.demo(data)(setValue) // call the demo function which we have created in the main.py file
}

function setValue(res) {
    document.getElementById("abc").src = res
}