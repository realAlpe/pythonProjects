from enum import Enum, auto


class EdgeType(Enum):
    GT = auto()
    LT = auto()

    def swap(self):
        if self == EdgeType.GT:
            return EdgeType.LT
        if self == EdgeType.LT:
            return EdgeType.GT
        raise ValueError("Invalid EdgeType.")

    def to_unicode(self, vertical: bool = False) -> str:
        if vertical:
            return "^" if self == EdgeType.LT else "v"
        else:
            return "<" if self == EdgeType.LT else ">"
