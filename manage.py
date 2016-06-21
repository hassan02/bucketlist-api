from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand

from app import app
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    """Creates database tables from sqlalchemy models"""
    db.create_all()


@manager.command
def drop_db():
    """Drops database tables"""
    if prompt_bool("Are you sure you want to delete all your data?"):
        db.drop_all()

if __name__ == '__main__':
    manager.run()
