## Social Media API - Posts and Comments

### Endpoints:

#### Posts:
- **List All Posts**: `GET /api/posts/`
- **Create a Post**: `POST /api/posts/` (Requires Authentication)
- **Retrieve a Post**: `GET /api/posts/{id}/`
- **Update a Post**: `PUT /api/posts/{id}/` (Requires Authentication and Ownership)
- **Delete a Post**: `DELETE /api/posts/{id}/` (Requires Authentication and Ownership)

#### Comments:
- **List All Comments**: `GET /api/comments/`
- **Create a Comment**: `POST /api/comments/` (Requires Authentication)
- **Retrieve a Comment**: `GET /api/comments/{id}/`
- **Update a Comment**: `PUT /api/comments/{id}/` (Requires Authentication and Ownership)
- **Delete a Comment**: `DELETE /api/comments/{id}/` (Requires Authentication and Ownership)

### Pagination:
- The posts and comments list endpoints support pagination.

### Filtering:
- You can filter posts by `title` or `content` using query parameters.
  Example: `/api/posts/?title=example`