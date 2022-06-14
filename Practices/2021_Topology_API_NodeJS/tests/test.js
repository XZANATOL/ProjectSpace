const api = require("../Topology_API.js")
const fs = require("fs")
var ins

// Class level tests
try{
    ins = new api.topology()
    console.log("[+] Test 1: API Object import = SUCCESS")
}
catch(err){
    console.log("[-] Test 1: API Object import = FAILED")
    throw err
}


// API level tests
// readJSON endpoint
try{
    if (ins.readJSON("./tests/topology.json") == 1){
        console.log("[+] Test 2: Read 'topology.json' file = SUCCESS")
}}catch(err){
    console.log("[-] Test 2: Read 'topology.json' file = FAILED")
    throw err
}

// writeJSON endpoint
try{
    if (ins.writeJSON("top1") == 1){
        console.log("[+] Test 3: Extract 'top1' entry from memory to disk = SUCCESS")
        // Delete created file by the test process
        try{
        fs.unlinkSync("./top1.json")}
        catch{
        fs.unlinkSync("../top1.json")
        }
}}catch(err){
    console.log("[-] Test 3: Extract 'top1' entry from memory to disk = FAILED")
    throw err
}

// queryTopologies endpoint
var arr = ins.queryTopologies()
if( arr.length == 1 && arr[0] == "top1"){
    console.log("[+] Test 4: queryTopologies endpoint return valid list = SUCCESS")
}else{
    console.log("[-] Test 4: queryTopologies endpoint return valid list = FAILED")
}

// queryDevices endoint
var arr = ins.queryDevices("top1")
if (arr.length == 2 && arr[0] == "res1" && arr[1] == "m1"){
    console.log("[+] Test 5: queryDevices endpoint return valid list = SUCCESS")
}else{
    console.log("[-] Test 5: queryDevices endpoint return valid list = FAILED")
}

// queryDevicesWithNetlistNode endpoint
arr = ins.queryDevicesWithNetlistNode("top1", "n1")
if (arr.length == 2 && arr[0] == "res1" && arr[1] == "m1"){
    console.log("[+] Test 6: queryDevicesWithNetlistNode endpoint return valid list = SUCCESS")
}else{
    console.log("[-] Test 6: queryDevicesWithNetlistNode endpoint return valid list = FAILED")
}

// deleteTopology && printAll endpoints
var status = ins.deleteTopology("top1")
arr = ins.printAll()
if (status == 1 && arr == ""){
    console.log("[+] Test 6: deleteTopology && printAll endpoints return valid results = SUCCESS")
}else{
    console.log("[-] Test 6: deleteTopology && printAll endpoints return valid results = FAILED")
}

