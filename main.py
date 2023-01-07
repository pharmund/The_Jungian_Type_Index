from text_analyzer import AspectDict
import aspect_words

if __name__ == "__main__":

    text = input("Введите текст: ")
    text = text.lower()
    text = text.rstrip()

    SE = AspectDict(aspect_words.se)
    SI = AspectDict(aspect_words.si)
    TE = AspectDict(aspect_words.te)
    TI = AspectDict(aspect_words.ti)
    FE = AspectDict(aspect_words.fe)
    FI = AspectDict(aspect_words.fi)
    NE = AspectDict(aspect_words.ne)
    NI = AspectDict(aspect_words.ni)


    # """ Создадим финальный словарь """
    final_dict = {}
    final_dict['SE'] = SE.analyze(text)
    final_dict['SI'] = SI.analyze(text)
    final_dict['TE'] = TE.analyze(text)
    final_dict['TI'] = TI.analyze(text)
    final_dict['FE'] = FE.analyze(text)
    final_dict['FI'] = FI.analyze(text)
    final_dict['NE'] = NE.analyze(text)
    final_dict['NI'] = NI.analyze(text)

    print (final_dict)