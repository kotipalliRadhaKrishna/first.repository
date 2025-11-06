from sqlalchemy import Column, Integer, String
from database import Base



# -------------------- PATIENT --------------------
from sqlalchemy import Column, Integer, String
from database import Base

# from sqlalchemy import Column, Integer, String
# from database import Base

class Patient(Base):
    __tablename__ = "patientsn b"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, index=True, nullable=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=True)
    e_mail = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    conform_password = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    blood_group = Column(String, nullable=True)
    city = Column(String, nullable=True)
    country = Column(String, nullable=True)

# -------------------- DOCTOR --------------------
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    gmail = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


# -------------------- ADMIN --------------------
class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    gmail = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


#--------------------add staff model-------------

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(String, unique=True, index=True)
    name = Column(String)
    specialization = Column(String)
    email = Column(String)
    password = Column(String)

class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, index=True)
    admin_id = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Staff(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(String, unique=True, index=True)
    name = Column(String)
    role = Column(String)
    email = Column(String)


