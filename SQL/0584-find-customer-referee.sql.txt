-- LeetCode #584
-- Find Customer Referee
--
-- Find customers who were either:
-- 1. Referred by a customer whose id is not 2.
-- 2. Not referred by any customer.

SELECT name
FROM Customer
WHERE referee_id != 2
   OR referee_id IS NULL;