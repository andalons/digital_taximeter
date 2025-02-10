def get_user_input(prompt, valid_inputs):
    """
    Pide una entrada al usuario y la valida.
    :param prompt: Mensaje para pedir la entrada.
    :param valid_inputs: Lista de opciones válidas para la entrada del usuario.
    :return: La entrada validada.
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_inputs:
            return user_input
        else:
            print(f"Entrada inválida. Opciones válidas: {', '.join(valid_inputs)}")
