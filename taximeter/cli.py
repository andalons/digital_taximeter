from taximeter import Taximeter 
from taximeter.utils import get_user_input

def show_welcome_message():
    print(
    """
    🚖 Bienvenido al Taxímetro Digital 🚖
    -------------------------------------
    Este programa calcula la tarifa de un taxi basándose en el tiempo de trayecto. A continuación las condiciones:

    1. Cuando el taxi está parado, se cobra 2 céntimos por segundo.
    2. Cuando el taxi está en movimiento, se cobra 5 céntimos por segundo.
    3. Hasta indicar lo contrario, por defecto al comenzar el trayecto la tarifa aplicada será la de taxi parado.
    4. Al finalizar un trayecto, podrá iniciar uno nuevo sin necesidad de cerrar el programa. 

    -------------------------------------
    """
    )

def main():
    """
    Función principal que gestiona la interacción con el usuario y el trayecto del taxi.
    """
    taximeter = Taximeter()
    show_welcome_message()
    
    while True:
        user_action = get_user_input(
            "\n¿Desea iniciar un trayecto? (s para sí, n para cancelar): ",
            ['s', 'n']
        )

        if user_action == 's':
            taximeter.reset_trip()  
            print("\n🚀 Iniciando trayecto...")
            taximeter.start_trip()
            while True:
                # Actualización del estado del taxi
                status = get_user_input(
                    "\nEn cada momento, indique si el taxi está en movimiento (m), parado (p) o si desea finalizar el trayecto (f): ",
                    ['m', 'p', 'f']
                )
                if status == 'm':
                    taximeter.update_status(moving=True)
                    print("\n🚗 Taxi en movimiento.")
                elif status == 'p':
                    taximeter.update_status(moving=False)
                    print("\n⛔ Taxi parado.")
                elif status == 'f':
                    taximeter.end_trip()
                    break
        elif user_action == 'n':
            print("👋 ¡Gracias por usar el Taxímetro Digital! Hasta la próxima.")
            break

if __name__ == "__main__":
    main()
