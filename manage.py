from api import create_app

app = create_app()


@app.route('/')
def hello():
    return app.secret_key

if __name__ == "__main__":
    app.run()