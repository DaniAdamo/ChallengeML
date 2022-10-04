from src.routes import download_data
from src.routes import show_data
from src.app import create_app
from src.routes import login


app = create_app()
app.register_blueprint(download_data.downloader)
app.register_blueprint(show_data.shower)
app.register_blueprint(login.loger)
