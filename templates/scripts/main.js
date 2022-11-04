var points = document.getElementById('pointsText');
var mainDB = document.getElementById("mainDBList");
var mainListItem = document.getElementsByClassName("mainListItem");
var dbContainer = document.getElementById("dbContainer");
var searchButtonDB = document.getElementById("searchButtonDB");
var search_Col = document.getElementById("search_Col");
var search_Type = document.getElementById("search_Type");

searchButtonDB.addEventListener("click",searchDB);

var allDB = [];

var cartData = [];

function assignPointText(pts) {
    points.textContent = pts;
}

function startPage() {
    eel.getPoints_py()(assignPointText);
    sortAll();
    eel.initDB_py()(initDB_js);
}

function initDB_js(lst) {
    allDB = lst;
}

function searchDB() {
    mainDB.innerHTML = "";
    let col = search_Col.value;
    let type = search_Type.value;
    eel.searchDB_py([col,type])(displayItems);
}

var msg = document.createElement("h1");
msg.className = "infoMSG";
msg.innerHTML = "You have added all items in this category to cart."

function displayItems(arr) {

    let n = arr.length;
    empty = true;
    for (let i = 0; i < n; i++) {
        let newID = arr[i][0] + "," + arr[i][1] + "," + arr[i][2];

        // create new list items
        var newItem = document.createElement("li");
        var newDiv = document.createElement("div");
        var newSpan = document.createElement("span");
        var newColl = document.createElement("h2");
        var newType = document.createElement("h2");
        var newPrice = document.createElement("h2");
        var newDivB = document.createElement("div");

        // Assign Class Names
        if (cartData.includes(newID)) {
            continue;
        }
        
        if (dbContainer.contains(msg)) {
            dbContainer.removeChild(msg);
        }
        newItem.id = newID+"div";
        newItem.className = "notCarted";
        newDiv.className = "dbItem";
        newColl.className = "collText";
        newType.className = "typeText";
        newPrice.className = "priceText";
        newDivB.className = "addCart";
        newDivB.id = newID;

        document.addEventListener('click',function(e){
            if(e.target && e.target.id == newID){
                  //do something
                  addtocartProcess(newID);
                  e.target.id = newID + "(added)";
             }
         });
        

        // Assign Contents
        newColl.innerHTML = arr[i][0];
        newType.innerHTML = arr[i][1];
        newPrice.innerHTML = arr[i][2];
        newDivB.innerHTML = "Add to Cart"

        // Append Children
        newSpan.appendChild(newColl);
        newSpan.appendChild(newType);
        newDiv.appendChild(newSpan);
        newDiv.appendChild(newPrice);
        newDiv.appendChild(newDivB);
        newItem.appendChild(newDiv);

        mainDB.appendChild(newItem);
        empty = false;
    }
    if (empty) {
        dbContainer.appendChild(msg);
    }
}

function sortAll() {
    mainDB.innerHTML = "";
    eel.initDB_py()(displayItems);
}

function sortSMG() {
    mainDB.innerHTML = "";
    eel.sortSMG_py()(displayItems);
}

function sortRifle() {
    mainDB.innerHTML = "";
    eel.sortRifle_py()(displayItems);
}

function sortShot() {
    mainDB.innerHTML = "";
    eel.sortShot_py()(displayItems);
}

function sortSniper() {
    mainDB.innerHTML = "";
    eel.sortSniper_py()(displayItems);
}

function sortMel() {
    mainDB.innerHTML = "";
    eel.sortMel_py()(displayItems);
}

function sortSidearms() {
    mainDB.innerHTML = "";
    eel.sortSidearms_py()(displayItems);
}

function sortHeavy() {
    mainDB.innerHTML = "";
    eel.sortHeavy_py()(displayItems);
}

function sortEdSelect() {
    mainDB.innerHTML = "";
    eel.sortEdSelect_py()(displayItems);
}

function sortEdDuxe() {
    mainDB.innerHTML = "";
    eel.sortEdDuxe_py()(displayItems);
}

function sortEdPrem() {
    mainDB.innerHTML = "";
    eel.sortEdPrem_py()(displayItems);
}

function sortEdEx() {
    mainDB.innerHTML = "";
    eel.sortEdEx_py()(displayItems);
}

function sortEdUltra() {
    mainDB.innerHTML = "";
    eel.sortEdUltra_py()(displayItems);
}

function addtocartProcess(newID) {
    var addedItem = document.getElementById(newID);
    var addedDiv = document.getElementById(newID+"div");
    addedItem.classList.add("addedCart");
    addedDiv.className = "addedCartDiv";
    cartData.push(newID);
}

function viewCart() {
    document.write(cartData);
}