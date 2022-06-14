// Middle-ware for simplifying processing
const fs = require("fs")
Array.prototype.remove = function(from, to) {
  var rest = this.slice((to || from) + 1 || this.length);
  this.length = from < 0 ? this.length + from : from;
  return this.push.apply(this, rest);
};

class topology{
    // Initialize memory storage
    constructor(topologies){
        this.topologies = []
    }


    // Return all enteries endpoint
    printAll(){
        return this.topologies
    }


    // Read given topology endpoint
    readJSON(path){
        try{
            let rawdata = require(path)
            return this.topologies.push(rawdata)
        }catch{
            throw "Couldn't open JSON file!"
    }}


    // Write given topology id from memory to disk endpoint
    writeJSON(id){
        let found = 0
        for(var index=0; index < this.topologies.length; index++){
            if(this.topologies[index]["id"] == id){
                try{
                    found = 1
                    let data = JSON.stringify(this.topologies[index], null, 4)
                    fs.writeFileSync(this.topologies[index]["id"]+".json", data)
                    break // Stop further looping
                }catch{
                    throw "Topology found, but couldn't write the file!"
        }}}
        // Case: Topology not found!
        if(found == 0){
            return 0
        }else{
            return 1
    }}


    // Display available topologies endpoint
    queryTopologies(){
        var array = []
        for(var index=0; index < this.topologies.length; index++){
            array.push( this.topologies[index]["id"] )
        }
        return array
    }


    // Delete topology using topology id endpoint
    deleteTopology(id){
        for(var index=0; index < this.topologies.length; index++){
            if (this.topologies[index]["id"] == id)
                this.topologies.remove(index)
                return 1 // Case found
        }
        return 0 // Case not found
    }


    // Query about which devices are in a given topology endpoint
    queryDevices(id){
        var devices = []
        for(var index=0; index < this.topologies.length; index++){
            if(this.topologies[index]["id"] == id){
                // Loop on the existing components
                for(var i=0; i < this.topologies[index]["components"].length; i++){
                    devices.push(this.topologies[index]["components"][i]["id"])
                }
                break
        }}
        return devices
    }


    // Query about which devices are connected to a given netlist node in a given topology endpoint
    queryDevicesWithNetlistNode(top_id, node_id){
        var devices = []
        for(var index=0; index < this.topologies.length; index++){
            if(this.topologies[index]["id"] == top_id){
                // Loop on the existing components
                for(var i=0; i < this.topologies[index]["components"].length; i++){
                    // Loop on the exisiting connected nodes
                    for ( var key in this.topologies[index]["components"][i]["netlist"]){
                        if( this.topologies[index]["components"][i]["netlist"][key] == node_id)
                            devices.push( this.topologies[index]["components"][i]["id"])
                    }}
                break // Stop further looping on array
        }}
        return devices
    }
    
}


// Export API class to be used within other 3rd parties
module.exports = {
    "topology": topology
}
