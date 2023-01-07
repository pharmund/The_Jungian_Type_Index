class AspectDict:
    """Анализатор текста"""

    def __init__(self, aspect_words):
        self.aspect_dict: dict = {}
        self.new_aspect_dict: dict = {}

        for word in aspect_words:
            self.aspect_dict[word] = 0

    def analyze(self, text) -> dict:
        for word in self.aspect_dict:
            if word in text:
                self.aspect_dict[word] = text.count(word)

        for word in self.aspect_dict:
            if self.aspect_dict[word] != 0:
                self.new_aspect_dict[word] = self.aspect_dict[word]
        
        return self.new_aspect_dict



