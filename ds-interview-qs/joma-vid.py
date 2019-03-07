#! usr/bin/env python3

"""From https://www.youtube.com/watch?v=4Z6lxfglvUU"""

Q1="""
SELECT AVG(video_duration)
FROM publisher_info
GROUP BY publisher_id;
"""

Q2="""
SELECT COUNT( DISTINCT publisher_id )
FROM publisher_info pi
  JOIN consumption_info ci ON pi.video_id = ci.video_id;
"""

