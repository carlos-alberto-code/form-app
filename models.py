from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy     import String, Integer

class Base(DeclarativeBase):
    pass

class Persona(Base):
    __tablename__ = 'persona'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50))
    edad: Mapped[int] = mapped_column(Integer)
    telefono: Mapped[str] = mapped_column(String(10))
