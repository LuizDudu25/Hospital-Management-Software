from hospital import Hospital
from patients import patient_area
from appointments import appointments_area
from wards import wards_area
from inventory import inventory
from staff import staff_area
from emergency import emergency
from menus import Menu
from finantial import finantial

def main():
    hospital = Hospital()
    
    while True:
        choice = Menu.main_menu()

        if choice == "1":
            patient_area(hospital)
        elif choice == "2":
            appointments_area(hospital)
        elif choice == '3':
            finantial(hospital)
        elif choice == '4':
            wards_area(hospital)
        elif choice == '5':
            inventory(hospital)
        elif choice == '6':
            staff_area(hospital)
        elif choice == '7':
            emergency(hospital)
        elif choice == "0":
            break
        else:
            print("Opção inválida!")
            input("Pressione ENTER para voltar ao menu.")

if __name__ == "__main__":
    main()