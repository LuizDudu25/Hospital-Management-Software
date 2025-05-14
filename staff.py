from models import Employee, InfoPrinter
from menus import Menu

class ExamScheduleDecorator(InfoPrinter):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def print_info(self):
        self.wrapped.print_info()
        print("\n--- CONSULTAS AGENDADAS ---")
        self.wrapped.employee.print_schedule()

class Doctor(Employee):
    available_shifts = ["Diurno", "Noturno", "Plantão 24h"]
    
    def __init__(self, nome, cpf, idade, genero, contato, especializacao, salario, turno):
        super().__init__(nome, cpf, idade, genero, contato, "Médico", salario, turno)
        self.especializacao = especializacao
        self.appointments = []
    
    def update_info(self):
        super().update_info()
        self.especializacao = input(f"Especialização [{self.especialização}]: ") or self.especializacao
    
    def print_info(self):
        super().print_info()
        print(f"Especialiação: {self.especializacao}")
    
    def is_available(self, date, time):
        for appointment in self.appointments:
            if appointment.date == date and appointment.time == time:
                return False
        return True
    
    def change_shift(self):
        print("\nTurnos disponíveis para médicos:")
        for i, shift in enumerate(Doctor.available_shifts, 1):
            print(f"{i}. {shift}")
        try:
            choice = int(input("Escolha o novo turno: "))
            if 1 <= choice <= len(Doctor.available_shifts):
                self.turno = Doctor.available_shifts[choice - 1]
                print(f"\nTurno alterado para {self.turno}.")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida.")
    
    @classmethod
    def add_shift(cls):
        novo_turno = input("Digite o novo turno para médicos: ").strip()
        if novo_turno and novo_turno not in cls.available_shifts:
            cls.available_shifts.append(novo_turno)
            print(f"Turno '{novo_turno}' adicionado.")
        else:
            print("Turno já existe ou entrada inválida.")
    
    def book_appointment(self, patient):
        from appointments import Appointment
        date = input("\nDigite a data da consulta: ")
        time = input("Digite o horário da consulta: ")
        if not self.is_available(date, time):
            print("\nErro: O médico já tem uma consulta nesse horário!")
            return
        
        healthcare_plan = Menu.menu_plan()
        appointment = Appointment(patient, self, date, time, healthcare_plan)
        self.appointments.append(appointment)
        patient.add_appointment(appointment)

        print("\nConsulta agendada com sucesso.")
    
    def cancel_appointment(self, hospital):
        cpf_patient = input("\nDigite o CPF do paciente: ")
        patient = hospital.find_person(cpf_patient, hospital.patients)
        if not patient:
            print("\nPaciente não encontrado.")
            input("Pressione ENTER para voltar ao menu.")
            return
        
        date = input("\nDigite a data da consulta: ")
        time = input("Digite o horário da consulta: ")
        
        for appointment in self.appointments:
            if appointment.patient == patient and appointment.date == date and appointment.time == time:
                self.appointments.remove(appointment)
                patient.appointments.remove(appointment)
                print("\nConsulta cancelada com sucesso.")
                return patient
        print("\nConsulta não encontrada.")

class Nurse(Employee):
    available_shifts = ["Diurno", "Noturno"]
    
    def __init__(self, nome, cpf, idade, genero, contato, salario, turno, especialidade):
        super().__init__(nome, cpf, idade, genero, contato, "Enfermeiro", salario, turno)
        self.especialidade = especialidade
        self.plantões = []

    def update_info(self):
        super().update_info()
        self.especialidade = input(f"Especialidade [{self.especialidade}]: ") or self.especialidade

    def print_info(self):
        super().print_info()
        print(f"Especialidade: {self.especialidade}")
    
    def change_shift(self):
        print("\nTurnos disponíveis para enfermeiros:")
        for i, shift in enumerate(Nurse.available_shifts, 1):
            print(f"{i}. {shift}")
        try:
            choice = int(input("Escolha o novo turno: "))
            if 1 <= choice <= len(Nurse.available_shifts):
                self.turno = Nurse.available_shifts[choice - 1]
                print(f"\nTurno alterado para {self.turno}.")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida.")

    @classmethod
    def add_shift(cls):
        novo_turno = input("Digite o novo turno para enfermeiros: ").strip()
        if novo_turno and novo_turno not in cls.available_shifts:
            cls.available_shifts.append(novo_turno)
            print(f"Turno '{novo_turno}' adicionado.")
        else:
            print("Turno já existe ou entrada inválida.")

class Other(Employee):
    available_shifts = ["Diurno", "Noturno", "Integral"]

    def __init__(self, nome, cpf, idade, genero, contato, cargo, salario, turno):
        super().__init__(nome, cpf, idade, genero, contato, cargo, salario, turno)

    def change_shift(self):
        print("\nTurnos disponíveis para outros funcionários:")
        for i, shift in enumerate(Other.available_shifts, 1):
            print(f"{i}. {shift}")
        try:
            choice = int(input("Escolha o novo turno: "))
            if 1 <= choice <= len(Other.available_shifts):
                self.turno = Other.available_shifts[choice - 1]
                print(f"\nTurno alterado para {self.turno}.")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida.")

    @classmethod
    def add_shift(cls):
        novo_turno = input("Digite o novo turno para outros funcionários: ").strip()
        if novo_turno and novo_turno not in cls.available_shifts:
            cls.available_shifts.append(novo_turno)
            print(f"Turno '{novo_turno}' adicionado.")
        else:
            print("Turno já existe ou entrada inválida.")

def staff_area(hospital):
    choice1 = Menu.menu_staff()
    choice2 = Menu.menu_group()

    if choice1 != '0':
        if choice2 == 'Médico':
            group = hospital.doctors
        elif choice2 == 'Enfermeiro':
            group = hospital.nurses
        else:
            choice2 = input("\nDigite o cargo do funcionário: ")
            group = hospital.employees
    
    if choice1 == '1':
        if group:
            for employee in group:
                employee.print_info()
        else:
            print("\nNenhum funcionário registrado.")
    elif choice1 == '2':        
        hospital.register_employee(choice2, group)
    elif choice1 == '3':
        cpf = input("\nDigite o CPF do funcionário: ")
        employee = hospital.find_person(cpf, group)

        if employee:
            from models import BasicEmployeeInfoPrinter, ShiftDecorator, ExamScheduleDecorator

            printer = BasicEmployeeInfoPrinter(employee)
            printer.print_info()

            choice = input("\nDeseja alterar as informações do funcionário? (S/N) ")
            if choice == 'S':
                employee.update_info()
    elif choice1 == '4':
        cpf = input("\nDigite o CPF do funcionário: ")
        employee = hospital.find_person(cpf, group)
        if employee:
            group.remove(employee)
            print("\nFuncionário removido.")
    elif choice1 == '0':
        return
    else:
        print("\nOpção inválida.")
    
    input("\nPressione ENTER para continuar ")
