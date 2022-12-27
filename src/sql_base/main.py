from base import Base_check, Base_create
from src.settings import Base

if __name__ == '__main__':
    if not Base_check(Base):
        Base_create(Base, "../../sql/base.sql")