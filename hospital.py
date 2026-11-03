# Hospital Registration Token System


# Patient Class
class Patient:
    def __init__(self, token, name, age, phone):
        self.token = token
        self.name = name
        self.age = age
        self.phone = phone


# Hospital Class
class Hospital:

    def __init__(self):
        self.patients = {}       # Dictionary to store patients
        self.queue = []          # Waiting queue
        self.completed = []      # Completed consultations
        self.phone_numbers = set()  # Prevent duplicate phone numbers
        self.token_number = 1

    # Register Patient
    def register_patient(self, name, age, phone):

        # Check for duplicate phone number
        if phone in self.phone_numbers:
            print("Error: Phone number already registered!")
            return None

        # Generate token
        token = self.token_number

        # Create patient object
        patient = Patient(token, name, age, phone)

        # Store patient details
        self.patients[token] = patient

        # Add token to waiting queue
        self.queue.append(token)

        # Store phone number to prevent duplicates
        self.phone_numbers.add(phone)

        # Increase token number
        self.token_number += 1

        print("Patient registered successfully!")
        print("Token Number:", token)
        print("Patient Name:", name)

        return patient

    # Display Waiting Queue
    def display_queue(self):
        print("\n===== WAITING QUEUE =====")

        if len(self.queue) == 0:
            print("No patients are waiting.")

        else:
            for token in self.queue:
                patient = self.patients[token]

                print(
                    "Token:", patient.token,
                    "| Name:", patient.name,
                    "| Age:", patient.age
                )

    # Get Next Patient
    def get_next_patient(self):
        if len(self.queue) == 0:
            return None

        token = self.queue[0]
        return self.patients[token]

    # Complete Consultation
    def complete_consultation(self):
        if len(self.queue) == 0:
            print("No patients are waiting.")
            return None

        # Remove first patient from queue
        token = self.queue.pop(0)

        # Get patient details
        patient = self.patients[token]

        # Add patient to completed list
        self.completed.append(patient)

        print("\nConsultation completed successfully!")
        print("Token:", patient.token)
        print("Patient Name:", patient.name)

        return patient

    # Display Completed Consultations
    def display_completed(self):
        print("\n===== COMPLETED CONSULTATIONS =====")

        if len(self.completed) == 0:
            print("No completed consultations.")

        else:
            for patient in self.completed:
                print(
                    "Token:", patient.token,
                    "| Name:", patient.name
                )


# Main Program for Terminal Testing
if __name__ == "__main__":

    hospital = Hospital()

    while True:
        print("\n================================")
        print("    HOSPITAL TOKEN SYSTEM")
        print("================================")
        print("1. Register Patient")
        print("2. Display Waiting Queue")
        print("3. Display Next Patient")
        print("4. Complete Consultation")
        print("5. Display Completed Consultations")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            name = input("Enter patient name: ").strip()

            if not name:
                print("Patient name cannot be empty.")
                continue

            try:
                age = int(input("Enter patient age: "))

                if age < 1 or age > 120:
                    print("Enter an age between 1 and 120.")
                    continue

            except ValueError:
                print("Invalid age! Enter a number.")
                continue

            phone = input("Enter 10-digit phone number: ").strip()

            if not phone.isdigit() or len(phone) != 10:
                print("Enter a valid 10-digit phone number.")
                continue

            hospital.register_patient(name, age, phone)

        elif choice == "2":
            hospital.display_queue()

        elif choice == "3":
            patient = hospital.get_next_patient()

            if patient:
                print("\n===== NEXT PATIENT =====")
                print("Token:", patient.token)
                print("Name:", patient.name)
                print("Age:", patient.age)
            else:
                print("No patients are waiting.")

        elif choice == "4":
            hospital.complete_consultation()

        elif choice == "5":
            hospital.display_completed()

        elif choice == "6":
            print("Thank you for using the Hospital Token System!")
            break

        else:
            print("Invalid choice! Enter a number from 1 to 6.")