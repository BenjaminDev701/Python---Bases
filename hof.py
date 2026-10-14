
# Funciones de orden Superior: Recibes funciones y retornas funciones


def required_auth(func):
    def wrapper(user):
        if (user == "admin"):
            return func(user)
        else:
            return "Acceso denegado"
    return wrapper


# Bienvenida al usuario si es que paso la auth
def view_dashboard(user):
    return f"Bienvenido al panel {user}"


auth_view_dashboard = required_auth(view_dashboard)
print(auth_view_dashboard("admin"))
print(auth_view_dashboard("invited"))
