from app.main import bp

@bp.route("/")
def index():
    return {"message": "Hello, World!"}