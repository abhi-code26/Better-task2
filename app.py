from flask import Flask
from flask_cors import CORS
from extensions import db  # ✅ import from extensions

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    db.init_app(app)

    # ✅ Import here AFTER db is initialized
    from comments_api import comments_bp
    app.register_blueprint(comments_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
