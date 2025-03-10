import logging

from db.base import Base
from db.session import engine
from db.init_db import init_db
from db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if  __name__ == "__main__":
    main()