from __future__ import annotations
from actor import Actor
from sprite_component import SpriteComponent
from move_component import MoveComponent
from maths import Vector2D, TWO_PI, PI_OVER_TWO
from randoms import Random


class Asteroid(Actor):
    def __init__(self, game: Game) -> None:
        super().__init__(game)

        self._m_circle: CircleComponent = None

        # Initialize position/orientation
        rand_pos: Vector2D = Random.get_vector(
            Vector2D(0.0, 0.0), Vector2D(1024.0, 768.0))
        self.set_position(rand_pos)
        self.set_rotation(Random.get_float_range(0.0, TWO_PI))

        # Add components
        sc = SpriteComponent(self)
        sc.set_texture(self._m_game.get_texture(b"assets/asteroid.png"))
        mc = MoveComponent(self)
        mc.set_rotation_speed(Random.get_float_range(0.0, PI_OVER_TWO))
        mc.set_mass(1)
        mc.add_force(self.get_forward() * 3000.0)

    def get_circle(self) -> CircleComponent:
        return self._m_circle
