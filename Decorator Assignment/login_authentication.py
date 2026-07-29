def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func()
        else:
            print("Access Denied! Please log in first.")
    return wrapper


@login_required
def dashboard():
    print("Welcome to the Dashboard!")


dashboard(True)
dashboard(False)