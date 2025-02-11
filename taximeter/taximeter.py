import time
from taximeter.logger import logger

class Taximeter: 
    def __init__(self):
        self.is_moving = False
        self.start_time = None
        self.total_cost = 0.0
        self.last_update_time = None
        self.acc_moving_time = 0.0 
        self.acc_stopped_time = 0.0 
        logger.info("Program initialized.")  # Log de inicialización

    
    def start_trip(self):
        self.start_time = time.time()
        self.last_update_time = self.start_time
        self.total_cost = 0.0
        self.acc_moving_time = 0.0
        self.acc_stopped_time = 0.0
        logger.info("Trip started.")
        print("🚖 ¡Taxímetro en marcha!")
    
    def update_status(self, moving: bool = None):

        if self.start_time is None or self.last_update_time is None:
            logger.warning("No se puede actualizar el estado antes de iniciar el viaje.")
            return
        
        current_time = time.time()
        elapsed_time = current_time - self.last_update_time

        # Actualiza el tiempo y coste según el estado actual
        if self.is_moving:
            self.acc_moving_time += elapsed_time
            self.total_cost += elapsed_time * 0.05  # 5 céntimos por segundo en movimiento
            logger.info(f"Taxi moving. +{elapsed_time:.2f}s, Total Cost: {self.total_cost:.2f}€")

        else:
            self.acc_stopped_time += elapsed_time
            self.total_cost += elapsed_time * 0.02  # 2 céntimos por segundo parado
            logger.info(f"Taxi stopped. +{elapsed_time:.2f}s, Total Cost: {self.total_cost:.2f}€")

        
        self.last_update_time = current_time

        # Solo cambia el estado si se proporciona un valor
        if moving is not None:
            self.is_moving = moving
            logger.info(f"Taxi status updated: {'Moving' if moving else 'Stopped'}")


        print(f"\n⏱️ Tiempo acumulado en movimiento: {self.acc_moving_time:.2f} segundos")
        print(f"⏱️ Tiempo acumulado en parado: {self.acc_stopped_time:.2f} segundos")
    
    def end_trip(self):
        # Asegura que el tiempo y coste se actualicen antes de finalizar
        self.update_status()
        logger.info(f"Trip ended. Total Cost: {self.total_cost:.2f}€")
        print(f"\nTrayecto finalizado.")
        print(f"💰 Total a pagar: {self.total_cost:.2f}€")
    
    def reset_trip(self):
        """
        Resetea el taxímetro a sus valores iniciales para iniciar un nuevo trayecto.
        """
        self.is_moving = False
        self.start_time = None
        self.total_cost = 0.0
        self.last_update_time = None
        self.acc_moving_time = 0.0 
        self.acc_stopped_time = 0.0
        logger.info("Trip reset.")

