-- Create the users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each user
    username TEXT UNIQUE NOT NULL,       -- Username (must be unique)
    hashed_password TEXT NOT NULL        -- Hashed password (store the hash, not the plain password)
);

-- Example of inserting a user (DO NOT store passwords like this in production)
-- In real applications, you would hash the password before inserting it
INSERT INTO users (username, hashed_password) VALUES ('testuser', '$2b$12$EXAMPLE_HASHED_PASSWORD');

-- Example of retrieving user data (for authentication on the server-side)
SELECT * FROM users WHERE username = 'testuser';

-- You would then compare the hashed password from the database with the hash of the password entered by the user.