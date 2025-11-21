-- Insert sample members
INSERT INTO Members (member_id, name, email, join_date) VALUES
(1, 'John Smith', 'john.smith@email.com', '2023-01-15'),
(2, 'Mary Johnson', 'mary.j@email.com', '2023-02-20'),
(3, 'David Brown', 'david.b@email.com', '2023-03-10');

-- Insert sample books
INSERT INTO Books (book_id, title, author, available) VALUES
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', true),
(2, 'To Kill a Mockingbird', 'Harper Lee', true),
(3, '1984', 'George Orwell', false);

-- Insert sample loans
INSERT INTO Loans (loan_id, member_id, book_id, loan_date, return_date) VALUES
(1, 1, 1, '2023-06-01', '2023-06-15'),
(2, 2, 2, '2023-06-05', '2023-06-19'),
(3, 3, 3, '2023-06-10', NULL);
