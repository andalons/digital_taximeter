from taximeter import Taximeter 

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

        action = input("Quieres iniciar un trayecto? (s/n): ").lower()
        
        while action not in ('s', 'n'):
            print ("❌ Opción no válida. Por favor, elige 's' para sí o 'n' para no.")
            action = input("¿Quieres iniciar un trayecto? (s/n): ").lower()
        
        if action == 's':
            taximeter.start_trip()

            while True:
                status = (input("Indique si el taxi está en movimiento (m), parado(p) o si desea finalizar el trayecto (f): "))
                
                if status == 'm':
                    taximeter.update_status(moving=True)
                    print("🚗 Taxi en movimiento.")

                elif status == 'p':
                    taximeter.update_status(moving=False)
                    print("⛔ Taxi parado.")
                elif status == 'f':
                    taximeter.stop_trip()
                    break
                else:
                    print("❌ Opción no válida. Intenta nuevamente.")
        
        else:
            print("👋 ¡Gracias por usar el Taxímetro Digital! Hasta luego.")
            break

if __name__ == "__main__":
    main()