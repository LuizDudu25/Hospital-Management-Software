import os

class Patient:
    def __init__(self, name, cpf, age, gender, contact):
        self.name = name
        self.cpf = cpf
        self.age = age
        self.gender = gender
        self.contact = contact
        self.medical_records = []
        self.bills = []
        self.invoicing = 0.0
        self.prescriptions = []
        self.lab_tests = []
        self.exams = []
        self.ward = None

    def update_info(self):
        print(f"\nName: {self.name}")
        choice = input("Change patient's name? (Y/N) ")
        if choice == 'Y':
            self.name = input("Patient's name: ")
        
        print(f"\nCPF: {self.cpf}")
        choice = input("Change patient's CPF? (Y/N) ")
        if choice == 'Y':
            self.cpf = input("Patient's CPF: ")
        
        print(f"\nAge: {self.age}")
        choice = input("Change patient's age? (Y/N) ")
        if choice == 'Y':
            self.age = input("Patient's age: ")

        print(f"\nGender: {self.gender}")
        choice = input("Change patient's gender? (Y/N) ")
        if choice == 'Y':
            self.gender = input("Patient's gender: ")

        print(f"\nContact: {self.cpf}")
        choice = input("Change patient's contact? (Y/N) ")
        if choice == 'Y':
            self.contact = input("Patient's contact: ")
    
    def book_exam(self, date, doctor):
        self.exams.append({"date": date, "doctor": doctor})
    
    def cancel_exam(self, date, doctor):
        self.exams.remove({"date": date, "doctor": doctor})
    
    def reeschedule_exam(self, cdate, ndate, doctor):
        for appointment in self.exams:
            if appointment["date"] == cdate and appointment["doctor"] == doctor:
                appointment["date"] = ndate

    def add_record(self):
        record = input("Type the medical record to be added:\n")
        if record not in self.medical_records:
            self.medical_records.append(record)
            print("\nMedical record successfully added")
        else:
            print("\nMedical record already added")
        
        choice = input("Do you wish to add another record? (Y/N) ")

        if choice.upper() == 'Y':
            self.add_record()
        else:
            return

    def register_bill(self, amount):
        self.bills.append(amount)
        self.invoicing += amount

    def add_prescription(self):
        record = input("Type the prescription to be added:\n")
        if record not in self.medical_records:
            self.medical_records.append(record)
            print("\nPrescription successfully added")
        else:
            print("\nPrescription already added")
        
        choice = input("Do you wish to add another prescription? (Y/N) ")

        if choice == 'Y':
            self.add_prescription()
        else:
            return

    def order_lab_test(self, test):
        self.exams.append({"test": test, "doctor": "No results yet"})

    def lab_tests_results(self, test):
        for lab_test in self.lab_tests:
            if lab_test["test"] == test:
                result = input("Type the result of the lab test: ")
                lab_test["result"] = result

    def print_main(self):
        print(f"\nName: {self.name}")
        print(f"CPF: {self.cpf}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact: {self.contact}")
    
    def print_schedule(self):
        if self.exams:
            for item in self.exams:
                print(f"- {item['doctor']}, {item['date']}")
        else:
            print("No exams scheduled")
    
    def print_medical_records(self):
        if self.medical_records:
            for item in self.medical_records:
                print(f"- {item}")
        else:
            print("No medical records registered")

    def print_bills(self):
        if self.bills:
            for item in self.bills:
                print(f"- {item}")
        else:
            print("No bills registered")
        print(f"Total: R$ {self.invoicing:.2f}")

    def print_prescriptions(self):
        if self.prescriptions:
            for item in self.prescriptions:
                print(f"- {item}")
        else:
            print("No medical records registered")

    def print_lab_tests(self):
        if self.lab_tests:
            for item in self.lab_tests:
                print(f"- {item['test']}\n  {item['result']}")
        else:
            print("No lab tests ordered")

    def print_info(self):
        os.system('clear')
        print("\n=== Patient Profile ===")

        self.print_main()

        if self.ward:
            print(f"Ward: {self.ward}")
        else:
            print("Patient not allocated in a ward")
        
        print("\n--- Medical Records ---\n")
        self.print_medical_records()
        print("\n--- Bills and Invoicing ---\n")
        self.print_bills()
        print("\n--- Prescriptions ---\n")
        self.print_prescriptions()
        print("\n--- Lab Tests ---\n")
        self.print_lab_tests()
        print("\n--- Exams ---\n")
        self.print_schedule()

        print("==============================\n")

