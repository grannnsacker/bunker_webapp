from flask import Flask
from flask_migrate import Migrate

from models import User
from store.config import PostgresConfig
from store.postgres import sa

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = PostgresConfig.db_url
app.config["SECRET_KEY"] = "S3cr3tK3y"

sa.init_app(app)
migrate = Migrate(app, sa)


@app.route("/card/<string:card_name>/<string:user_id>", methods=["GET"])
def switch_card_(card_name: str, user_id: str):
    settings_ = get_user_by_user_id(user_id).settings
    if card_name == "exchange_add":
        pass
    sa.session.commit()


def get_user_by_user_id(user_id: str):
    user = sa.session.query(User).filter_by(user_id=user_id).first()
    return user


if __name__ == "__main__":
    app.run(debug=True)