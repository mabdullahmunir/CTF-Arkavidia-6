CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    role INTEGER NOT NULL,
    secret_key VARCHAR(50) NOT NULL
);

INSERT INTO users (username, password, role, secret_key) VALUES ('admin', readfile('password.conf'), 1, readfile('secret.conf'));

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(127) NOT NULL,
    author VARCHAR(127) NOT NULL,
    description VARCHAR(300) NOT NULL,
    image VARCHAR(127) NOT NULL
);

INSERT INTO books (title, author, description, image) VALUES ('Applied Cryptography', 'Bruce Schneier', 'Praise for Applied Cryptography &quot;This book should be on the shelf of any computer professional involved in the use or implementation of cryptography.', '/static/assets/book/ac.jpg');
INSERT INTO books (title, author, description, image) VALUES ('Computer Networks: A Systems Approach', 'Larry L. Peterson, Bruce S. Davie', 'Computer Networks: A Systems Approach, Fifth Edition, explores the key principles of computer networking, with examples drawn from the real world of network and protocol design', '/static/assets/book/cn.jpg');
INSERT INTO books (title, author, description, image) VALUES ('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 'Turning the envelope over, his hand trembling, Harry saw a purple wax seal bearing a coat of arms; a lion, an eagle, a badger and a snake surrounding a large letter ''H''.', '/static/assets/book/hp1.jpg');
INSERT INTO books (title, author, description, image) VALUES ('Harry Potter and the Chamber of Secrets', 'J.K. Rowling', 'There is a plot, Harry Potter. A plot to make most terrible things happen at Hogwarts School of Witchcraft and Wizardry this year.', '/static/assets/book/hp2.jpg');

.exit
