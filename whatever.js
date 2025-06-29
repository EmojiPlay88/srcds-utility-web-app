function execcommand() {
    const command = document.getElementById("execcommand").value;
    const api_url = `http://127.0.0.1:5000/execcommand/${command}`;
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        document.getElementById("output").innerHTML = this.responseText;
    }
    xhttp.open("GET", api_url, true);
    xhttp.send();
}

function playerCount(playercount){
    document.getElementById("playercount").innerHTML = playercount;
}

function getStatus(){
    return new Promise((resolve, reject) => {
        const api_url = `http://127.0.0.1:5000/getstatus`;
        const xhttp = new XMLHttpRequest();
        xhttp.onload = function () {
            resolve(this.responseText)
        }

        xhttp.open("GET", api_url, true);
        xhttp.send();
    });
}

function hostname(hostname){
    document.getElementById("hostname").innerHTML = hostname;
}

async function onLoad() {
    const status = await getStatus();
    const statusData = JSON.parse(status)
    playerCount(statusData["players"]);
    hostname(statusData["hostname"].replaceAll("\\", ""));
}
