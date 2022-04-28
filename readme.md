# Create card for a Task:
## Make a POST request to:

- curl -X POST "http://127.0.0.1:8000/api/v1/" -H "Content-Type: application/json" -d '{"type":"task", "title":"Is a task", "category":"cat1"}' 
