## Posts & Comments API

### Endpoints

- GET /api/posts/
- POST /api/posts/
- GET /api/posts/{id}/
- PUT /api/posts/{id}/
- DELETE /api/posts/{id}/

- GET /api/comments/
- POST /api/comments/

### Authentication
Uses Token Authentication.
Include header:
Authorization: Token <your_token>

## Follow System & Feed

### Follow a User
POST /api/follow/{user_id}/

### Unfollow a User
POST /api/unfollow/{user_id}/

### User Feed
GET /api/feed/

Returns posts from users you follow, ordered by most recent.
Authentication required for all endpoints.
