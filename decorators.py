
# Decorators


def required_auth(func):
    def wrapper(user):
        if (user == "admin"):
            return func(user)
        else:
            return "Acceso denegado"
    return wrapper

# Bienvenida al usuario si es que paso la auth


@required_auth
def view_dashboard(user):
    return f"Bienvenido al panel {user}"


print(view_dashboard("admin"))
print(view_dashboard("invited"))
