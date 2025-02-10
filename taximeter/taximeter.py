import time

class Taximeter: 
    def __init__(self):
        self.is_moving = False
        self.start_time = None
        self.total_cost = 0.0
        self.last_update_time = None
        self.acc_moving_time = 0.0  # Tiempo acumulado en movimiento
        self.acc_stopped_time = 0.0  # Tiempo acumulado en parado
    
    def start_trip(self):
        print("🚀 Iniciando trayecto...")
        self.start_time = time.time()
        self.last_update_time = self.start_time
        self.total_cost = 0.0
        self.acc_moving_time = 0.0
        self.acc_stopped_time = 0.0
        
        print("⛔ El taxi comienza parado.")
    
    def update_status(self, moving: bool = None):
        current_time = time.time()
        elapsed_time = current_time - self.last_update_time

        # Actualiza el tiempo y coste según el estado actual
        if self.is_moving:
            self.acc_moving_time += elapsed_time
            self.total_cost += elapsed_time * 0.05  # 5 céntimos por segundo en movimiento
        else:
            self.acc_stopped_time += elapsed_time
            self.total_cost += elapsed_time * 0.02  # 2 céntimos por segundo parado
        
        self.last_update_time = current_time

        # Solo cambia el estado si se proporciona un valor
        if moving is not None:
            self.is_moving = moving

        print(f"⏱️ Tiempo acumulado en movimiento: {self.acc_moving_time:.2f} segundos")
        print(f"⏱️ Tiempo acumulado en parado: {self.acc_stopped_time:.2f} segundos")
    
    def end_trip(self):
        # Asegura que el tiempo y coste se actualicen antes de finalizar
        self.update_status()
        print(f"💰 Total a pagar: {self.total_cost:.2f}€")
