from flask import Flask, request, render_template
from text_analyzer import AspectDict
import aspect_words
from itertools import chain
from itertools import zip_longest

import re, operator
import operator

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from log_request import log_request



application = Flask(__name__)
application.config['JSON_AS_ASCII'] = False

@application.route('/')
@application.route('/entry') 
def entry_page() -> 'html': 
    return render_template('entry.html',
    the_title='Welcome to search4words on the web!')


@application.route('/search4', methods=['POST'])
def do_search() -> dict:

    text = request.form['phrase']
    title = 'Here are your results:'

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

    sorted_SE = sorted(SE.analyze(text).items(), key=lambda x: x[1], reverse=True)
    tuple_SE = (list(first_dict)[0], first_dict['SE'])
    sorted_SE.insert(0, tuple_SE)
    sorted_SE = list(map(list, sorted_SE))

    sorted_SI = sorted(SI.analyze(text).items(), key=lambda x: x[1], reverse=True)
    tuple_SI = (list(first_dict)[1], first_dict['SI'])
    sorted_SI.insert(0, tuple_SI)
    sorted_SI = list(map(list, sorted_SI))

    sorted_TE = sorted(TE.analyze(text).items(), key=lambda x: x[1], reverse=True)
    tuple_TE = (list(first_dict)[2], first_dict['TE'])
    sorted_TE.insert(0, tuple_TE)
    sorted_TE = list(map(list, sorted_TE))

    sorted_TI = sorted(TI.analyze(text).items(), key=lambda x: x[1], reverse=True)
    tuple_TI = (list(first_dict)[3], first_dict['TI'])
    sorted_TI.insert(0, tuple_TI)
    sorted_TI = list(map(list, sorted_TI))

    sorted_FE = sorted(FE.analyze(text).items(), key=lambda x: x[1], reverse=True)
    tuple_FE = (list(first_dict)[4], first_dict['FE'])
    sorted_FE.insert(0, tuple_FE)
    sorted_FE = list(map(list, sorted_FE))

    sorted_FI = sorted(FI.analyze(text).items(), key=lambda x: x[1], reverse=True)
    tuple_FI = (list(first_dict)[5], first_dict['FI'])
    sorted_FI.insert(0, tuple_FI)
    sorted_FI = list(map(list, sorted_FI))

    sorted_NE = sorted(NE.analyze(text).items(), key=lambda x: x[1], reverse=True)
    tuple_NE = (list(first_dict)[6], first_dict['NE'])
    sorted_NE.insert(0, tuple_NE)
    sorted_NE = list(map(list, sorted_NE))

    sorted_NI = sorted(NI.analyze(text).items(), key=lambda x: x[1], reverse=True)
    tuple_NI = (list(first_dict)[7], first_dict['NI'])
    sorted_NI.insert(0, tuple_NI)
    sorted_NI = list(map(list, sorted_NI))


    bar_labels = list(results)
    bar_values = list(results.values())


    result_list = list(zip_longest(sorted_SE, sorted_SI, sorted_TE, sorted_TI, sorted_FE, sorted_FI, sorted_NE, sorted_NI, fillvalue=['0',0]))
    result_list = list(map(list, result_list)) # лист листов

    new_result_list = []
    for element in result_list:
        element = list(chain.from_iterable(element))
        new_result_list.append(element )


 

    log_request(text, new_result_list)
    return render_template('results.html', title='', max=max(bar_values), labels=bar_labels, values=bar_values,
                            # # the_results8=sorted_NI,
                            # the_results8=new_result_list,
                            table = new_result_list,
                            )



@application.route('/count_words', methods=['POST'])
def count() -> 'html':
    frequency = {}

    text = request.form['phrase']

    match_pattern = re.findall(r'\b[а-я]{3,15}\b', text)
    match_pattern = [word for word in match_pattern if word not in stopwords.words('russian')]

    for word in match_pattern:
        count = frequency.get(word,0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()
    dict_aspect = {}
    sorted_dict_aspect = {}

    for words in frequency_list:
        if frequency[words]>1:
            dict_aspect[words] = text.count(words)
            sorted_dict_aspect = sorted(dict_aspect.items(), key=operator.itemgetter(1), reverse=True)

    
    sorted_dict_aspect = list(map(list, sorted_dict_aspect))

    return render_template('results2.html', table=sorted_dict_aspect,
                        #    the_result=stopword,
                        #    the_result2=sorted_dict_aspect,
                           )


if __name__ == '__main__':
    # application.run(host='0.0.0.0')
    application.run(debug=True)
