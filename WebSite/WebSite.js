const express 	 = require("express");
const dotenv 	 = require("dotenv").config();
const app 		 = express();

// Setting up the server
const host = process.env.HOST || "localhost";
const port = process.env.PORT || 8080;

// Importing routes
const LivingRoom = require("./App/Routes/LivingRoom/instantData");

// Setting up the static files
app.use(express.static(__dirname + "/Public/css"));
app.use(express.static(__dirname + "/src/LivingRoom"));
app.use(express.static(__dirname + "/Public/img"));

// Setting up the routes
app.use("/livingroom", LivingRoom);

// Setting up the entry point
app.get("/", function (req, res)
{
	res.sendFile(__dirname + "/Public/html/index.html");
});

// Starting the server
app.listen(port, host, () => 
{
	console.log(`Server is running on http://${host}:${port}`);
});