class Employee:
    def __init__(self, name, cpf, function):
        self.name = name
        self.cpf = cpf
        self.function = function
        self.shifts = []
        self.schedule = []
        self.exams = []
    
    def book_exam(self, date, patient):
        self.exams.append({"date": date, "patient": patient})
    
    def cancel_exam(self, date, patient):
        self.exams.remove({"date": date, "patient": patient})
    
    def reeschedule_exam(self, cdate, ndate, patient):
        for appointment in self.exams:
            if appointment["date"] == cdate and appointment["patient"] == patient:
                appointment["date"] = ndate
    
    def update_info(self):
        print(f"\nName: {self.name}")
        choice = input("Change employee's name? (Y/N) ")
        if choice == 'Y':
            self.name = input("Employee's name: ")
        
        print(f"\nCPF: {self.cpf}")
        choice = input("Change employee's CPF? (Y/N) ")
        if choice == 'Y':
            self.cpf = input("Patient's CPF: ")
        
        print(f"\nFunction: {self.function}")
        choice = input("Change employee's function? (Y/N) ")
        if choice == 'Y':
            self.function = input("Employee's function: ")

    def set_shifts(self):
        print(f"Current {self.name}'s shifts: ")
        self.print_shift()
        new_shift = input("\nType the new shift: ")
        self.shifts.append(new_shift)
    
    def cancel_shifts(self):
        print(f"Current {self.name}'s shifts: ")
        self.print_shift()
        shift = input("\nType the shift: ")
        if shift in self.shifts:
            self.shifts.remove(shift)
        else:
            print("\nShift not set.")

    def print_schedule(self):
        if self.exams:
            for item in self.exams:
                print(f"- {item['patient']}, {item['date']}")
        else:
            print("No exams scheduled")
    
    def print_shift(self):
        print("")
        if self.shifts:
            for shift in self.shifts:
                print(f"- {shift}")
        else:
            print("\nNo shifts set.")
    
    def print_info(self):
        os.system('clear')
        print("\n=== Employee Profile ===")

        print(f"Name: {self.name}")
        print(f"CPF: {self.cpf}")
        print(f"Function: {self.function}")
        
        print("\n--- Shifts ---\n")
        self.print_shift()
        print("\n--- Exams ---\n")
        self.print_schedule()

        print("==============================\n")
        

class Ward:
    def __init__(self, number, beds):
        self.number = number
        self.beds = beds
        self.occupation = 0
        self.patients = []
    
    def allocate_patient(self, patient):
        self.patients.append(patient)
        self.occupation += 1

    def remove_patient(self, patient):
        self.patients.remove(patient)
        self.occupation -= 1

    def print_ward_info(self):
        print(f"Number: {self.number}")
        print(f"Number of beds: {self.beds}")
        
        print("\nBed allocation:\n")
        for i in self.patients:
            print(f"- {i}")

class Items:
    def __init__(self, item):
        self.item = item
        self.stock = 0
    
    def add_stock(self, quantity):
        self.stock += quantity
    
    def remove_stock(self, quantity):
        self.stock -= quantity

    def print_info(self):
        print(f"{self.item} ({self.stock})")

