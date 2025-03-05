from app import create_app
from datetime import timedelta
from flask_jwt_extended import JWTManager
from app.config import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRE_HOURS, JWT_REFRESH_EXPIRE_DAYS
from flask_cors import CORS

app = create_app()

CORS(app)

app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=int(JWT_EXPIRE_HOURS))
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=int(JWT_REFRESH_EXPIRE_DAYS))
app.config["JWT_ALGORITHM"] = JWT_ALGORITHM

jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
