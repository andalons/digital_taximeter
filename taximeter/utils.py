def get_user_input(prompt: str, valid_inputs: list) -> str:
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if user_input not in valid_inputs:
                raise ValueError("Entrada no válida.")
            return user_input
        except ValueError as e:
            print(f"❌ {e} Por favor, elige una opción válida: {', '.join(valid_inputs)}")
        except Exception as e:
            print(f"Error inesperado: {e}")