class Hospital:
    def __init__(self):
        self.patients = []
        self.employees = []
        self.wards = []
        self.inventory = []
        self.invoicing = 0.0
        self.emergency_cases = []
    
    def find_patient(self, cpf):
        for p in self.patients:
            if cpf == p.cpf:
                return p
        return None
    
    def register_patient(self):
        name = input("\nPatient's name: ")
        cpf = input("Patient's CPF: ")

        existing_patient = self.find_patient(cpf)
        if existing_patient:
            print(f"\nPatient already registered.")
            return
        
        age = input("Patient's age: ")
        gender = input("Patient's gender: ")
        contact = input("Patient's contact: ")

        new_patient = Patient(name, cpf, age, gender, contact)
        self.patients.append(new_patient)

        print(f"\nPatient {name} registered successfully.")
    
    def update_info(self):
        cpf = input("\nType patient's CPF: ")
        patient = self.find_patient(cpf)
        if patient:
            patient.update_info()
            print(f"\n{patient.name}'s profile updated successfully")
        else:
            print("\nPatient not found.")
    
    def patient_list(self):
        os.system('clear')
        if self.patients:
            for p in self.patients:
                p.print_main()
        else:
            print("\nNo patients registered")

    def book_appointment(self):
        cpf = input("\nType patient's CPF: ")        
        existing_patient = self.find_patient(cpf)
        if existing_patient:
            doctor = input("Doctor: ")
            existing_doctor = self.find_doctor(doctor)
            if existing_doctor:
                date = input("Type the day of the exam: ")
                existing_patient.cancel_exam(date, doctor)
                existing_doctor.cancel_exam(date, existing_patient.name)
                print(f"Exam with Dr. {existing_doctor.name} successfully booked for {existing_patient.name}")
            else:
                print("\nDoctor not found.")
        else:
            print("\nPatient not found.")
    
    def cancel_appointment(self):
        cpf = input("\nType patient's CPF: ")        
        existing_patient = self.find_patient(cpf)
        if existing_patient:
            existing_patient.print_schedule()
            doctor = input("Type the name of the doctor: ")
            existing_doctor = self.find_doctor(doctor)
            if existing_doctor:
                date = input("Type the day of the exam: ")
                existing_patient.cancel_exam(date, doctor)
                existing_doctor.cancel_exam(date, existing_patient.name)
            else:
                print("\nDoctor not found.")
        else:
            print("\nPatient not found.")

    def reeschedule_appointment(self):
        cpf = input("\nType patient's CPF: ")        
        existing_patient = self.find_patient(cpf)
        if existing_patient:
            doctor = input("Type the name of the doctor: ")
            existing_doctor = self.find_doctor(doctor)
            if existing_doctor:
                cdate = input("Type the current day of the exam: ")
                ndate = input("Choose a new date")
                existing_patient.reeschedule_exam(cdate, ndate, doctor)
                existing_doctor.reeschedule_exam(cdate, ndate, existing_patient.name)
            else:
                print("\nDoctor not found.")
        else:
            print("\nPatient not found.")
    
    def update_medical_record(self):
        cpf = input("\nType patient's CPF: ")        
        existing_patient = self.find_patient(cpf)
        if existing_patient:
            existing_patient.print_medical_records()
            existing_patient.add_record()
        else:
            print("\nPatient not found.")
    
    def update_bills(self):
        cpf = input("\nType patient's CPF: ")        
        existing_patient = self.find_patient(cpf)
        if existing_patient:
            print(f"\n{existing_patient.name}'s current bills and invoicing:\n")
            existing_patient.print_bills()
            amount = input("\nType the value of the bill: ")
            self.invoicing += amount
            existing_patient.register_bill(amount)
            print("\nBill successfully registered.")
        else:
            print("\nPatient not found.")
    
    def update_prescriptions(self):
        cpf = input("\nType patient's CPF: ")        
        existing_patient = self.find_patient(cpf)
        if existing_patient:
            print(f"\n{existing_patient.name}'s current prescriptions:\n")
            existing_patient.print_prescriptions()
            existing_patient.add_prescription()
        else:
            print("\nPatient not found.")
    
    def order_lab_test(self):
        cpf = input("\nType patient's CPF: ")        
        existing_patient = self.find_patient(cpf)
        if existing_patient:
            print(f"\n{existing_patient.name}'s current lab tests:\n")
            existing_patient.print_lab_tests()
            test = input("\nType the name of the test: ")
            existing_patient.order_lab_test(test)
            print("Test ordered.")
        else:
            print("\nPatient not found.")
    
    def launch_result(self):
        cpf = input("\nType patient's CPF: ")        
        existing_patient = self.find_patient(cpf)
        if existing_patient:
            print(f"\n{existing_patient.name}'s current lab tests:\n")
            existing_patient.print_lab_tests()
            test = input("\nType the test you want to launch the result: ")
            existing_patient.results(test)
        else:
            print("\nPatient not found.")

    def find_ward(self, number):
        for p in self.wards:
            if number == number.p:
                return p
        return None
    
    def register_ward(self):
        number = input("\nWard number: ")
        existing_ward = self.find_ward(number)

        if existing_ward:
            print("\nWard already registered.")
            return

        beds = input("Number of beds in the ward: ")
        ward = Ward(number, beds)
        self.wards.append(ward)

    def allocate_ward(self):
        cpf = input("Type patient's CPF: ")        
        patient = self.find_patient(cpf)
        if patient:
            if patient.ward:
                print(f"\nPatient {patient.name} already allocated in ward {patient.ward}")
                return
            
            number = input("Ward number: ")
            ward = self.find_ward(number)
            if ward:
                if ward.occupation == ward.beds:
                    ward.allocate_patient(patient)
                    patient.ward = number
                else:
                    print("\nCrowded ward.")
            else:
                print("\nWard not found.")
        else:
            print("\nPatient not found.")
    
    def reallocate_ward(self):
        cpf = input("\nType patient's CPF: ")        
        patient = self.find_patient(cpf)
        if patient:
            if not patient.ward:
                print(f"\nPatient {patient.name} not allocated")
                return
            
            print(f"\n{patient.name}'s current ward: {patient.ward}")
            ward = self.find_ward(patient.ward)
            ward.remove_patient(patient)
            
            number = input("New ward number: ")
            new_ward = self.find_ward(number)
            if new_ward:
                if new_ward.occupation == ward.beds:
                    new_ward.allocate_patient(patient)
                    patient.ward = number
                else:
                    print("\nCrowded ward.")
            else:
                print("\nWard not found.")
        else:
            print("\nPatient not found.")
    
    def deallocate_ward(self):
        cpf = input("\nType patient's CPF: ")        
        patient = self.find_patient(cpf)
        if patient:
            if not patient.ward:
                print(f"\nPatient {patient.name} not allocated")
                return
            
            print(f"{patient.name}'s current ward: {patient.ward}")
            ward = self.find_ward(patient.ward)
            ward.remove_patient(patient)
        else:
            print("\nPatient not found.")
    
    def find_item(self, item):
        for x in self.inventory:
            if x.item == item:
                return x
        return None
    
    def add_inventory(self):
        item = input("\nType the item to be added to inventory: ")
        existing_item = self.find_item(item)

        if existing_item:
            print(f"\nCurrent stock of {item}: {existing_item.stock}")
            choice = input("\nDo you wish to add more to the stock? (Y/N): ")

            if choice.upper() == 'Y':
                quantity = input("How much? ")
                existing_item.add_stock(quantity)
        else:
            print("\nItem not registered yet")
            quantity = input("\nHow much would you like to add? ")
            new_item = Items(item)
            new_item.add_stock(quantity)
            self.inventory.append(new_item)
    
    def remove_inventory(self):
        item = input("\nType the item to be removed to inventory: ")
        existing_item = self.find_item(item)

        if existing_item:
            print(f"\nCurrent stock of {item}: {existing_item.stock}")
            quantity = input("\nHow much would you wish to remove? ")
            if quantity >= existing_item.stock:
                self.inventory.remove(existing_item)
            else:
                existing_item.remove_stock(quantity)
        else: 
            print("\nItem not found")

    def print_inventory(self):
        if self.inventory:
            for x in self.inventory:
                x.print_info()
        else:
            print("Empty inventory.")

    def find_employee(self, cpf):
        for e in self.employees:
            if cpf == e.cpf:
                return e
        return None
    
    def register_employee(self):
        name = input("\nEmployee's name: ")
        cpf = input("Emplyee's CPF: ")

        existing_employee = self.find_employee(cpf)
        if existing_employee:
            print(f"\nEmployee already registered.")
            return
        
        function = input("Employee's function: ")

        new_employee = Employee(name, cpf, function)
        self.employees.append(new_employee)

        print(f"\nEmployee {name} registered.")
        return new_employee
    
    def update_info_staff(self):
        cpf = input("\nType employee's CPF: ")
        employee = self.find_employee(cpf)
        if employee:
            employee.update_info()
        else:
            print("\nEmployee not found.")
    
    def set_shift(self):
        cpf = input("\nType employee's CPF: ")
        employee = self.find_employee(cpf)
        if employee:
            employee.set_shifts()
        else:
            print("\nEmployee not found.")
    
    def cancel_shift(self):
        cpf = input("\nType employee's CPF: ")
        employee = self.find_employee(cpf)
        if employee:
            employee.cancel_shifts()
        else:
            print("\nEmployee not found.")
    
    def add_emergency_case(self):
        name = input("\nType the patient's name: ")
        condition = input("Type the patient's condition: ")
        priority = input("Type the level of priority: ")
        self.emergency_cases.append({"name": name, "condition": condition, "priority": priority})
        print("\nEmergency registered.")
    
    def remove_emergency_case(self):
        name = input("\nEnter the patient's name to remove from emergency cases: ")
        for case in self.emergency_cases:
            if case["name"] == name:
                self.emergency_cases.remove(case)
                print(f"Emergency case for {name} has been removed.")
                return
        print(f"No emergency case found for {name}.")

