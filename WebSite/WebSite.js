const express 	 = require("express");
const dotenv 	 = require("dotenv").config();
const app 		 = express();

// Setting up the server
const host = process.env.HOST || "localhost";
const port = process.env.PORT || 8080;

// Setting up the route
app.get("/", function (req, res)
{
	res.send("Hello World!")
});

// Starting the server
app.listen(port, host, () => 
{
	console.log(`Server is running on http://${host}:${port}`);
});
