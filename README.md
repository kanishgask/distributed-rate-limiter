# 🚦 Distributed Rate Limiter

System Design Project – Backend Infrastructure

---

# Problem Statement

Design a distributed rate limiter to restrict how many requests a user can make within a time window.

Example:

100 requests per minute per user.

---

# Functional Requirements

- Limit API requests
- Support multiple users
- Fast decision making
- Scalable across servers

---

# Non Functional Requirements

- Low latency
- High availability
- Horizontal scalability
- Distributed coordination

---

# Rate Limiting Algorithms

• Token Bucket  
• Leaky Bucket  
• Fixed Window  
• Sliding Window

---

# High Level Architecture

Client
 ↓
API Gateway
 ↓
Rate Limiter
 ↓
Redis Store
 ↓
Application Server
