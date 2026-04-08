from database import Base #ek "blueprint" ya "template" hai jiske sahare aap Python classes ko database tables mein badalte hain.
from sqlalchemy import String,Column,Integer    

class Stock(Base):
    __tablename__ = "stocks"
    id = Column(Integer, primary_key = True, index =True)
    name = Column(String,index = True)
    price = Column(Integer)