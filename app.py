import menu
from product import Base, engine


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    menu.menu()