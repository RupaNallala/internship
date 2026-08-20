# Q78: Hospital Management System
class HospitalError(Exception):
    pass

doctors = {"Dr. Rao", "Dr. Priya"}

try:
    patient = input("Enter patient name: ").strip()
    if not patient:
        raise HospitalError("Invalid patient name.")

    doctor = input("Enter doctor name: ").strip()
    if doctor not in doctors:
        raise HospitalError("Doctor is unavailable.")

    date = input("Enter appointment date (DD-MM-YYYY): ").strip()
    if len(date) != 10 or date[2] != "-" or date[5] != "-":
        raise HospitalError("Invalid appointment date.")

    print("Appointment booked successfully.")
except HospitalError as e:
    print("Error:", e)
