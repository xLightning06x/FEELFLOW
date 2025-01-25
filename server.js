const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcrypt');
const cors = require('cors');

const app = express();
const db = new sqlite3.Database('database.db');

app.use(cors());
app.use(express.json());

// User registration
app.post('/signup', (req, res) => {
    const { username, email, password } = req.body;
    const hashedPassword = bcrypt.hashSync(password, 10);

    db.run('INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)', [username, email, hashedPassword], function(err) {
        if (err) {
            return res.status(400).send("Error: Username or email already exists.");
        }
        res.status(201).send("User added successfully!");
    });
});

// User login
app.post('/login', (req, res) => {
    const { email, password } = req.body;

    db.get('SELECT * FROM users WHERE email = ?', [email], (err, row) => {
        if (err || !row) {
            return res.status(400).send("Invalid email or password.");
        }
        if (bcrypt.compareSync(password, row.hashed_password)) {
            res.send("Login successful!");
        } else {
            res.status(400).send("Invalid email or password.");
        }
    });
});

// Start the server
app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});