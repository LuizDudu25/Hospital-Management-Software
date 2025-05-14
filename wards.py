from models import Ward
from menus import Menu

def wards_patient_area(hospital):
    from patients import Patient
    choice = Menu.menu_wards_patients()

    if choice == '1':
        cpf = input("\nDigite o CPF do paciente: ")
        patient = hospital.find_person(cpf, hospital.patients)
        ward = hospital.find_ward()
        if ward.add_patient(patient):
            patient.ward = ward
    elif choice == '2':
        cpf = input("\nDigite o CPF do paciente: ")
        patient = hospital.find_person(cpf, hospital.patients)
        patient.ward.remove_patient(patient)
        patient.ward = None
    elif choice == '3':
        cpf = input("\nDigite o CPF do paciente: ")
        patient = hospital.find_person(cpf, hospital.patients)
        patient.reallocate(hospital)
    elif choice == '0':
        return
    else:
        print("\nOpção inválida!")
    
    input("\nPressione ENTER para continuar ")

def wards_management_area(hospital):
    while True:
        choice = Menu.menu_wards_management()

        if choice == '1':
            number = input("\nNúmero do quarto: ")
            if next((ward for ward in hospital.wards if ward.number == number), None):
                print("\nNúmero de quarto já registrado.")
                continue
            capacity = int(input("Capacidade do quarto: "))
            new_ward = Ward(number, capacity)
            hospital.wards.append(new_ward)
        elif choice == '2':
            ward = hospital.find_ward()
            if ward.patients:
                reallocate = input("\nHá pacientes alocados no quarto. Deseja realocá-los? (S/N) ")
                if reallocate == 'S':
                    for patient in ward.patients:
                        patient.reallocate(hospital, ward)
                else:
                    for patient in ward.patients:
                        patient.ward = None
            hospital.wards.remove(ward)
        elif choice == '3':
            ward = hospital.find_ward()
            ward.print_info()
            choice = input("\nDeseja alterar o número do quarto? (S/N) ")
            if choice == 'S':
                new_number = input("\nNovo número do quarto: ")
                ward.number = new_number
            choice = input("\nDeseja alterar a capacidade do quarto? (S/N) ")
            if choice == 'S':
                new_capacity = int(input("\nNova capacidade do quarto: "))
                if len(ward.patients) > new_capacity:
                    print("\nCapacidade insuficiente para alocar os pacientes. É preciso realoca-los.")
                    while len(ward.patients) > new_capacity:
                        choice = input("Qual paciente deseja realocar? ")
                        patient = ward.patients.pop(choice-1)
                        patient.reallocate(hospital, ward)
        elif choice == '4':
            if not hospital.wards:
                print("\nNenhum quarto registrado.")
                continue
            for ward in hospital.wards:
                ward.print_info()
        elif choice == '0':
            break
        else:
            print("\nOpção inválida!")
        
        input("\nPressione ENTER para continuar ")

def wards_area(hospital):
    while True:
        choice = Menu.menu_wards()

        if choice == '1':
            wards_management_area(hospital)
        elif choice == '2':
            wards_patient_area(hospital)
        elif choice == '0':
            break
        else:
            print("\nOpção inválida!")
        
        input("\nPressione ENTER para continuar ")