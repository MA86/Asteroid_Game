from __future__ import annotations
from component import Component


class CircleComponent(Component):
    def __init__(self, owner: Actor) -> None:
        super().__init__(owner)

        self._m_radius: float = 0.0

    def intersect(self, circle_a: CircleComponent, circle_b: CircleComponent) -> bool:
        # Compute distance squared
        dist: Vector2D = circle_a.get_center() - circle_b.get_center()
        # TODO

    def get_center(self) -> float:
        pass

    def get_radius(self) -> float:
        return self._m_radius

    def set_radius(self, radius: float) -> None:
        self._m_radius = radius
