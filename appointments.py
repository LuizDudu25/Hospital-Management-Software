from menus import Menu

class Appointment:
    def __init__(self, patient, doctor, date, time, healthcare_plan):
        self.date = date
        self.time = time
        self.patient = patient
        self.doctor = doctor
        self.healthcare_plan = healthcare_plan

    def __str__(self):
        from patients import Patient
        return f'{self.date} | {self.time} | {self.patient.nome} | {self.healthcare_plan}'

class Lab_test:
    def __init__(self, patient, date, test):
        self.patient = patient
        self.date = date
        self.test = test
        self.result = None

    def __str__(self):
        return f'{self.patient} | {self.date} | {self.test}'

def appointments_area(hospital):
    while True:
        choice = Menu.menu_appointments()

        if choice == '1':
            cpf_patient = input("\nDigite o CPF do paciente: ")
            patient = hospital.find_person(cpf_patient, hospital.patients)
            if not patient:
                print("\nPaciente não encontrado.")
                input("Pressione ENTER para voltar ao menu.")
                continue
                
            cpf_doctor = input("\nDigite o CPF do médico: ")
            doctor = hospital.find_person(cpf_doctor, hospital.doctors)
            if not doctor:
                print("\nMédico não encontrado.")
                input("Pressione ENTER para voltar ao menu.")
                continue

            doctor.book_appointment(patient)
        elif choice == 2:
            cpf_doctor = input("\nDigite o CPF do médico: ")
            doctor = hospital.find_person(cpf_doctor, hospital.doctors)
            if not doctor:
                print("\nMédico não encontrado.")
                input("Pressione ENTER para voltar ao menu.")
                continue

            patient = doctor.cancel_appointment(hospital)
        elif choice == 3:
            cpf_doctor = input("\nDigite o CPF do médico: ")
            doctor = hospital.find_person(cpf_doctor, hospital.doctors)
            if not doctor:
                print("\nMédico não encontrado.")
                input("Pressione ENTER para voltar ao menu.")
                continue

            patient = doctor.cancel_appointment(hospital)
            doctor.book_appointment(patient)
        elif choice == 4:
            cpf_patient = input("\nDigite o CPF do paciente: ")
            patient = hospital.find_person(cpf_patient, hospital.patients)
            if patient:
                print("\nTestes solicitados para", patient.name)
                for i, test in enumerate(patient.testes):       
                    print(f"{i+1}. {test}")
            else:
                print("\nPaciente não encontrado.")
            
            test = input("\nDigite o teste a ser solicitado: ")
            date = input("Digite a data do teste: ")
            patient.request_test(test, date)
        elif choice == '0':
            break
        else:
            print("\nOpção inválida!")
        
        input("\nPressione ENTER para continuar ")