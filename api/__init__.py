from flask import Flask
import os
from dotenv import load_dotenv


load_dotenv()

def create_app():
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    from api.db.pool_management import connection_pool

    @app.shell_context_processor
    def ctx():
        return {"app": app, "pool": connection_pool}  
    return app