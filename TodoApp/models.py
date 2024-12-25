from TodoApp.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

class Todos(Base):
    __tablename__ = 'todos'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    priority: Mapped[str] = mapped_column(String)
    complete: Mapped[bool] = mapped_column(Boolean, default=False)
    
    
    