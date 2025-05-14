from abc import ABC, abstractmethod
from models import Person, InfoPrinter, Subject, DoctorNotifier
from menus import Menu

class BasicPatientInfoPrinter(InfoPrinter):
    def __init__(self, patient):
        self.patient = patient

    def print_info(self):
        print("=== INFORMAÇÕES BÁSICAS ===")
        self.patient.print_info()

class MedicalRecordDecorator(InfoPrinter):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def print_info(self):
        self.wrapped.print_info()
        print("\n--- PRONTUÁRIO MÉDICO ---")
        self.wrapped.patient.print_medical_records()

class AppointmentsDecorator(InfoPrinter):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def print_info(self):
        self.wrapped.print_info()
        print("\n--- CONSULTAS AGENDADAS ---")
        self.wrapped.patient.print_schedule()

class PrescriptionsDecorator(InfoPrinter):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def print_info(self):
        self.wrapped.print_info()
        print("\n--- PRESCRIÇÕES ---")
        self.wrapped.patient.print_prescriptions()

class LabTestsDecorator(InfoPrinter):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def print_info(self):
        self.wrapped.print_info()
        print("\n--- TESTES LABORATORIAIS ---")
        self.wrapped.patient.print_lab_tests()

class Medical_record:
    def __init__(self, medico, data, hora, diagnostico):
        self.medico = medico
        self.data = data
        self.hora = hora
        self.diagnostico = diagnostico
    
    def __str__(self):
        return f'{self.medico} | {self.data} | {self.hora} | {self.diagnostico}'

class Prescription:
    def __init__(self, medico, data, hora, prescricao):
        self.medico = medico
        self.data = data
        self.hora = hora
        self.prescricao = prescricao
    
    def __str__(self):
        return f'{self.medico}\n{self.data} | {self.hora}\n{self.prescricao}\n'

class Lab_test:
    def __init__(self, tipo, data, hora):
        self.tipo = tipo
        self.data = data
        self.hora = hora
        self.resultado = None
    
    def __str__(self):
        return f'{self.tipo} | {self.data} | {self.hora}'

class Patient(Person, Subject):
    def __init__(self, nome, cpf, idade, genero, contato):
        Person().__init__(self, nome, cpf, idade, genero, contato)
        Subject().__init__(self)
        self.__appointments = []
        self.__medical_record = []
        self.__bills = []
        self.__prescricoes = []
        self.__testes = []
        self.ward = None 
        self.attach(DoctorNotifier())

    @property
    def appointments(self):
        return self.__appointments.copy()

    @property
    def medical_record(self):
        return self.__medical_record.copy()

    @property
    def bills(self):
        return self.__bills.copy()

    @property
    def prescricoes(self):
        return self.__prescricoes.copy()

    @property
    def testes(self):
        return self.__testes.copy()

    def add_appointment(self, appointment):
        self.__appointments.append(appointment)
        self.notify("Nova consulta agendada")

    def add_record(self, medico, data, hora, diagnostico):
        registro = Medical_record(medico, data, hora, diagnostico)
        self.__medical_record.append(registro)
        self.notify("Novo prontuário registrado")

    def add_bill(self, bill):
        self.__bills.append(bill)
        self.notify("Nova conta registrada")

    def add_prescription(self, medico, data, hora, prescricao):
        prescription = Prescription(medico, data, hora, prescricao)
        self.__prescricoes.append(prescription)
        self.notify("Nova prescrição adicionada")

    def add_test(self, test):
        self.__testes.append(test)
        self.notify("Novo teste laboratorial agendado")

    def update_info(self):
        print(f"\nAtualizando informações do paciente {self.nome}:")
        self.nome = input(f"Nome [{self.nome}]: ") or self.nome
        self.cpf = input(f"CPF [{self.cpf}]: ") or self.cpf
        self.idade = input(f"Idade [{self.idade}]: ") or self.idade
        self.genero = input(f"Gênero [{self.genero}]: ") or self.genero
        self.contato = input(f"Contato [{self.contato}]: ") or self.contato
    
    def print_info(self):
        print("\nInformações do Paciente:\n")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade}")
        print(f"Gênero: {self.genero}")
        print(f"Contato: {self.contato}")
        if self.ward:
            print(f"Quarto: {self.ward.number}")
        else:
            print("Quarto: Não alocado")
    
    def print_medical_records(self):
        if self.medical_records:
            for record in self.medical_records:
                print(f"- {record}")
        else:
            print("Nenhum prontuário registrado.")

    def print_schedule(self):
        if self.appointments:
            for a in self.appointments:
                print(f"- {a.date} às {a.time}")
        else:
            print("Nenhuma consulta agendada.")

    def print_prescriptions(self):
        if self.prescriptions:
            print(f"\nPrescrições de {self.nome}:")
            for i, prescription in enumerate(self.__prescricoes):
                print(f"{i+1}\n{prescription}\n")
        else:
            print("Nenhuma prescrição registrada.")
    
    def print_lab_tests(self):
        for i, test in enumerate(self.testes):
            print(f"{i+1}. {test}")
            if test.result:
                print(f"   Resultado: {test.result}")
            else:
                print("   Resultado: Teste não realizado\n")
    
    def update_prescription(self):
        choice = int(input("\nDigite o número da prescrição que deseja alterar: "))
        if choice > len(self.__prescricoes) or choice < 1:
            print("\nPrescrição não encontrada.")
            return
        
        medico = input("\nMédico: ")
        data = input("Data: ")
        hora = input("Hora: ")
        prescricao = input("Prescrição: ")

        prescription = Prescription(medico, data, hora, prescricao)
        self.__prescricoes[choice-1] = prescription
    
    def request_test(self, test, date):
        from appointments import Lab_test
        test = Lab_test(self, date, test)
        self.__testes.append(test)
    
    def reallocate(self, hospital, ward):
        ward.remove_patient(self)
        while True:
            new_ward = int(input("\nDigite o número do novo quarto: "))
            ward = next((ward for ward in hospital.wards if ward.number == new_ward), None)
            if not ward:
                print("\nQuarto não encontrado.")
                continue
            if ward.add_patient(self):
                self.ward = ward
                break

