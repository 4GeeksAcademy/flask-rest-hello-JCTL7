from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    username: Mapped[str] = mapped_column(String(12), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(120), nullable=False)
    bio: Mapped[str] = mapped_column(String(350), nullable=True)
    url_profile_picture: Mapped[str] = mapped_column(String(350), nullable=True)

    favorites = relationship("Favorites", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "username": self.username,
            "full_name": self.full_name,
            "bio": self.bio,
            "url_profile_picture": self.url_profile_picture
        }
    
class People(db.Model):
    __tablename__="People"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    height: Mapped[str] = mapped_column(String(50), nullable=True)
    mass: Mapped[str] = mapped_column(String(50), nullable=True)
    hair_color: Mapped[str] = mapped_column(String(50), nullable=True)
    skin_color: Mapped[str] = mapped_column(String(50), nullable=True)
    eye_color: Mapped[str] = mapped_column(String(50), nullable=True)
    birth_year: Mapped[str] = mapped_column(String(50), nullable=True)
    gender: Mapped[str] = mapped_column(String(50), nullable=True)

    favorited_by = relationship("Favorites", back_populates="people")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }
    
class Planets(db.Model):
    __tablename__ = "Planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    diameter: Mapped[str] = mapped_column(String(50), nullable=True)
    rotation_period: Mapped[str] = mapped_column(String(50), nullable=True)
    orbital_period: Mapped[str] = mapped_column(String(50), nullable=True)
    gravity: Mapped[str] = mapped_column(String(50), nullable=True)
    population: Mapped[str] = mapped_column(String(50), nullable=True)
    climate: Mapped[str] = mapped_column(String(50), nullable=True)
    terrain: Mapped[str] = mapped_column(String(50), nullable=True)

    favorited_by = relationship("Favorites", back_populates="planet")
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain
        }
    
class Vehicles(db.Model):
    __tablename__ = "Vehicles"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    model: Mapped[str] = mapped_column(String(120), nullable=True)
    manufacturer: Mapped[str] = mapped_column(String(120), nullable=True)
    cost_in_credits: Mapped[str] = mapped_column(String(50), nullable=True)
    length: Mapped[str] = mapped_column(String(50), nullable=True)
    crew: Mapped[str] = mapped_column(String(50), nullable=True)
    passengers: Mapped[str] = mapped_column(String(50), nullable=True)
    vehicle_class: Mapped[str] = mapped_column(String(50), nullable=True)


    favorited_by = relationship("Favorites", back_populates="vehicle")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "vehicle_class": self.vehicle_class
        }  

class Favorites(db.Model):
    __tablename__ = "Favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False)
    people_id: Mapped[int] = mapped_column(ForeignKey("People.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey("Planet.id"), nullable=False)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("Vehicles.id"), nullable=False)

    user = relationship("User", back_populates="favorites")
    people = relationship("People", back_populates="favorites")
    planet = relationship("Planets", back_populates="favorites")
    vehicle = relationship("Vehicles", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }