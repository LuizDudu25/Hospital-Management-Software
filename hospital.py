import bisect
from patients import Patient

class StaffFactory:
    @staticmethod
    def create_staff(cargo, name, cpf, age, gender, contact, salary, shift):
        from staff import Doctor, Nurse, Other

        if cargo == "Médico":
            especializacao = input("Espcialização do médico: ")
            return Doctor(name, cpf, age, gender, contact, especializacao, salary, shift)
        elif cargo == "Enfermeiro":
            especialidade = input("Especialidade do enfermeiro: ")
            return Nurse(name, cpf, age, gender, contact, salary, shift, especialidade)
        else:
            cargo = input("Cargo do funcionário: ")
            return Other(name, cpf, age, gender, contact, cargo, salary, shift)

class Hospital:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Hospital, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance
    
    def __init__(self):
        if self.__initialized:
            return
        self.patients = []
        self.employees = []
        self.doctors = []
        self.nurses = []
        self.wards = []
        self.inventory = []
        self.invoicing = 0.0
        self.emergency_cases = []
        self.__initialized = True
    
    def find_person(self, cpf, group):
        for person in group:
            if person.cpf == cpf:
                return person
        return None
    
    def register_patient(self):
        name = input("\nNome do paciente: ")
        cpf = input("CPF do paciente: ")

        existing_patient = self.find_person(cpf, self.patients)
        if existing_patient:
            print(f"\nCPF já registrado.")
            return
        
        age = input("Idade do paciente: ")
        gender = input("Gênero do paciente: ")
        contact = input("Contato do paciente: ")

        new_patient = Patient(name, cpf, age, gender, contact)
        self.patients.append(new_patient)

        print(f"\nPaciente {name} registrado com sucesso.")
    
    def find_ward(self):
        number = input("\nNúmero do quarto: ")
        if not number.isdigit():
            print("\nNúmero inválido.")
            self.find_ward()
        ward = next((ward for ward in self.wards if ward.number == number), None)
        if not ward:
            print("\nQuarto não encontrado.")
            return None
        return ward

    def find_item(self):
        number = input("\nNúmero do item: ")
        if not number.isdigit():
            print("\nNúmero inválido.")
            self.find_item()
        item = next((item for item in self.inventory if item.number == number), None)
        if not item:
            print("\nItem não encontrado no inventário.")
            return None
        return item
    
    def register_employee(self, cargo, group):
        name = input("\nNome do funcionário: ")
        cpf = input("CPF do funcionário: ")
        if self.find_person(cpf, group):
            print("\nCPF já registrado.")
            return
        age = input("Idade do funcionário: ")
        gender = input("Gênero do funcionário: ")
        contact = input("Contato do funcionário: ")
        salary = input("Salário do funcionário: ")
        shift = input("Turno do funcionário: ")
        
        funcionario = StaffFactory.create_staff(cargo, name, cpf, age, gender, contact, salary, shift)

        self.employees.append(funcionario)

        if cargo == "Médico":
            self.doctors.append(funcionario)
        elif cargo == "Enfermeiro":
            self.nurses.append(funcionario)
        
        print(f"\nFuncionário {funcionario.nome} registrado com sucesso.")
        
    
    def add_emergency_case(self, patient):
        from menus import Menu
        from emergency import Emergency_case
        specialty = Menu.menu_specialties()
        priority = int(input("Nível de prioridade: "))
        healthcare_plan = Menu.menu_plan()

        new_case = Emergency_case(patient, specialty, priority, healthcare_plan)
        bisect.insort(self.emergency_cases, new_case)
    
    def call_next_patient(self, specialty):
        for i, case in enumerate(self.emergency_cases):
            if case.specialty == specialty:
                called_patient = self.emergency_cases.pop(i)
                print(f"Chamando {called_patient.patient} para atendimento de {specialty}!")
                return called_patient

        print(f"Nenhum paciente aguardando atendimento de {specialty} no momento.")
        return None
