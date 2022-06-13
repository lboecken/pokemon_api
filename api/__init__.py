from flask import Flask
import os
from dotenv import load_dotenv


load_dotenv()

def create_app():
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    from api.db.pool_management import create_db_pool    
    with app.app_context():
        conn_pool = create_db_pool()
    app.config['DB_POOL'] = conn_pool

    @app.shell_context_processor
    def ctx():
        return {"app": app, "pool": conn_pool}
    
    from api.pokemon.pokemon import pokemon_bp
    app.register_blueprint(pokemon_bp)

    return app