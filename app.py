from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]
 
# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    user_input = request.get_json()
    print(user_input['title'])
    event_id = max([event.id for event in events],default=0) + 1
    new_event = Event(event_id,user_input['title'])
    events.append(new_event)
    print(events)
    return jsonify(new_event.to_dict()),201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    new_title = request.get_json()
    event_to_update = next((e for e in events if e.id == event_id),None)
    if event_to_update:
        event_to_update.title = new_title['title']
        return jsonify(event_to_update.to_dict()),200
    else:
        return f'Event not found!',404

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events
    event_to_delete =  next((e for e in events if e.id == event_id),None)
    if event_to_delete:
        events = [event for event in events if event.id != event_id]
        return f'{event_to_delete.title} has been deleted!',204
    else:
        return f'Event not found!',404

if __name__ == "__main__":
    app.run(debug=True)
