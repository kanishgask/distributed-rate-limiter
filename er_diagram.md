# ER Diagram – Rate Limiter

USERS
- user_id

RATE_LIMITS
- user_id
- request_count
- window_start

Relationship:

User 1 → 1 Rate Limit Record
