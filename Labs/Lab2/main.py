import calculations
import report

def main():
    results = {}

    print("1. Bus")
    print("2. Train")
    print("3. Airplane")
    
    choice = input("Выберите тип транспорта (1,2,3): ")
    
    if choice == '1':
        mode = 'bus'
    elif choice == '2':
        mode = 'train'
    elif choice == '3':
        mode = 'airplane'
    else:
        print("Неверное значение")
        return
    
    distance = float(input("Ввод растояния (в км): "))
    speed = float(input("Ввод средней скорости (км/ч): "))
    ticket_price = float(input("Цена билета: "))
    passengers = int(input("Кол-во пасажиров: "))
    
    transport = calculations.create_transport(mode, distance, speed, ticket_price)
    
    time, cost = calculations.get_trip_info(transport, passengers)
    results[mode] = {"time": time, "cost": cost}
    
    print("Результат:")
    for mode, info in results.items():
        print(f'Транспорт: {mode}, Время: {info["time"]:.2f} часов, Стоимость: ${info["cost"]:.2f}')
    
    save_choice = input("Хотите сохранить результат? (Y - да, N - нет): ")
    
    if save_choice.lower() == 'y':
        format_choice = input("Выберите формат (docx/xls): ")
        
        if format_choice.lower() == 'docx':
            report.save_to_docx(results)
            print("Results saved to report.docx")
        
        elif format_choice.lower() == 'xls':
            report.save_to_xls(results)
            print("Results saved to report.xlsx")
        
        else:
            print("Invalid format choice.")
    
if __name__ == "__main__":
    main()