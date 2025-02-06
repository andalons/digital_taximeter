import time

class Taximeter: 
    def __init__(self):
        self.is_moving = False
        self.start_time = None
        self.total_cost = 0.0
        self.last_update_time = None
    
    def start_trip(self):
        print("🚀 Iniciando trayecto...")
        self.start_time = time.time()
        self.last_update_time = self.start_time
        self.total_cost = 0.0
    
    def update_status(self, moving:bool):
        current_time = time.time()
        elapsed_time = current_time - self.last_update_time

        if self.is_moving:
            self.total_cost += elapsed_time * 0.05 # 5 céntimos por segundo en movimiento
        else:
            self.total_cost += elapsed_time * 0.02 # 2 céntimos por segundo parado
        
        self.is_moving = moving
        self.last_update_time = current_time
    
    def stop_trip(self):
        self.update_status(self.is_moving)
        print(f"🏁 Trayecto finalizado. Total a pagar: {self.total_cost:.2f}€")