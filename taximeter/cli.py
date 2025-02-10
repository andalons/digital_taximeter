from taximeter import Taximeter 
from taximeter.utils import get_user_input

def show_welcome_message():
    print(
        """
    🚖 Bienvenido al Taxímetro Digital 🚖
    -------------------------------------
    Instrucciones:
    1. Inicia un trayecto.
    2. Marca cuando el taxi esté en movimiento o parado.
    3. Finaliza el trayecto para ver el total.
    -------------------------------------
    """
    )

def main():
    taximeter = Taximeter()

    while True:
        show_welcome_message()

        action = get_user_input("¿Quieres iniciar un trayecto? (s/n): ", ['s', 'n'])
        
        if action == 's':
            taximeter.start_trip()

            while True:

                status = get_user_input("Indique si el taxi está en movimiento (m), parado (p) o si desea finalizar el trayecto (f): ", ['m', 'p', 'f'])
                
                if status == 'm':
                    taximeter.update_status(moving=True)
                    print("🚗 Taxi en movimiento.")

                elif status == 'p':
                    taximeter.update_status(moving=False)
                    print("⛔ Taxi parado.")
                elif status == 'f':
                    taximeter.end_trip()
                    break
        
        else:
            print("👋 ¡Gracias por usar el Taxímetro Digital! Hasta la próxima.")
            break

if __name__ == "__main__":
    main()