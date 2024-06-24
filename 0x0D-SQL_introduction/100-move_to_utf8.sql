-- Convert the database hbtn_0c_0 to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- This script changes the character set and collation of the database hbtn_0c_0, the table first_table, and the field name in first_table

USE hbtn_0c_0;

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CHANGE name name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
