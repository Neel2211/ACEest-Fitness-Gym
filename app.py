from flask import Flask, jsonify, request
import random

app = Flask(__name__)

clients = []

program_templates = {
    "Fat Loss": [
        "Full Body HIIT",
        "Circuit Training",
        "Cardio + Weights"
    ],
    "Muscle Gain": [
        "Push/Pull/Legs",
        "Upper/Lower Split",
        "Full Body Strength"
    ],
    "Beginner": [
        "Full Body 3x/week",
        "Light Strength + Mobility"
    ]
}

workouts = []


@app.route("/")
def home():
    return jsonify({
        "application": "ACEest Fitness & Gym",
        "status": "Running"
    })


@app.route("/clients", methods=["GET"])
def get_clients():
    return jsonify(clients)


@app.route("/clients", methods=["POST"])
def add_client():
    data = request.get_json()

    client = {
        "name": data["name"],
        "age": data.get("age", 0),
        "membership": "Active"
    }

    clients.append(client)

    return jsonify(client), 201


@app.route("/clients/<name>", methods=["GET"])
def get_client(name):
    for client in clients:
        if client["name"] == name:
            return jsonify(client)

    return jsonify({"message": "Client not found"}), 404


@app.route("/programs", methods=["GET"])
def get_programs():
    return jsonify(program_templates)


@app.route("/generate_program/<name>", methods=["POST"])
def generate_program(name):

    program_type = random.choice(list(program_templates.keys()))
    program = random.choice(program_templates[program_type])

    return jsonify({
        "client": name,
        "program_type": program_type,
        "program": program
    })


@app.route("/membership/<name>", methods=["GET"])
def membership(name):
    return jsonify({
        "client": name,
        "membership": "Active"
    })


@app.route("/workouts", methods=["POST"])
def add_workout():

    data = request.get_json()

    workout = {
        "client": data["client"],
        "workout_type": data["workout_type"],
        "duration": data["duration"]
    }

    workouts.append(workout)

    return jsonify(workout), 201


@app.route("/workouts/<name>", methods=["GET"])
def get_workouts(name):

    client_workouts = [
        w for w in workouts
        if w["client"] == name
    ]

    return jsonify(client_workouts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
