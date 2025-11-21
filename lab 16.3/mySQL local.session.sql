

SELECT b.title, b.author, l.loan_date, l.return_date
FROM Books b
JOIN Loans l ON b.book_id = l.book_id
WHERE l.member_id = 1; -- Replace 1 with desired member_id

-- Update book availability when borrowed
UPDATE Books 
SET available = FALSE 
WHERE book_id = 1; -- Replace ? with actual book_id

-- Delete member safely (only if they have no active loans)
DELETE FROM Members 
WHERE member_id = 1 
AND NOT EXISTS (
    SELECT 1 FROM Loans 
    WHERE member_id = Members.member_id 
    AND return_date IS NULL
);