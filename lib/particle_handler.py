import random as rd
from .particle import PointParticle


def rocket_launch(particle: PointParticle) -> None:

    particle.vel = particle.vel.update_y(rd.random() / 20)
    particle.size -= rd.random() / 5


def rocket_basic_explosion(particle: PointParticle) -> None:

    particle.vel = particle.vel.update_y(rd.random() / 15)
    particle.size -= rd.random() / 15


def rocket_image_explosion(particle: PointParticle) -> None:

    particle.vel = particle.vel.update_y(rd.random() / 20)
    particle.size -= rd.random() / 25


def rocket_line_explosion(particle: PointParticle) -> None:

    particle.vel = particle.vel.update_y(rd.random() / 40 * particle.vel.length())
    particle.size -= rd.random() / 15


def fountain_basic(particle: PointParticle) -> None:

    particle.vel = particle.vel.update_y(rd.random() / 5)
    particle.size -= rd.random() / 15
