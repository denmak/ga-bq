-- Mapping every event to its session
SELECT
      part
      ,TIMESTAMP_SECONDS(occurred_at) as ts
       ,CASE
       WHEN userAgent LIKE '%Android%' THEN 'android' -- Android|webOS|iPhone|iPad|iPod|BlackBerry
       WHEN userAgent LIKE '%webOS%' THEN 'webos' -- Android|webOS|iPhone|iPad|iPod|BlackBerry
       WHEN userAgent LIKE '%iPhone%' THEN 'iphone' -- Android|webOS|iPhone|iPad|iPod|BlackBerry
       WHEN userAgent LIKE '%iPad%' THEN 'ipad' -- Android|webOS|iPhone|iPad|iPod|BlackBerry
       WHEN userAgent LIKE '%iPod%' THEN 'ipod' -- Android|webOS|iPhone|iPad|iPod|BlackBerry
       WHEN userAgent LIKE '%BlackBerry%' THEN 'blackberry' -- Android|webOS|iPhone|iPad|iPod|BlackBerry
       WHEN userAgent LIKE '%Windows%' THEN 'windows' -- Android|webOS|iPhone|iPad|iPod|BlackBerry
       WHEN userAgent LIKE '%X11%' THEN 'x11' -- Android|webOS|iPhone|iPad|iPod|BlackBerry
       WHEN userAgent LIKE '%Macintosh%' THEN 'macintosh' -- Android|webOS|iPhone|iPad|iPod|BlackBerry
       ELSE 'Other'
   END OS
        ,clientId, type,global_session_id
        ,RANK() OVER (Partition by global_session_id ORDER BY  occurred_at) AS msg_num_global_session_id
        ,RANK() OVER (Partition by global_session_id ORDER BY  occurred_at DESC) AS msg_num_desc_global_session_id
       ,userId
       ,referralPath,campaign,source
       ,medium,userAgent,location,eventCategory
FROM(
SELECT clientId, type,last_event,occurred_at,
       SUM(is_new_session) OVER (ORDER BY clientId, occurred_at) AS global_session_id
       ,userId
       ,referralPath,campaign,source
       ,medium,userAgent,location,eventCategory
       ,part
  FROM (
       SELECT clientId, type,last_event,occurred_at, CASE WHEN occurred_at - last_event >= (60 * 10) OR last_event IS NULL THEN 1 ELSE 0 END AS is_new_session
       ,userId
       ,referralPath,campaign,source
       ,medium,userAgent,location,eventCategory
       ,part
         FROM (
              SELECT clientId, type, occurred_at, LAG(occurred_at,1) OVER (PARTITION BY clientId ORDER BY occurred_at) AS last_event
              ,userId
              ,referralPath,campaign,source
              ,medium,userAgent,location,eventCategory
              ,part
                FROM (
                     SELECT clientId,type,timestamp AS occurred_at,userId
                     ,trafficSource.referralPath,trafficSource.campaign,trafficSource.source
                     ,trafficSource.medium,device.userAgent,page.location,eventInfo.eventCategory
                     ,_PARTITIONTIME as part
                       FROM `{}.{}.{}`
                     ) pre
              ) last
       ) final

 ) as main
 ORDER BY 1,2