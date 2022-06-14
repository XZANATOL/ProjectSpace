# API Documentation

This documentation covers all the methods presents in the API library of `Topology_API.js` along with usage example of each and how to implement them into your code.

Index:
* [Importing API to your code](#importing-api-to-your-code)
* [printAll method](#printall-method)
* [readJSON method](#readjson-method)
* [writeJSON method](#writejson-method)
* [queryTopologies method](#querytopologies-method)
* [deleteTopology method](#deletetopology-method)
* [queryDevices method](#querydevices-method)
* [queryDevicesWithNetlistNode method](#querydeviceswithnetlistnode-method)

Note:

* Code here is run with considering the root directory of the repository as the current working directory.
* The API is designed to work with JSON of similair structure like this [example](./tests/topology.json).

<hr>

## Importing API to your code

First, We begin with importing the API to our code.<br>
<code>const api = require("./Topology_API.js")</code><br>
Following by declaring an instance or more to be used as an object.<br>
<code>var project_1 = new api.topology()</code>

Now, an object has been declared with the accessibility to its methods.

```
const api = require("./Topology_API.js")
var project_1 = new api.topology() // New object
var project_2 = new api.topology() // New object
var project_3 = new api.topology() // New object
```
<hr>

## printAll method

The method lies under `object.printAll()`. It takes no arguments, but returns a list with the current stored data in the memory.

On object initialization, the method returns an empty list.
```
const api = require("./Topology_API.js")
var project_1 = new api.topology()

console.log( project_1.printAll() ) // output: []
```
<hr>

## readJSON method

The method lies under `object.readJSON(path)`. It takes a path argument, to read a provided JSON file and add it's topology to the memory. In case of providing a valid JSON file, the function will return no output, else it will throw/exit with an error.
```
const api = require("./Topology_API.js")
var project_1 = new api.topology()

project_1.readJSON("./tests/topology.json") // No Output
project_1.readJSON("./non_existent_file.json") // Exits with error "Couldn't open JSON file!"
```

<hr>

## writeJSON method

The method lies under `object.writeJSON(id)`. It takes an id argument, to fetch the topology id from memory and extracts into a seperate json file named after the id topology. The function returns `1` if the topology was found, and `0` if not found. The function will throw an error if the topology was found but couldn't write the file.
```
const api = require("./Topology_API.js")
var project_1 = new api.topology()

project_1.readJSON("./tests/topology.json") // No Output

console.log( project_1.writeJSON("top1") ) // Output: 1
console.log( project_1.writeJSON("toprandom") ) // Output: 0

// Case the folder doesn't have write permissions
console.log( project_1.writeJSON("top1") ) // Exits with error "Topology found, but couldn't write the file!"
```

<hr>

## queryTopologies method

The method lies under `object.queryTopologies()`. It takes no arguments, but returns a list with the current stored topologies ids in the memory.

On object initialization, the method returns an empty list.
```
const api = require("./Topology_API.js")
var project_1 = new api.topology()

console.log( project_1.queryTopologies() ) // Output: []

project_1.readJSON("./tests/topology.json") // No Output

console.log( project_1.queryTopologies() ) // Output: ["top1"]
```

<hr>

## deleteTopology method

The method lies under `object.deleteTopology(id)`. It takes a topology id argument and deletes it from the memeory if exists. On successfull delete, the function returns an integer value of `1`, else `0`.
```
const api = require("./Topology_API.js")
var project_1 = new api.topology()

console.log( project_1.deleteTopology("top1") ) // Output: 0

project_1.readJSON("./tests/topology.json") // No Output

console.log( project_1.deleteTopology("top1") ) // Output: 1
```

<hr>

## queryDevices method

The method lies under `object.queryDevices(id)`. It takes a topology id argument and fetches it from the memory returning a list of devices ids inside this topology. It returns an empty list in case of topology id doesn't exist.
```
const api = require("./Topology_API.js")
var project_1 = new api.topology()

console.log( project_1.queryDevices("top1") ) // Output: []

project_1.readJSON("./tests/topology.json") // No Output

console.log( project_1.queryDevices("top1") ) // Output: ["res1", "m1"]
```

<hr>

## queryDevicesWithNetlistNode method

The method lies under `object.queryDevicesWithNetlistNode(topology_id, node_id)`. It take 2 arguments `topology_id` and `node_id`, to return are devices ids connected to the same Netlist Node id in a provided topology id. It returns an empty list if either arguments are invalid.
```
const api = require("./Topology_API.js")
var project_1 = new api.topology()

project_1.readJSON("./tests/topology.json") // No Output

console.log( project_1.queryDevicesWithNetlistNode("top1", "n5") ) // Output: []

console.log( project_1.queryDevicesWithNetlistNode("top1", "vin") ) // Output: ["m1"]
```

<hr>
