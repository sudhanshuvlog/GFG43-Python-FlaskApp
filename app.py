from flask import Flask


def create_app():
    x=10
    y=10
    app = Flask(__name__)
    print("inside create_app function")

    @app.route('/')
    def home():
        print("inside home function")
        return 'Hi hi GFG43 25th april 2026 12345'

    @app.route('/test')
    def test():
        print("inside home function")
        x=5
        while x>1:
            print(x)
        break
        return 'Hi hi GFG43 25th april 2026 12345'

    return app


if __name__ == '__main__':
    app = create_app()

    app.run(host='0.0.0.0', port=80, debug=True)
