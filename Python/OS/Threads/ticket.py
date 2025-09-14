from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Shared resource
tickets_available = 10
lock = threading.Lock()

@app.route("/book", methods=["POST"])
def book_ticket():
    global tickets_available

    data = request.get_json()
    user = data.get("user")
    tickets_to_book = int(data.get("tickets", 1))

    with lock:  # Critical section (thread-safe)
        time.sleep(random.uniform(0.2, 0.8))  # Simulate processing delay

        if tickets_available >= tickets_to_book:
            tickets_available -= tickets_to_book
            result = {
                "status": "success",
                "message": f"{user} successfully booked {tickets_to_book} ticket(s).",
                "remaining_tickets": tickets_available
            }
        else:
            result = {
                "status": "failed",
                "message": f"Only {tickets_available} ticket(s) left. Cannot book {tickets_to_book}.",
                "remaining_tickets": tickets_available
            }

    return jsonify(result)

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"tickets_remaining": tickets_available})

if __name__ == "__main__":
    app.run(debug=True, threaded=True)