from __future__ import annotations
from move_component import MoveComponent
import ctypes


class InputComponent(MoveComponent):
    def __init__(self, owner: Actor) -> None:
        super().__init__(owner)

        # Max forward/rotation speeds
        self._m_max_forward_speed: float = None
        self._m_max_rotation_speed: float = None

        # Keys for forward/rotation movements
        self._m_forward_key: int = 0
        self._m_back_key: int = 0
        self._m_clockwise_key: int = 0
        self._m_counter_clockwise_key: int = 0

    # Implements
    def input(self, keyb_state: ctypes.Array) -> None:
        # Control speed variables of MoveComponent based on keys:
        # Forward/back movement
        forward_speed = 0.0
        if keyb_state[self._m_forward_key]:
            forward_speed += self._m_max_forward_speed
        if keyb_state[self._m_back_key]:
            forward_speed -= self._m_max_forward_speed
        self.set_forward_speed(forward_speed)
        # Rotation movement
        rotation_speed = 0.0
        if keyb_state[self._m_clockwise_key]:
            rotation_speed += self._m_max_rotation_speed
        if keyb_state[self._m_counter_clockwise_key]:
            rotation_speed -= self._m_max_rotation_speed
        self.set_rotation_speed(rotation_speed)

    def get_max_forward(self) -> float:
        return self._m_max_forward_speed

    def get_max_rotation(self) -> float:
        return self._m_max_rotation_speed

    def get_forward_key(self) -> int:
        return self._m_forward_key

    def get_back_key(self) -> int:
        return self._m_back_key

    def get_clockwise_key(self) -> int:
        return self._m_clockwise_key

    def get_counter_clockwise_key(self) -> int:
        return self._m_counter_clockwise_key

    def set_max_forward_speed(self, speed: float) -> None:
        self._m_max_forward_speed = speed

    def set_max_rotation_speed(self, speed: float) -> None:
        self._m_max_rotation_speed = speed

    def set_forward_key(self, key: int) -> None:
        self._m_forward_key = key

    def set_back_key(self, key: int) -> None:
        self._m_back_key = key

    def set_clockwise_key(self, key: int) -> None:
        self._m_clockwise_key = key

    def set_counter_clockwise_key(self, key: int) -> None:
        self._m_counter_clockwise_key = key
