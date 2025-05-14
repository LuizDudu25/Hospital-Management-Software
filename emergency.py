from menus import Menu

class Emergency_case:
    def __init__(self, patient, specialty, priority, healthcare_plan):
        self.patient = patient
        self.specialty = specialty
        self.priority = priority
        self.healtcare_plan = healthcare_plan
    
    def __str__(self):
        return f'{self.patient.nome} | {self.specialty} | {self.priority} | {self.healtcare_plan}'

def emergency(hospital):
    while True:
        choice = Menu.menu_emergency()

        if choice == '1':
            if hospital.emergency_cases:
                print("\nCasos de emergência:")
                for case in hospital.emergency_cases:
                    print(case)
            else:
                print("\nNenhum caso de emergência registrado.")
        elif choice == '2':
            cpf = input("\nDigite o CPF do paciente: ")
            patient = hospital.find_person(cpf, hospital.patients)
            if not patient:
                from patients import Patient
                name = input("Nome do paciente: ")
                age = input("Idade do paciente: ")
                gender = input("Gênero do paciente: ")
                contact = input("Contato do paciente: ")
                patient = Patient(name, cpf, age, gender, contact)
                hospital.patients.append(patient)
            hospital.add_emergecy_case(patient)
        elif choice == '3':
            specialty = Menu.menu_specialties()
            patient = hospital.call_next_patient(specialty)
        elif choice == '0':
            break
        else:
            print("\nOpção inválida!")
        
        input("\nPressione ENTER para continuar ")
