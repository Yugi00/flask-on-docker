from flask.cli import FlaskGroup

from project import app, db, User


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    print("dropped all")
    db.create_all()
    print("created all")
    db.session.commit()
    print("committed all")


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()


if __name__ == "__main__":
    cli()
