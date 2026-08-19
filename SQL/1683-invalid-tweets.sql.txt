-- LeetCode #1683
-- Invalid Tweets
--
-- Find tweets whose content contains more than 15 characters.

SELECT TWEET_ID FROM TWEETS
WHERE LENGTH(CONTENT) > 15;