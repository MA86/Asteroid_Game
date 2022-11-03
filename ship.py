from __future__ import annotations
import ctypes
import sdl2
from actor import Actor
from sprite_component import SpriteComponent
from input_move_component import InputMoveComponent
from maths import PI
from randoms import Random


class Ship(Actor):
    def __init__(self, game: Game) -> None:
        super().__init__(game)

        self._m_laser_cool_down: float = 0.0

        # Create components for Ship
        sc = SpriteComponent(self, 150)
        sc.set_texture(game.get_texture(b"assets/ship.png"))

        ic = InputMoveComponent(self)
        ic.set_forward_key(sdl2.SDL_SCANCODE_W)
        ic.set_back_key(sdl2.SDL_SCANCODE_S)
        ic.set_clockwise_key(sdl2.SDL_SCANCODE_D)
        ic.set_counter_clockwise_key(sdl2.SDL_SCANCODE_A)
        ic.set_max_rotation_speed(PI)
        ic.set_forward_speed(500.0)
        ic.set_mass(2)

    # Implements
    def update_actor(self, dt: float) -> None:
        # TODO set laser cool down here
        pass

    # Implements
    def input_actor(self, keyb_state: ctypes.Array) -> None:
        # TODO fire laser here
        pass
