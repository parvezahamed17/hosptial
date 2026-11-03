from flask import Flask, render_template, request, redirect, url_for, flash
from hospital import Hospital

app = Flask(__name__)

# Secret key for displaying messages
app.secret_key = "hospital_token_demo_key"

# Create hospital object only once
hospital = Hospital()


# Home Page
@app.route("/")
def home():

    waiting_patients = []

    # Get all waiting patients
    for token in hospital.queue:
        patient = hospital.patients[token]
        waiting_patients.append(patient)

    # Get next patient
    next_patient = hospital.get_next_patient()

    return render_template(
        "index.html",
        waiting=waiting_patients,
        next_patient=next_patient,
        completed=hospital.completed
    )


# Register Patient
@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name", "").strip()
    age_text = request.form.get("age", "").strip()
    phone = request.form.get("phone", "").strip()

    # Check name
    if not name:
        flash("Please enter the patient name.")
        return redirect(url_for("home"))

    # Check age
    try:
        age = int(age_text)
    except ValueError:
        flash("Please enter a valid age.")
        return redirect(url_for("home"))

    if age < 1 or age > 120:
        flash("Age must be between 1 and 120.")
        return redirect(url_for("home"))

    # Check phone number
    if not phone.isdigit() or len(phone) != 10:
        flash("Enter a valid 10-digit phone number.")
        return redirect(url_for("home"))

    # Register patient
    patient = hospital.register_patient(name, age, phone)

    # Check whether registration succeeded
    if patient is None:
        flash("This phone number is already registered!")
    else:
        flash(
            f"Patient registered successfully! Token number: {patient.token}"
        )

    return redirect(url_for("home"))


# Complete Consultation
@app.route("/complete", methods=["POST"])
def complete():

    patient = hospital.complete_consultation()

    if patient is None:
        flash("No patients are waiting for consultation.")
    else:
        flash(
            f"Consultation completed for {patient.name}, "
            f"Token {patient.token}."
        )

    return redirect(url_for("home"))


# Run Website
if __name__ == "__main__":
    app.run(debug=True)