class TextAnalyzer:
    """Класс, который подсчитывает, сколько слов из входного текста попало под какие категории"""

    def __init__(self):
        self.group_classification: dict = {}

    def add_group_str(self, name: str, group: str):
        self.add_group_list(name, group.split(', '))

    def add_group_list(self, name: str, group: list):
        self.group_classification[name] = group

    def analyze(self, text: str) -> dict:
        result = {}
        for name, group in self.group_classification.items():
            result[name] = self.__analyze_group(group, text)
        return result

    def __analyze_group(self, group: list, text: str) -> int:
        match = 0
        for word in group:
            if word in text:
                match += 1
        return match
