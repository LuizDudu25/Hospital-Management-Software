from abc import ABC, abstractmethod

class InfoPrinter(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, subject, event):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, event):
        for observer in self._observers:
            observer.update(self, event)

class DoctorNotifier(Observer):
    def update(self, subject, event):
        print(f"[Notificação] Paciente {subject.nome}: {event}")

class Person(ABC):
    def __init__(self, nome: str, cpf: str, idade: int, genero: str, contato: str):
        self._nome = nome
        self.__cpf = cpf
        self._idade = idade
        self._genero = genero
        self._contato = contato

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not novo_nome.strip():
            raise ValueError("Nome não pode ser vazio!")
        self._nome = novo_nome.strip()

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf: str):
        if not self.__validar_cpf(novo_cpf):
            raise ValueError("CPF inválido! Verifique o número digitado.")
        self.__cpf = ''.join(filter(str.isdigit, novo_cpf))
    
    def __validar_cpf(self, cpf: str) -> bool:
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11 or len(set(cpf)) == 1:
            return False
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = (soma * 10) % 11
        digito1 = resto if resto < 10 else 0
        if digito1 != int(cpf[9]):
            return False
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = (soma * 10) % 11
        digito2 = resto if resto < 10 else 0
        if digito2 != int(cpf[10]):
            return False
        return True

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, nova_idade: int):
        if not isinstance(nova_idade, int) or nova_idade < 0:
            raise ValueError("Idade deve ser um inteiro positivo!")
        self._idade = nova_idade

    @property
    def genero(self) -> str:
        return self._genero

    @genero.setter
    def genero(self, novo_genero: str):
        if novo_genero not in ["M", "F", "Outro"]:
            raise ValueError("Gênero deve ser 'M', 'F' ou 'Outro'!")
        self._genero = novo_genero

    @property
    def contato(self) -> str:
        return self._contato

    @contato.setter
    def contato(self, novo_contato: str):
        if "@" not in novo_contato and not novo_contato.isdigit():
            raise ValueError("Contato deve ser um email ou telefone!")
        self._contato = novo_contato
    
    @abstractmethod
    def update_info(self):
        pass

    @abstractmethod
    def print_info(self):
        pass

class BasicEmployeeInfoPrinter(InfoPrinter):
    def __init__(self, employee):
        self.employee = employee

    def print_info(self):
        print("=== INFORMAÇÕES DO FUNCIONÁRIO ===")
        self.employee.print_info()


class ShiftDecorator(InfoPrinter):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def print_info(self):
        self.wrapped.print_info()
        print("\n--- TURNOS ---")
        self.wrapped.employee.print_shift()

class Employee (Person, ABC):
    available_shifts = {}
    
    def __init__(self, nome, cpf, idade, genero, contato, cargo, salario, turno):
        super().__init__(nome, cpf, idade, genero, contato)
        self.cargo = cargo
        self.__salario = salario
        self._turno = turno
    
    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, novo_salario: float):
        self.__salario = self.__validar_salario(novo_salario)

    def __validar_salario(self, valor) -> float:
        valor = float(valor)
        if valor <= 0:
            raise ValueError("Salário deve ser positivo!")
        return round(valor, 2)

    @property
    def turno(self) -> str:
        return self._turno

    @turno.setter
    def turno(self, novo_turno: str):
        turnos_validos = ["Manhã", "Tarde", "Noite", "Diurno", "Noturno", "Integral", "Plantão 24h"]
        if novo_turno not in turnos_validos:
            raise ValueError(f"Turno inválido. Deve ser um dos: {', '.join(turnos_validos)}.")
        self._turno = novo_turno

    @abstractmethod
    def change_shift(self):
        pass
    
    @classmethod
    @abstractmethod
    def add_shift(cls):
        pass
    
    def update_info(self):
        print(f"\nAtualizando informações do funcionário {self.nome}:")
        self.nome = input(f"Nome [{self.nome}]: ") or self.nome
        self.cpf = input(f"CPF [{self.cpf}]: ") or self.cpf
        self.idade = input(f"Idade [{self.idade}]: ") or self.idade
        self.genero = input(f"Gênero [{self.genero}]: ") or self.genero
        self.contato = input(f"Contato [{self.contato}]: ") or self.contato
        self.salario = input(f"Salário [{self.salario}]: ") or self.salario
        self.turno = input(f"Turno [{self.turno}]: ") or self.turno
    
    def print_info(self):
        print("\nInformações do Funcionário:")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade}")
        print(f"Gênero: {self.genero}")
        print(f"Contato: {self.contato}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {float(self.salario):.2f}")
        print(f"Turno: {self.turno}")
    
    @staticmethod
    def factory(cargo: str, *args):
        cargo = cargo.lower()
        if cargo == "médico" or cargo == "medico":
            from staff import Doctor
            return Doctor(*args)
        elif cargo == "enfermeiro":
            from staff import Nurse
            return Nurse(*args)
        else:
            from staff import Other
            return Other(*args)

class Item:
    def __init__(self, number, name, quantity):
        self.number = number
        self.name = name
        self.quantity = quantity

class Ward:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.patients = []
    
    def add_patient(self, patient):
        from patients import Patient
        if len(self.patients) == self.capacity:
            print("\nQuarto cheio.")
            return False
        self.patients.append(patient)
        patient.ward = self
        print(f"\nPaciente {patient.nome} alocado no quarto {self.number}.")
        return True
    
    def remove_patient(self, patient):
        from patients import Patient
        self.patients.remove(patient)
        patient.ward = None
        print(f"\nPaciente {patient.nome} removido do quarto {self.number}.")
    
    def print_info(self):
        from patients import Patient
        print(f"\nQuarto {self.number} - Capacidade: {self.capacity}")
        if not self.patients:
            print("\nNenhum paciente alocado no quarto.")
            return
        print("\nPacientes:")
        for i, patient in enumerate(self.patients):
            print(f"{i+1}. {patient.nome}, {patient.cpf}")