def patient_area(hospital):
    while True:
        os.system('clear')
        print("PATIENT AREA\n")

        print("1. Register new patient")
        print("2. Check patient profile")
        print("3. Update patient's profile")
        print("4. Check patient list")
        print("0. Return to main menu\n")
        choice = input("Choose an option: ")

        if choice == '1':
            hospital.register_patient()
        elif choice == '2':
            cpf = input("\nType patient's CPF: ")
            patient = hospital.find_patient(cpf)
            if patient:
                patient.print_info()
            else:
                print("\nPatient not found")
        elif choice == '3':
            hospital.update_info()
        elif choice == '4':
            hospital.patient_list()
        elif choice == '0':
            break
        else:
            print("\nInvalid option!")
        
        input("\nPress ENTER to return to patient area")

def schedule_appointment(hospital):
    while True:
        os.system('clear')
        print("APPOINTMENT SCHEDULING AREA\n")

        print("1. Book an appointment")
        print("2. Check patient's appointments")
        print("3. Cancel patient's appointment")
        print("4. Reeschedule patient's appointment")
        print("0. Return to main menu\n")
        choice = input("Choose an option: ")

        if choice == '1':
            hospital.book_appointment()
        elif choice == '2':
            cpf = input("\nType patient's CPF: ")
            patient = hospital.find_patient(cpf)
            if patient:
                patient.print_schedule()
            else:
                print("\nPatient not found")
        elif choice == '3':
            hospital.cancel_appointment()
        elif choice == '4':
            hospital.reeschedule_appointment()
        elif choice == '0':
            break
        else:
            print("\nInvalid option!")
        
        input("\nPress ENTER to return to appoitment scheduling area")

