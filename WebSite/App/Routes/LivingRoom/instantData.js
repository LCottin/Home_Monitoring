const express   = require("express");
const path      = require("path");
const dotv      = require("dotenv").config();
const router    = express.Router();
const mysql     = require('mysql');

// Créer une connexion à la base de données MySQL
const connection = mysql.createConnection({
    host: process.env.HOST_DB,
    user: process.env.USER_DB,
    password: process.env.PASS_DB,
    database: process.env.NAME_DB
});

// Se connecter à la base de données
connection.connect();

router.get("/", function (req, res) {
    connection.query('SELECT * FROM LivingRoom ORDER BY id DESC LIMIT 1', function (error, results, fields) {
        if (error)
            throw error;

        const date = new Date(results[0].time * 1000);

        // Renvoyer les données au format JSON	
        res.render(path.resolve("Public/ejs/LivingRoom/instantData.ejs"), {
            timestamp: date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear() + " " + date.getHours() + ":" + date.getMinutes(),
            temperature: results[0].temperature,
            humidity: results[0].humidity,
            pressure: results[0].pressure,
        });
    });
});

router.get("/get_all", function (req, res) {
    connection.query('SELECT * FROM LivingRoom ORDER BY id DESC LIMIT 20', function (error, results, fields) {
        if (error)
            throw error;

        // Renvoyer les données au format JSON	
        res.statusCode = 200;
        res.set('Content-Type', 'application/javascript');
        res.json(results);
        res.end();
    });
});

router.get("/graph", function (req, res) 
{
    res.render(path.resolve("Public/ejs/LivingRoom/graph.ejs"));
});

module.exports = router;
