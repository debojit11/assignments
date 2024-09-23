# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

# Class to model an application form
class ApplicationForm:
    def __init__(self, name, age, address, medical_history):
        self.name = name
        self.age = age
        self.address = address
        self.medical_history = medical_history

    def __str__(self):
        return f"Patient: {self.name}, Age: {self.age}, Address: {self.address}, Medical History: {self.medical_history}"

# Instantiate some objects from the ApplicationForm class
if __name__ == '__main__':
    # Example forms filled by different patients
    patient1 = ApplicationForm("John Doe", 32, "123 Elm St", "Asthma")
    patient2 = ApplicationForm("Jane Smith", 28, "456 Oak St", "No known conditions")
    patient3 = ApplicationForm("Mike Johnson", 40, "789 Maple Ave", "Diabetes, High Blood Pressure")

    # Print the form information
    print(patient1)
    print(patient2)
    print(patient3)
