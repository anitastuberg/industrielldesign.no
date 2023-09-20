let obj = [
    {"name": "Johanne", "antall": 2, "begrunnelse": "for sent ute med innkalling"}
    //{name:"", antall: 0, begrunnelse: " "}

]
let table = document.getElementById("prikksystem")
/*for(i = 0; i < antall_prikks.length; i++){
    let th = document.createElement("tr")
    console.log(antall_prikks[i])
    for(const key in antall_prikks[i]){
        let td = document.createElement("td")
        td.innerHTML = antall_prikks[i].key;
        th.appendChild(td)
    }
    table.appendChild(th)
}*/

for (var i = 0; i < obj.length; i++) {
    var tr = "<tr>";

    /* Verification to add the last decimal 0 */
    if (obj[i].value.toString().substring(obj[i].value.toString().indexOf('.'), obj[i].value.toString().length) < 2) 
        obj[i].value += "0";

    /* Must not forget the $ sign */
    tr += "<td>" + obj[i].key + "</td>" + "<td>$" + obj[i].value.toString() + "</td></tr>";

    /* We add the table row to the table body */
    tbody.innerHTML += tr;
}