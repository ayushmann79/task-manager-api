from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []
next_id = 1


@app.route("/")
def home():
    return jsonify({"message": "Task Manager API is running"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id

    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Title is required"}), 400

    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)
    next_id += 1

    return jsonify(task), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
