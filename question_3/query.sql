-- this query i tried to solve it, i googled the syntax for each column, for example, DATE or PERCENTILE COUNT
-- this way, i tried to look into the syntax and then tried to solve it,
-- the syntax for the daily_acc comes from the google, i tried to search, but it comes in ai overview,
-- so i'm writing it honestly
-- i spend alot of time on this task, but at least i tried to solve it,
-- but i learnt a lot tried solving this,
-- i kept the first version here, so you can see how i started and then where i go
-- i didn't tries to solve it 100 percent, because after so much time, i was still stuck
-- the main thing where i was stuck is to accuracy over a trailing 7 days and previous day accuracy
-- and based on that, the drift flag will also be calculated

-- Second Version
WITH DailyAcc AS (
    SELECT
        DATE(created_at) AS day,
        COUNT(*) AS n,
        ROUND( COUNT(CASE WHEN predicted = actual THEN 1 END) * 100.0 / COUNT(*), 2 ) AS daily_acc,
        PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY latency_ms) AS p95_latency,
    FROM interferences
)

SELECT
    day,
    n,
    daily_acc,
    P95_latency,
    -- CASE WHEN daily_acc > 10 THEN 'Yes' ELSE 'No' END AS is_greater_than_10 
    FROM interferences
WHERE n >= 100
GROUP BY DATE(created_at)
ORDER BY model_name, day


-- First Version
SELECT
    DATE(created_at) AS day,
    COUNT(*) AS n,
    ROUND( COUNT(CASE WHEN predicted = actual THEN 1 END) * 100.0 / COUNT(*), 2 ) AS daily_acc,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY latency_ms) AS p95_latency,
FROM interferences
WHERE n >= 100
GROUP BY DATE(created_at)
ORDER BY model_name, day