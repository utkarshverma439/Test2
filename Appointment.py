'''from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Get form data
    name = request.form.get("name")
    age = request.form.get("age")
    sex = request.form.get("sex")
    problem = request.form.get("problem")

    # Store appointment details in a dictionary
    appointment = {
        "name": name,
        "age": age,
        "sex": sex,
        "problem": problem
    }

    # Save appointment details to a file
    with open("appointments.txt", "a") as f:
        f.write(f"{name},{age},{sex},{problem}\n")

    # Return a confirmation message to the user
    return f"Thank you for scheduling an appointment, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
'''
# Doctor Appointment Program

# Define a dictionary to store appointment details
appointment = {}

# Get user input for appointment details
appointment["name"] = input("What is your name? ")
appointment["age"] = int(input("What is your age? "))
appointment["sex"] = input("What is your sex? ")
appointment["problem"] = input("What is your problem/issue? ")

# Print appointment details for confirmation
print("Appointment details:")
print(f"Name: {appointment['name']}")
print(f"Age: {appointment['age']}")
print(f"Sex: {appointment['sex']}")
print(f"Problem/Issue: {appointment['problem']}")

# Save appointment details to a file
with open("appointments.txt", "a") as f:
    f.write(f"{appointment['name']},{appointment['age']},{appointment['sex']},{appointment['problem']}\n")

# Notify user that their appointment has been scheduled
print("Thank you for scheduling an appointment with us!")
