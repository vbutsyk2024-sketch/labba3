class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, figure_type: str, length: float):
        if length <= 0:
            raise ValueError("Довжина повинна бути більше нуля")
        if figure_type not in self.FIGURES:
            raise ValueError("Невідомий тип фігури")
        self.type = figure_type
        self.length = length

    @property
    def get_angles(self):
        if self.type == "квадрат":
            return 4
        elif self.type == "прямокутник":
            return 4
        elif self.type == "трикутник":
            return 3
        return 0