def manage_medical_records(hospital):
    while True:
        os.system('clear')
        print("MEDICAL RECORDS AREA\n")

        print("1. Update patient's medical record")
        print("2. Access patient's medical record")
        print("0. Return to main menu\n")
        choice = input("Choose an option: ")

        if choice == '1':
            hospital.update_medical_record()
        elif choice == '2':
            cpf = input("\nType patient's CPF: ")
            patient = hospital.find_patient(cpf)
            if patient:
                patient.print_medical_records()
            else:
                print("\nPatient not found")
        elif choice == '0':
            break
        else:
            print("\nInvalid option!")
        
        input("\nPress ENTER to return to medical records area")

def billing(hospital):
    while True:
        os.system('clear')
        print("BILLING AND INVOICING AREA\n")

        print("1. Update patient's bills")
        print("2. Access patient's bills")
        print("3. Access hospital invoicing")
        print("0. Return to main menu\n")
        choice = input("Choose an option: ")

        if choice == '1':
            hospital.update_bills()
        elif choice == '2':
            cpf = input("\nType patient's CPF: ")
            patient = hospital.find_patient(cpf)
            if patient:
                patient.print_bills()
            else:
                print("\nPatient not found")
        elif choice == '3':
            hospital.print_invoicing()
        elif choice == '0':
            break
        else:
            print("\nInvalid option!")
        
        input("\nPress ENTER to return to billing and invoicing area")

def manage_prescriptions(hospital):
    while True:
        os.system('clear')
        print("PRESCRIPTIONS AREA\n")

        print("1. Update patient's prescriptions")
        print("2. Access patient's prescriptions")
        print("0. Return to main menu\n")
        choice = input("Choose an option: ")

        if choice == '1':
            hospital.update_prescriptions()
        elif choice == '2':
            cpf = input("\nType patient's CPF: ")
            patient = hospital.find_patient(cpf)
            if patient:
                patient.print_prescriptions()
            else:
                print("\nPatient not found")
        elif choice == '0':
            break
        else:
            print("\nInvalid option!")
        
        input("\nPress ENTER to return to pescriptions area")

def lab_test(hospital):
    while True:
        os.system('clear')
        print("LAB TESTS AREA\n")

        print("1. Order lab test")
        print("2. Launch lab test result")
        print("3. Check patient's lab tests")
        print("0. Return to main menu\n")
        choice = input("Choose an option: ")

        if choice == '1':
            hospital.order_lab_test()
        if choice == '2':
            hospital.launch_result()
        elif choice == '3':
            cpf = input("\nType patient's CPF: ")
            patient = hospital.find_patient(cpf)
            if patient:
                patient.print_lab_tests()
            else:
                print("\nPatient not found")
        elif choice == '0':
            break
        else:
            print("\nInvalid option!")
        
        input("\nPress ENTER to return to lab tests area")

