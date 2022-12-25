def type_aspect(aspect_words, text):
    aspect_dict = {}

    for word in aspect_words:
        if word in text:
            aspect_dict.setdefault(word, 0)
            aspect_dict[word] += 1
    
    print (aspect_dict)
    return aspect_dict

if __name__ == "__main__":

    #Список слов-аспектов

    # Власть, влияние, ресурсы
    se = 'alert, area, artillery, bullet, countr, hunt, power, shot, survive, war, автомат, агресс, арми, артиллер, баланс, башн, бдительност, безопасност, блок, богат, бив, бирж, битв, бить, боев, бой, бомб, бороть, борьб, бунт, бьёт, бюдж, взорв, взрыв, власт, влиян, вместе, воев, военн, воин, войн, войск, враг, врат, гвард, государ, границ, грохн, давлен, давят, денег, деньг, денеж, демократ, держав, доминир, доспех, драк, драл, дроб, завоеван, замок, заряд, захват, захвач, зацепил, играет, изгн, импер, капитал, катастроф, команд, контрол, конфликт, крепост, кризис, кулак, кусат, легион, меч, митинг, мишен, монарх, мятеж, напад, напал, напряж, насил, наступлен, нож, оккупиров, опасе, опасн, операц, ополч, оруж, отваг, отряд, офицер, палк, парламент, переворот, побед, поверг, поверж, пожирател, позиции, покуш, полит, полиц, полк, порез, правитель, приказ, пробив, пробил, проигра, промах, проруб, пространств, против, прочност, прутик, пул, ракет, разрук, разруш, реза, репресс, ресурс, рушит, рушив, силов, силы, сильнее, смерт, солдат, соперн, сопротивлен, столкновен, стратег, стрел, стычк, суверен, суд, схват, танк, терз, территор, тоталитар, тыкат, убив, убий, убил , убь, угроз, угрож, удар, уничт, управлен, урон, хищн, хран, цивилизац, чуж, штурм, щит'
    se = se.split(', ')

    # Субъективное восприятие органами чувтв
    si = 'body, feel, muscle, nerve, nervous, organ, perception, perceive, receptor, sensation, sensory, sensing, skin, smell, spine, spinal, stomach, taste, touch, боли, вдох, видеть, витамин, вкус, влажн, вода, водой, воду, воды, воздух, выдох, выполнен, гимнастик, гормон, грыжа, грыжи, движени, дыхание, жарк, желудка, желудок, заболеван, заняти, запах, здоров, зрение, зрения, иммун, йога, кашель, кисл, кишечн, клетка, клетки, кожа, кожи, колен, конечност, кост, красив, кровообращени, крови, кровь, лежа, лекарств, лечебн, лечен, массаж, матрас, медик, медицин, море, мышечн, мышц, нерв, ногами, ноги, нюх, организм,  орган, остеохондроз, отдых, ощущен, пахн, печени, печень, питан, пить, плеч, позвоночник, почки, почувствовать, препарат, прохладн, процедур, пить, пью, рецептор, самочувств, сауна, сауны, свет, свеж, симптом, слаб, слух, сосуд, спать, спина, спине, спины, стопа, стопу, сустав, сустав, таблетк, тела, теле, тело, тепл, тёпл, ткан, ткани, травм, тренажер, трогат, туловищ, упражнен, усталост, ухо, уют, физически, физкультур, фитнес, холод, чувствуешь'
    si = si.split(', ')

    # Продуктивность, техническое мышление
    te = 'circuit, machine, technology, tool, акци, аналит, бесплатн, бизнес, блок, валют, вихр, выручк, гаджет, дела, дело, движок, двигател, детал, дешевле, деятел, документ, долг, доллар, дороже, доход, заплат, заработат, инвест, индекс, инженер, инструкт, инструмент, интернет, ипотек, комисс, компьютер, компан, конструкт, контракт, крепл, купит, купил, кэш, материал, машин, меньше, механизм, миллион, миллиард,  накладн, оборот, оптимизац, отчет, опыт, оценк, плат, показат,  покуп, полезн, польз, порядок, потребит, прибор, прибыл, продукт, программ, прода, продук, производ, профит, процент, процесс, работ, рабоч, рентабел, регистр, робот, рынок, рыноч, рубл, сделк, сделок, скидк, способ, станок, страховк, строит, стоим, телефон, техник, технолог, торг, транзит, тысяч, услуг, финанс, фонд, халяв, цена, цене, цифр, экономик, эффект'
    te = te.split(', ')

    # Структурное мышление
    ti = 'абсолют, алгоритм, блок, бытие, вектор, гипот, дискретн, дифференц, единиц, закон, императив, категор, класс, конструкт, конструкц, контур, концепц, кристалл, критер, лексик, лини, макро, массив, масштаб, материи, материя, матриц, мерн, метафизи, метод,  модел, модул, набор, накоп, наук, объект, онтолог, определен, относительн, оценк, парадигм, параметр, паттерн, перспектив, поле, поряд, последовательност, предел, признак, призм, проекц, процесс, рамк, ранг, связ, семант, синтаксис, систем, спектр, спирал, сторон, структур, субстанц, субстрат, субъект, сущност, сфер, схем, теолог, теор, точка, точки, уров, фаза, фазо, фазы, фактор, форм, фрагмент, функц, центр, цепоч, цикл, частиц, шкал, хаос, эквивалент, элемент, эмпири, ядр'
    ti = ti.split(', ')

    # Восприятие эмоций человека (животных)
    fe = 'gaze, аха, атмосфер, весел, взгляд, видел, вопль, глаз, гнев, горд, горе, громко, груст, интонац, лицо, жалобно, жалост, завист, задумал, злост, испуг, крик, крич, любил, мил, молч, мрач, напряжен, обид, обиж, отвечал, плак, плач, покой, презрени, радует, раздраж, реагир, реакц, ржач, ржем, ржу, рыдат, сердит, серж, слез, скучн, скушн, смех, смеев, смеш, смеют, смея, смотрел, смотрет, страд, страх, стыд, тоск, угарат, угрюм, удивл, удивил, улыб, ужас, хмур, человечеств, шутк, шутн, эмоци'
    fe = fe.split(', ')

    # Описание родственных связей
    fi = 'бабушк, батя, брак, брат, близост, близк, девоч, девич, девушк, дед, детей, дети, дитя, детк, детсв, детск, детстве, довери, дорогая, дорогой, дочь, друж, друз, душевн, душу, душа, дядюшк, дядя, жена, жену, женил, женит, пожалуйста, жалет, жалей, жены, жена, женит, женою, зло, котен, кошек, кошк, кума, любв, любим, любл, любовь, любопытство, мальчик, мальчиш, мама, мамой, маму, матерь, мать, молча, морал, муж, невест, нравственн, отец, отношений, отношения, отца, отцом, папа, папой, папу, парен, парни, племянн, плох, пожалуйста, подруж, ребёнк, ребёнок, ребенк, ребенок, ребят, родител, родн, семей, семье, семьи, семью, семья, сестр, собак, ссора, ссоре, супруг, сын, тетя, тетушк, честн, ухажив, щенок, щенка'
    fi = fi.split(', ')

    # Новшества, проницательность, скрытый смысл, знак
    ne = 'conscious, dream, mind, insight, intention, imagination, realize, ассоциат, ассоциаци, божеств, бытие, бытия, вселенн, вариант, возможност, загадк, знак, значен, значит, идеи, идей, идею, идея, истин, ключ, легенд, маги, метафор, миф, мысли, мысль, образ, открыти, понимал, притч, разум, религ, рефлекси, ритуал, сакрал, символ, сказк, скрыт, смысл, снам, снах, сне, снов, сном, снится, сознав, сознан, сознат, сознай, сон, суть, сущност, фантаз, фольклор, явлен'
    ne = ne.split(', ')

    # Категория времени
    ni = 'hour, minute, year, аврал, бежит, быстр, вечер, врем, движен, движет, день, дне, дни, дня, динамик, мгновен, ждал, ждать, жду, завтр, задерж, затем, зрелост, кончится, коротк, мгнов, медленн, месяц, миг, минут, момент, недел, ночь, перемен, пора, план, поздн, поколен, поток, прогноз, пройдёт, прорицат, прошл, процесс, развити, рано, спеш, сразу, срок, срок, сроч, скор, темпы, тенденц,  торопит, торопливо, утро, час, фаза, цикл, эпоха, эпохи, юност'
    ni = ni.split(', ')


    text = input("Введите текст: ")
    text = text.lower()
    text = text.rstrip()

    #Создаём словари для каждого аспекта
    SE_dict = type_aspect(se, text)
    SI_dict = type_aspect(si, text)
    TE_dict = type_aspect(te, text)
    TI_dict = type_aspect(ti, text)
    FE_dict = type_aspect(fe, text)
    FI_dict = type_aspect(fi, text)
    NE_dict = type_aspect(ne, text)
    SE_dict = type_aspect(ni, text)