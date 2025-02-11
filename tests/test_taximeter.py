import unittest
from taximeter import Taximeter
from taximeter.logger import logger
import time

class TestTaximeter(unittest.TestCase):
    
    def setUp(self):
        """Configuramos el taxímetro antes de cada test"""
        self.taximeter = Taximeter()
        self.taximeter.start_trip()
    
    def tearDown(self):
        """Limpiamos después de cada test"""
        self.taximeter.end_trip()
    
    def test_start_trip(self):
        """Comprobamos que el trayecto se inicia correctamente"""
        self.assertIsNotNone(self.taximeter.start_time)
        self.assertEqual(self.taximeter.total_cost, 0.0)
    
    def test_update_status_moving(self):
        """Comprobamos que al actualizar el estado a 'movimiento' se actualiza el coste"""
        initial_cost = self.taximeter.total_cost
        self.taximeter.update_status(moving=True)
        time.sleep(1)  # Simulamos un segundo de trayecto
        self.taximeter.update_status(moving=True)
        self.assertGreater(self.taximeter.total_cost, initial_cost)
    
    def test_update_status_stopped(self):
        """Comprobamos que al actualizar el estado a 'parado' se actualiza el coste"""
        initial_cost = self.taximeter.total_cost
        self.taximeter.update_status(moving=False)
        time.sleep(1)  # Simulamos un segundo de trayecto
        self.taximeter.update_status(moving=False)
        self.assertGreater(self.taximeter.total_cost, initial_cost)

    def test_end_trip(self):
        """Comprobamos que el coste total se muestra correctamente al finalizar el trayecto"""
        self.taximeter.end_trip()
        self.assertGreater(self.taximeter.total_cost, 0.0)

    def test_reset_trip(self):
        """Comprobamos que el reseteo del trayecto funciona correctamente"""
        self.taximeter.reset_trip()
        self.assertEqual(self.taximeter.total_cost, 0.0)
        self.assertIsNone(self.taximeter.start_time)

    def test_logging_on_trip_start(self):
        """Comprobamos que se genera un log al iniciar el trayecto"""
        with self.assertLogs(logger, level='INFO') as log:
            self.taximeter.start_trip()
            self.assertIn("Trip started.", log.output[0])

if __name__ == '__main__':
    unittest.main()
