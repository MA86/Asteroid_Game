from __future__ import annotations
from actor import Actor
from sprite_component import SpriteComponent
from move_component import MoveComponent
from maths import Vector2D, TWO_PI
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
        sc.set_texture(self._m_game.get_texture("assets/asteroid.png"))
        mc = MoveComponent(self)
        mc.set_forward_speed(150.0)

    def get_circle(self) -> CircleComponent:
        return self._m_circle
