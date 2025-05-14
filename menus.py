import os

class Menu:
    def main_menu():
        os.system('clear')
        
        print("SISTEMA HOSPITALAR\n")
        print("1. Gerenciamento de pacientes")
        print("2. Agendamentos e solicitações")
        print("3. Financeiro")
        print("4. Alocação de quartos")
        print("5. Inventário")
        print("6. Gerenciamento de funcionários")
        print("7. Casos de emergência")
        print("0. Sair\n")
        choice = input("Escolha uma opção: ")

        return choice
    
    def menu_patients():
        os.system('clear')
        print("GERENCIAMENTO DE PACIENTES\n")

        print("1. Lista de pacientes")
        print("2. Registrar novo paciente")
        print("3. Acessar perfil de paciente")
        print("0. Voltar ao menu principal\n")
        choice = input("Escolha uma opção: ")

        return choice
    
    def menu_patient_profile(patient, printer):
        os.system('clear')
        print(f"PERFIL DO PACIENTE {patient.nome}")
        printer.print_info()

        print("\n1. Atualizar informações")
        print("2. Histórico médico")
        print("3. Prescrições médicas")
        print("4. Testes de laboratório")
        print("0. Voltar ao menu de pacientes\n")
        choice = input("Escolha uma opção: ")

        return choice
    
    def menu_appointments():
        os.system('clear')
        print("ÁREA DE EXAMES E CONSULTAS\n")

        print("1. Agendar consulta")
        print("2. Cancelar consulta")
        print("3. Reagendar consulta")
        print("4. Solicitar teste de laboratório")
        print("0. Voltar ao menu principal\n")
        choice = input("Escolha uma opção: ")

        return choice
    
    def menu_plan():
        print("\nQual o tipo de atendimento desejado?\n")

        print("1. Convênio")
        print("2. Particular")
        print("3. SUS")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            return 'Convênio'
        elif choice == '2':
            return 'Particular'
        elif choice == '3':
            return 'SUS'
        else:
            print("\nOpção inválida!")
            return Menu.menu_plan()
    
    def menu_finantial():
        os.system('clear')
        print("FINANCEIRO\n")

        print("1. Faturamento total")
        print("2. Faturamento por paciente")
        print("0. Voltar ao menu principal\n")
        choice = input("Escolha uma opção: ")

        return choice

    def menu_wards():
        os.system('clear')
        print("ALOCAÇÃO DE QUARTOS\n")

        print("1. Gerenciar quartos")
        print("2. Gerenciar alocação de pacientes")
        print("0. Voltar ao menu principal\n")
        choice = input("Escolha uma opção: ")

        return choice
    
    def menu_wards_management():
        os.system('clear')
        print("GERENCIAMENTO DE QUARTOS\n")

        print("1. Adicionar quarto")
        print("2. Remover quarto")
        print("3. Atualizar informações do quarto")
        print("4. Lista de quartos")
        print("0. Voltar ao menu de alocação de quartos\n")
        choice = input("Escolha uma opção: ")

        return choice
    
    def menu_wards_patients():
        os.system('clear')
        print("GERENCIAMENTO DE PACIENTES ALOCADOS\n")

        print("1. Alocar paciente")
        print("2. Desalocar paciente")
        print("3. Realocar paciente")
        print("0. Voltar ao menu de alocação de quartos\n")
        choice = input("Escola uma opção: ")

        return choice
    
    def menu_inventory():
        os.system('clear')
        print("INVENTÁRIO\n")

        print("1. Lista de itens")
        print("2. Adicionar item")
        print("3. Remover item")
        print("4. Atualizar informações do item")
        print("0. Voltar ao menu principal\n")
        choice = input("Escolha uma opção: ")

        return choice

    def menu_staff():
        os.system('clear')
        print("GERENCIAMENTO DE FUNCIONÁRIOS\n")

        print("1. Lista de funcionários")
        print("2. Adicionar funcionário")
        print("3. Perfil de funcionário")
        print("4. Remover funcionário")
        print("0. Voltar ao menu principal\n")
        choice = input("Escolha uma opção: ")

        return choice
    
    def menu_group():
        print("\nEm qual grupo deseja realizar essa operação?\n")

        print("1. Médicos")
        print("2. Enfermeiros")
        print("3. Outros")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            return 'Médico'
        elif choice == '2':
            return 'Enfermeiro'
        elif choice == '3':
            return 'Outros'
        else:
            print("\nOpção inválida!")
            return Menu.menu_group()
    
    def menu_emergency():
        os.system('clear')
        print("CASOS DE EMERGÊNCIA\n")

        print("1. Lista de espera")
        print("2. Adicionar caso de emergência")
        print("3. Chamar próximo paciente")
        print("0. Voltar ao menu principal\n")
        choice = input("Escolha uma opção: ")

        return choice
    
    def menu_specialty():
        print("\nQual especialidade deseja chamar?\n")
        print("1. Clínico Geral")
        print("2. Ortopedia")
        print("3. Cardiologia")
        print("4. Neurologia")
        print("5. Pediatria")
        print("6. Ginecologia")
        print("7. Oftalmologia")
        print("8. Dermatologia")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            return 'Clínico Geral'
        elif choice == '2':
            return 'Ortopedia'
        elif choice == '3':
            return 'Cardiologia'
        elif choice == '4':
            return 'Neurologia'
        elif choice == '5':
            return 'Pediatria'
        elif choice == '6':
            return 'Ginecologia'
        elif choice == '7':
            return 'Oftalmologia'
        elif choice == '8':
            return 'Dermatologia'
        else:
            print("\nOpção inválida!")
            return Menu.menu_specialty()