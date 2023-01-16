from flask import Flask, request, render_template, Markup
from text_analyzer import AspectDict
import aspect_words
import pandas as pd
import numpy as np



application = Flask(__name__)
application.config['JSON_AS_ASCII'] = False





@application.route('/search4', methods=['POST'])
def do_search() -> dict:

    text = request.form['phrase']
    title = 'Here are your results:'

    # text = input("Введите текст: ")
    # text = text.lower()
    # text = text.rstrip()

    SE = AspectDict(aspect_words.se)
    SI = AspectDict(aspect_words.si)
    TE = AspectDict(aspect_words.te)
    TI = AspectDict(aspect_words.ti)
    FE = AspectDict(aspect_words.fe)
    FI = AspectDict(aspect_words.fi)
    NE = AspectDict(aspect_words.ne)
    NI = AspectDict(aspect_words.ni)

    """ Создадим финальный словарь """

    final_dict = {}

    first_dict = {}
    first_dict['SE'] = sum(SE.analyze(text).values())
    first_dict['SI'] = sum(SI.analyze(text).values())
    first_dict['TE'] = sum(TE.analyze(text).values())
    first_dict['TI'] = sum(TI.analyze(text).values())
    first_dict['FE'] = sum(FE.analyze(text).values())
    first_dict['FI'] = sum(FI.analyze(text).values())
    first_dict['NE'] = sum(NE.analyze(text).values())
    first_dict['NI'] = sum(NI.analyze(text).values())

    final_dict['SE'] = SE.analyze(text)
    final_dict['SI'] = SI.analyze(text)
    final_dict['TE'] = TE.analyze(text)
    final_dict['TI'] = TI.analyze(text)
    final_dict['FE'] = FE.analyze(text)
    final_dict['FI'] = FI.analyze(text)
    final_dict['NE'] = NE.analyze(text)
    final_dict['NI'] = NI.analyze(text)


    results = first_dict
    results2 = final_dict

    df = pd.DataFrame.from_dict(results2)

    bar_labels = list(results)
    # print (bar_labels)
    bar_values = list(results.values())
    return render_template('results.html', title='', max=max(bar_values), labels=bar_labels, values=bar_values,
                            the_results2=results2,
                            )

    return render_template('results.html',
                           the_phrase=text,
                           the_title=title,
                           the_results=results,
                           the_results2=results2,)

@application.route('/')
@application.route('/entry') 
def entry_page() -> 'html': 
    return render_template('entry.html',
    the_title='Welcome to search4letters on the web!')


if __name__ == '__main__':
    # application.run(host='0.0.0.0')
    application.run(debug=True)
