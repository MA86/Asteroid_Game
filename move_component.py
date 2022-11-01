from __future__ import annotations
from component import Component
from maths import check_near_zero
from maths import Vector2D


class MoveComponent(Component):
    def __init__(self, owner: Actor, update_order: int = 10) -> None:
        super().__init__(owner, update_order)
        # For simple movement (rad/sec and units/sec)
        self._m_rotation_speed: float = 0.0
        self._m_forward_speed: float = 0.0

        # TODO For Newtonian movement

    # Implements
    def update(self, dt: float) -> None:
        if check_near_zero(self._m_rotation_speed) == False:
            rot: float = self._m_owner.get_rotation()

            # Numeric integration of rotation (rot = speed / time)
            rot = rot + (self._m_rotation_speed * dt)

            self._m_owner.set_rotation(rot)
        if check_near_zero(self._m_forward_speed) == False:
            pos: Vector2D = self._m_owner.get_position()

            # Numeric integration of position (pos = forward (speed / time))
            pos = pos + (self._m_owner.get_forward()
                         * self._m_forward_speed * dt)

            # Screen wrapping (for Asteroid only, remove for generic MoveComponent)
            if pos.x < 0.0:
                pos.x = 1022.0
            elif pos.x > 1024.0:
                pos.x = 2.0
            if pos.y < 0.0:
                pos.y = 766.0
            elif pos.y > 768.0:
                pos.y = 2.0

            self._m_owner.set_position(pos)

    def get_rotation_speed(self) -> float:
        return self._m_rotation_speed

    def get_forward_speed(self) -> float:
        return self._m_forward_speed

    def set_rotation_speed(self, speed: float) -> None:
        self._m_rotation_speed = speed

    def set_forward_speed(self, speed: float) -> None:
        self._m_forward_speed = speed