def manage_wards(hospital):
    while True:
        os.system('clear')
        print("WARD MANAGEMENT AREA\n")

        print("1. Register ward")
        print("2. Check wards")
        print("3. Allocate patient")
        print("4. Reallocate patient")
        print("5. Deallocate patient")
        print("0. Return to main menu\n")
        choice = input("Choose an option: ")

        if choice == '1':
            hospital.register_ward()
        elif choice == '2':
            cpf = input("\nType patient's CPF: ")
            patient = hospital.find_ward(cpf)
            if patient:
                patient.print_ward_info()
            else:
                print("\nPatient not found")
        elif choice == '3':
            hospital.allocate_ward()
        elif choice == '4':
            hospital.reallocate_ward()
        elif choice == '0':
            break
        else:
            print("\nInvalid option!")
        
        input("\nPress ENTER to return to ward management area")

def manage_inventory(hospital):
    while True:
        os.system('clear')
        print("INVENTORY MANAGEMENT AREA\n")

        print("1. Check inventory")
        print("2. Add item to inventory")
        print("3. Remove item from inventory")
        print("0. Return to main menu\n")
        choice = input("Choose an option: ")

        if choice == '1':
            hospital.print_inventory()
        elif choice == '2':
            hospital.add_inventory()
        elif choice == '3':
            hospital.remove_inventory()
        elif choice == '0':
            break
        else:
            print("\nInvalid option!")
        
        input("\nPress ENTER to return to inventory management area")

def staff_area(hospital):
    while True:
        os.system('clear')
        print("STAFF AREA\n")

        print("1. Register new employee")
        print("2. Check employee's profile")
        print("3. Update employee's profile")
        print("4. Check employee shift")
        print("5. Set employee shift")
        print("6. Cancel employee shift")
        print("0. Return to main menu\n")
        choice = input("Choose an option: ")

        if choice == '1':
            hospital.register_employee()
        elif choice == '2':
            cpf = input("\nType employee's CPF: ")
            employee = hospital.find_employee(cpf)
            if employee:
                employee.print_info()
            else:
                print("\nEmployee not found")
        elif choice == '3':
            hospital.update_info_staff()
        elif choice == '4':
            cpf = input("\nType employee's CPF: ")
            employee = hospital.find_employee(cpf)
            if employee:
                employee.print_shift()
            else:
                print("\nEmployee not found")
        elif choice == '5':
            hospital.set_shift()
        elif choice == '6':
            hospital.cancel_shift()
        elif choice == '0':
            break
        else:
            print("\nInvalid option!")
        
        input("\nPress ENTER to return to staff area")

def emergency_cases(hospital):
    while True:
        os.system('clear')
        print("EMERGENCY CASES AREA\n")

        print("1. Add emergency case")
        print("2. Remove emergency case")
        print("0. Return to main menu\n")
        choice = input("Choose an option: ")

        if choice == '1':
            hospital.add_emergency_case()
        elif choice == '2':
            hospital.remove_emergency_case()
        elif choice == '0':
            break
        else:
            print("\nInvalid option!")
        
        input("\nPress ENTER to return to emergency cases area")

def main():
    hospital = Hospital()
    
    while True:
        os.system('clear')
        
        print("HOSPITAL SYSTEM\n")
        print("1. Patient profiles")
        print("2. Schedule appointment")
        print("3. Manage medical records")
        print("4. Billing and invoicing")
        print("5. Manage prescriptions")
        print("6. Order and manage lab tests")
        print("7. Ward management")
        print("8. Inventory management")
        print("9. Staff management")
        print("10. Emergency cases")
        print("0. Exit\n")
        choice = input("Choose an option: ")
        
        if choice == "1":
            patient_area(hospital)
        elif choice == "2":
            schedule_appointment(hospital)
        elif choice == "3":
            manage_medical_records(hospital)
        elif choice == "4":
            billing(hospital)
        elif choice == "5":
            manage_prescriptions(hospital)
        elif choice == "6":
            lab_test(hospital)
        elif choice == "7":
            manage_wards(hospital)
        elif choice == "8":
            manage_inventory(hospital)
        elif choice == "9":
            staff_area(hospital)
        elif choice == "10":
            emergency_cases(hospital)
        elif choice == "0":
            break
        else:
            print("\nInvalid option!")
            input("\npress ENTER to return to main menu.")

if __name__ == "__main__":
    main()