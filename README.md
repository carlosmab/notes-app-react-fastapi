### Notes App

## Backend: FastAPI (Python)

# Controller FastAPI
- Endpoints
| Method | URL       | Callback     |
| -----  | -----     | ------       |
| GET    | /         | get_routes   |
| GET    | /notes    | get_notes    |
| GET    | /notes/id | get_notes    |
| POST   | /notes    | add_note     |
| PATCH  | /notes/id | update_note  |
| DELETE | /notes/id | remove_note  |

# Database Mongo Atlas:
- Using PyMongo
- Model Notes (class)
  - create
  - find_by_id
  - update_one
  - remove_one

## Frontend React 