from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from trading_app.domain.config import Config


class DatabaseConnector:
    class DatabaseConnection:
        def __init__(self):
            db_connection_url = 'sqlite:///{}'.format(
                Config().get().get('database', 'sqlite_db_path')
            )
            self.engine = create_engine(db_connection_url)
            self.db_session = sessionmaker(bind=self.engine)

            # Tactical - ensure table exists in database, rather than handling externally for now.
            self._ensure_tables_exist()

        def _ensure_tables_exist(self):
            if not self.engine.dialect.has_table(self.engine, 'tblTrade'):  # If table don't exist, Create.
                from ..model.base import Base
                from ..model.model import Trade  # noqa: F401
                Base.metadata.create_all(bind=self.engine)

        def get_engine(self) -> Engine:
            return self.engine

        def get_session(self) -> Session:
            return self.db_session()

        def close(self):
            self.db_session.close()

    _instance: DatabaseConnection = None

    def __new__(cls):
        if not DatabaseConnector._instance:
            DatabaseConnector._instance = DatabaseConnector.DatabaseConnection()

        return DatabaseConnector._instance
