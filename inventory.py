from menus import Menu

def inventory(hospital):
    choice = Menu.menu_inventory()

    if choice == '1':
        print("\nInventário:")
        for item in hospital.inventory:
            print(f"{item.number}. {item.name} - {item.quantity}")
    elif choice == '2':
        item = hospital.find_item()
        if item:
            quantity = input("\nQuantidade a adicionar: ")
            item.quantity += int(quantity)
            print(f"\nItem {item.name} adicionado ao inventário.")
        else:
            choice = input("Registrar item? (S/N) ")
            if choice == 'S':
                from models import Item
                number = len(hospital.inventory) + 1
                name = input("Nome do item: ")
                quantity = input("Quantidade: ")
                new_item = Item(number, name, int(quantity))
                hospital.inventory.append(new_item)
                print(f"\nItem {name} adicionado ao inventário.")
    elif choice == '3':
        item = hospital.find_item()
        if item:
            while True:
                quantity = input("\nQuantidade a remover: ")
                if int(quantity) > item.quantity:
                    print("\nQuantidade inválida.")
                else:
                    item.quantity -= int(quantity)
                    print(f"\nItem {item.name} removido do inventário.")
                    break
    elif choice == '0':
        return
    else:
        print("\nOpção inválida.")
    
    input("\nPressione ENTER para continuar ")