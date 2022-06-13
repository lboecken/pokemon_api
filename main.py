from flask.cli import FlaskGroup

from api import create_app
from api.db.pool_management import get_curs

app = create_app()


@app.route('/')
def hello():
    return 'hello world'

cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def setup_db():
    with get_curs() as cur:
        cur.execute(open('backup.sql').read())
        print('DATABASE RECREATED')


if __name__ == "__main__":
    cli()