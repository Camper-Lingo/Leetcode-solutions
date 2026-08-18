-- LeetCode #1148
-- Article Views I
--
-- Find authors who viewed at least one of their own articles.
-- Return the result table sorted by id in ascending order.

SELECT AUTHOR_ID AS ID FROM VIEWS
WHERE AUTHOR_ID = VIEWER_ID
GROUP BY ID
ORDER BY ID;