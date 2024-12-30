import random as rd
from .particle import PointParticle


def rocket_launch(particle: PointParticle) -> None:

    particle.vel = particle.vel.update_y(rd.random() / 20)
    particle.size -= rd.random() / 5


def rocket_basic_explosion(particle: PointParticle) -> None:

    particle.vel = particle.vel.update_y(rd.random() / 15)
    particle.size -= rd.random() / 18


def rocket_image_explosion(particle: PointParticle) -> None:

    particle.vel = particle.vel.update_y(rd.random() / 15)
    particle.size -= rd.random() / 20


def fountain_basic(particle: PointParticle) -> None:

    particle.vel = particle.vel.update_y(rd.random() / 15)
    particle.size -= rd.random() / 20