def profile(patient):
    while True:
        printer = BasicPatientInfoPrinter(patient)
        choice = Menu.menu_patient_profile(patient, printer)

        if choice == '1':
            printer.print_info()
            patient.update_info()
        if choice == '2':
            printer = MedicalRecordDecorator(printer)
            printer.print_info()
            
            choice = input("\nDeseja adicionar um novo registro? (S/N) ")
            if choice == 'S':
                patient.add_record()
        if choice == '3':
            printer = PrescriptionsDecorator(printer)
            printer.print_info()
            
            choice = input("\nDeseja alterar uma prescrição? (S/N) ")
            if choice == 'S':
                patient.update_prescription()
            
            choice = input("\nDeseja adicionar uma nova prescrição? (S/N) ")
            if choice == 'S':
                patient.add_prescription()
        elif choice == '4':
            printer = LabTestsDecorator(printer)
            printer.print_info()
            
            if patient.testes:
                choice = input("\nDeseja adicionar um resultado? (S/N) ")
                if choice == 'S':
                    test = int(input("Digite o número do teste: "))
                    result = input("Digite o resultado: ")
                    patient.testes[test-1].result = result
            
            choice = input("\nDeseja solicitar um novo teste laboratorial? (S/N) ")
            if choice == 'S':
                tipo = input("Digite o tipo de teste a ser realizado: ")
                data = input("Digite a data para realizar o teste: ")
                hora = input("Digite a hora para realizar o teste: ")

                teste = Lab_test(tipo, data, hora)
                patient.add_test(teste)
        elif choice == '0':
            break
        else:
            print("\nOpção inválida!")
        
        input("\nPressione ENTER para continuar ")

def patient_area(hospital):
    while True:
        choice = Menu.menu_patients()

        if choice == '1':
            if hospital.patients:
                for patient in hospital.patients:
                    patient.print_info()
            else:
                print("\nNenhum paciente registrado")
        elif choice == '2':
            hospital.register_patient()
        elif choice == '3':
            cpf = input("\nDigite o CPF do paciente: ")
            patient = hospital.find_person(cpf, hospital.patients)
            if patient:
                profile(patient)
            else:
                print("\nPaciente não encontrado.")
        elif choice == '0':
            break
        else:
            print("\nOpção inválida!")
        
        input("\nPressione ENTER para continuar ")