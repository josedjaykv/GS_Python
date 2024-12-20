from ui.login_window import launch_login
from database.db_manager import initialize_database

if __name__ == "__main__":
    initialize_database()
    launch_login()
