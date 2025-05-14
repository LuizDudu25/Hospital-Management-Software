from menus import Menu

def finantial(hospital):
    while True:
        choice = Menu.menu_finantial()

        if choice == '1':
            print(f"Faturamento total: R$ {hospital.invoicing}")
        elif choice == '2':
            cpf = input("\nDigite o CPF do paciente: ")
            patient = hospital.find_person(cpf, hospital.patients)
            if patient:
                print(f"Faturas de {patient.nome}:")
                for bill in patient.bills:
                    print("R$ ", bill)
            
                print("\nTotal: R$ ", sum(patient.bills))

                choice = input("\nDeseja adicionar uma nova fatura? (S/N) ")
                if choice == 'S':
                    bill = float(input("Valor da fatura: "))
                    patient.add_bill(bill)
                    hospital.invoicing += bill
                    print("\nFatura adicionada com sucesso.")
            else:
                print("\nPaciente não encontrado.")
        elif choice == '0':
            break
        else:
            print("\nOpção inválida!")
        
        input("\nPressione ENTER para continuar ")