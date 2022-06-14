# Topology API

An API library that gives the functionality to access, manage and store device topologies using objects.

<strong>Topology Specification:</strong>
A topology is a set of electronic components that are connected together.
Example [JSON file](./tests/topology.json).

For API documentation, refer to this [documentation](./api_documentation.md).

## Technologies used

* The API library is built using Node.js, JSON files are after all a Javascript object an Javascript tends to be one of the best languages in terms of effiecency to deal with these objects.

* If you don't have Node.js installed on your machine, you can install a local copy in the projects folder using Maven. (Installation can be viewed in the following [section](#environment-preparation))

* ESLint is used as a code analysis tool, so refer to it whenever you decide to edit the library.

* Basic API tests are located in the `tests` folder. (Usage can be viewed in the following [section](#environment-preparation))

## Environment preparation

In case Node.js isn't present on the current machine, Maven can be used to install a local copy of Node.js along with the required dependencies to run the API library. This can be done through running the following command line.

> `mvn clean install`

The output is as follows:
* 3 folders [ `node` , `bin` , `lib` ]
> `node` folder will contain executables for nodejs interpreter and npm. <br>
> `bin` folder will contain executable for eslint.

* The project can now make use of Node.js just by running `node/node <package name>`
> Note: Commands here are run from the root directory of the repository and using the local installation of the Node.js.

* For running basic tests:
> run: `node/node tests/test.js`

* For running eslint code analysis tool (Topology_API.js will be a test case):
> run: `bin/eslint Topology_API.js`
