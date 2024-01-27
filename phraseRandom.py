import random
#import os
#import openai
#openai.api_key = "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"


english = ['house', 'sun', 'love', 'day', 'time', 'cat', 'mom', 'dog', 'girl', 'boy',
    'street', 'night', 'life', 'friend', 'child', 'door', 'eat', 'drink', 'sleep', 'go',
    'come', 'study', 'read', 'write', 'speak', 'listen', 'see', 'think', 'understand', 'know',
    'want', 'can', 'must', 'be', 'have', 'do', 'beautiful', 'good', 'nice', 'tall',
    'short', 'small', 'big', 'long', 'short', 'old', 'new', 'red', 'blue',
    'green', 'yellow', 'black', 'white', 'happy', 'sad', 'angry', 'tired', 'glad', 'interesting',
    'difficult', 'easy', 'fast', 'slow', 'hot', 'cold', 'open', 'closed', 'strong', 'weak',
    'right', 'wrong', 'ready', 'busy', 'free', 'play', 'run', 'jump', 'sing', 'dance',
    'watch', 'smile', 'laugh', 'cry', 'forget', 'remember', 'help', 'wait', 'start', 'finish',
    'cook', 'eat', 'drink', 'sleep', 'wake up', 'walk', 'travel', 'drive', 'book', 'ask',
    'answer', 'call', 'meet', 'think', 'dream', 'spy', 'discover', 'wish', 'advise', 'hope',
    'believe', 'studious', 'intelligent', 'shy', 'kind', 'brave', 'generous', 'friendly', 'funny', 'serious',
    'energetic', 'responsible', 'patient', 'curious', 'creative', 'organized', 'decisive', 'affectionate', 'charming', 'reliable',
    'hungry', 'thirsty', 'happy', 'sad', 'angry', 'tired', 'content', 'intense', 'calm', 'romantic',
    'fast', 'slow', 'hot', 'cold', 'simple', 'complicated', 'normal', 'strange', 'important', 'useless',
    'true', 'false', 'early', 'late', 'often', 'rarely', 'never', 'always', 'before', 'after',
    'today', 'tomorrow', 'yesterday', 'immediately', 'then', 'when', 'where', 'how', 'why', 'how much',
    'which', 'who', 'what', 'therefore', 'also', 'not', 'but', 'however', 'so', 'thus',
    'while', 'until', 'that is', 'except', 'or', 'in order to', 'because', 'although', 'nevertheless', 'indeed',
    'moreover', 'that is', 'thus', 'only', 'still', 'not even', 'just', 'barely', 'simply', 'completely',
    'enough', 'fortunately', 'sufficiently', 'sincerely', 'soon', 'currently', 'normally', 'rarely', 'truly', 'really', 'the day after tomorrow', 'previously']

Ukrainian = ['дім', 'сонце', 'любов', 'день', 'час', 'кіт', 'мама', 'собака', 'дівчина', 'хлопець',
    'вулиця', 'ніч', 'життя', 'друг', 'дитина', 'двері', 'їсти', 'пити', 'спати', 'йти',
    'приходити', 'вчитися', 'читати', 'писати', 'говорити', 'слухати', 'бачити', 'думати', 'розуміти', 'знати',
    'хотіти', 'могти', 'має', 'бути', 'робити', 'гарний', 'добрий', 'приємний', 'високий',
    'низький', 'малий', 'великий', 'довгий', 'короткий', 'старий', 'новий', 'червоний', 'синій',
    'зелений', 'жовтий', 'чорний', 'білий', 'щасливий', 'сумний', 'сердитий', 'втомлений', 'задоволений', 'цікавий',
    'складний', 'легкий', 'швидкий', 'повільний', 'гарячий', 'холодний', 'відкритий', 'закритий', 'сильний', 'слабкий',
    'правильний', 'неправильний', 'готовий', 'зайнятий', 'вільний', 'грати', 'бігти', 'стрибати', 'співати', 'танцювати',
    'дивитися', 'усміхатися', 'сміятися', 'плакати', 'забувати', "пам'ятати", 'допомагати', 'чекати', 'починати', 'закінчувати',
    'готувати', 'їсти', 'пити', 'спати', 'прокидатися', 'ходити', 'подорожувати', 'водити', 'бронювати', 'питати',
    'відповідати', 'телефонувати', 'зустрічатися', 'думати', 'мріяти', 'шпигувати', 'відкривати', 'бажати', 'надавати пораду', 'сподіватися',
    'вірити', 'студіозний', 'розумний', 'соромливий', 'добрий', 'хоробрий', 'щедрий', 'симпатичний', 'веселий', 'серйозний',
    'енергійний', 'відповідальний', 'терплячий', 'допитливий', 'творчий', 'організований', 'рішучий', 'лагідний', 'чарівний', 'надійний',
    'голодний', 'спраглий', 'щасливий', 'сумний', 'сердитий', 'втомлений', 'задоволений', 'інтенсивний', 'спокійний', 'романтичний',
    'швидкий', 'повільний', 'гарячий', 'холодний', 'простий', 'складний', 'звичайний', 'дивний', 'важливий', 'непотрібний',
    'правдивий', 'хибний', 'рано', 'пізно', 'часто', 'рідко', 'ніколи', 'завжди', 'до', 'після',
    'сьогодні', 'завтра', 'вчора', 'негайно', 'потім', 'коли', 'де', 'як', 'чому', 'скільки',
    'який', 'хто', 'що', 'отже', 'також', 'не', 'але', 'однак', 'тому', 'отже',
    'поки', 'доки', 'тобто', 'окрім', 'або', 'щоб', 'тому що', 'хоча', 'однак', 'справді',
    'крім того', 'тобто', 'отже', 'тільки', 'все ще', 'навіть', 'ледве', 'просто', 'зовсім', 'повністю',
    'достатньо', 'на щастя', 'достатньо', 'щиро', 'скоро', 'зараз', 'зазвичай', 'рідко', 'справді', 'справді', 'післязавтра', 'раніше']

Italian = ['casa', 'sole', 'amore', 'giorno', 'tempo', 'gatto', 'mamma', 'cane', 'ragazza', 'ragazzo',
    'strada', 'notte', 'vita', 'amico', 'bambino', 'porta', 'mangiare', 'bere', 'dormire', 'andare',
    'venire', 'studiare', 'leggere', 'scrivere', 'parlare', 'ascoltare', 'vedere', 'pensare', 'capire',
    'sapere', 'volere', 'potere', 'dovere', 'essere', 'avere', 'fare', 'bello', 'bravo', 'buono',
    'alto', 'basso', 'piccolo', 'grande', 'lungo', 'corto', 'vecchio', 'nuovo', 'rosso', 'blu',
    'verde', 'giallo', 'nero', 'bianco', 'felice', 'triste', 'arrabbiato', 'stanco', 'contento', 'interessante',
    'difficile', 'facile', 'veloce', 'lento', 'caldo', 'freddo', 'aperto', 'chiuso', 'forte', 'debole',
    'giusto', 'sbagliato', 'pronto', 'occupato', 'libero', 'giocare', 'correre', 'saltare', 'cantare', 'ballare',
    'guardare', 'sorridere', 'ridere', 'piangere', 'dimenticare', 'ricordare', 'aiutare', 'aspettare', 'iniziare', 'finire',
    'cucinare', 'mangiare', 'bere', 'dormire', 'svegliarsi', 'camminare', 'viaggiare', 'guidare', 'prenotare', 'chiedere',
    'rispondere', 'chiamare', 'incontrare', 'pensare', 'sognare', 'spiare', 'scoprire', 'desiderare', 'consigliare', 'sperare',
    'credere', 'studioso', 'intelligente', 'timido', 'gentile', 'coraggioso', 'generoso', 'simpatico', 'divertente', 'serio',
    'energico', 'responsabile', 'paziente', 'curioso', 'creativo', 'organizzato', 'deciso', 'affettuoso', 'affascinante', 'affidabile',
    'affamato', 'assetato', 'felice', 'triste', 'arrabbiato', 'stanco', 'contento', 'intenso', 'tranquillo', 'romantico',
    'veloce', 'lento', 'caldo', 'freddo', 'semplice', 'complicato', 'normale', 'strano', 'importante', 'inutile',
    'vero', 'falso', 'presto', 'tardi', 'spesso', 'raramente', 'mai', 'sempre', 'prima', 'dopo',
    'oggi', 'domani', 'ieri', 'subito', 'poi', 'quando', 'dove', 'come', 'perché', 'quanto',
    'quale', 'chi', 'cosa', 'dunque', 'anche', 'non', 'ma', 'però', 'quindi', 'così',
    'mentre', 'finché', 'cioè', 'eccetto', 'oppure', 'affinché', 'perché', 'sebbene', 'tuttavia', 'infatti',
    'anzi', 'cioè', 'dunque', 'ovvero', 'però', 'poi', 'quindi', 'solo', 'ancora', 'neanche',
    'appena', 'mai', 'già', 'sempre', 'neppure', 'semplicemente', 'completamente', 'abbastanza', 'fortunatamente', 'sufficientemente',
    'sinceramente', 'presto', 'attualmente', 'normalmente', 'raramente', 'veramente', 'davvero', 'proprio', 'dopodomani', 'precedentemente']

German = ['Haus', 'Sonne', 'Liebe', 'Tag', 'Zeit', 'Katze', 'Mutter', 'Hund', 'Mädchen', 'Junge',
    'Straße', 'Nacht', 'Leben', 'Freund', 'Kind', 'Tür', 'essen', 'trinken', 'schlafen', 'gehen',
    'kommen', 'lernen', 'lesen', 'schreiben', 'sprechen', 'hören', 'sehen', 'denken', 'verstehen', 'wissen',
    'wollen', 'können', 'müssen', 'sein', 'haben', 'tun', 'schön', 'gut', 'nett', 'groß',
    'klein', 'alt', 'neu', 'rot', 'blau', 'grün', 'gelb', 'schwarz', 'weiß', 'glücklich',
    'traurig', 'wütend', 'müde', 'zufrieden', 'interessant', 'schwierig', 'einfach', 'schnell', 'langsam',
    'heiß', 'kalt', 'offen', 'geschlossen', 'stark', 'schwach', 'richtig', 'falsch', 'bereit', 'beschäftigt',
    'frei', 'spielen', 'rennen', 'springen', 'singen', 'tanzen', 'schauen', 'lächeln', 'lachen', 'weinen',
    'vergessen', 'erinnern', 'helfen', 'warten', 'starten', 'beenden', 'kochen', 'essen', 'trinken', 'schlafen',
    'aufwachen', 'gehen', 'reisen', 'fahren', 'buchen', 'fragen', 'antworten', 'anrufen', 'treffen', 'denken',
    'träumen', 'spionieren', 'entdecken', 'wünschen', 'beraten', 'hoffen', 'glauben', 'studieren', 'intelligent', 'schüchtern',
    'freundlich', 'mutig', 'großzügig', 'nett', 'lustig', 'ernst', 'energisch', 'verantwortungsbewusst', 'geduldig', 'neugierig',
    'kreativ', 'organisiert', 'entschlossen', 'liebevoll', 'charmant', 'zuverlässig', 'hungrig', 'durstig', 'glücklich', 'traurig',
    'wütend', 'müde', 'zufrieden', 'intensiv', 'ruhig', 'romantisch', 'schnell', 'langsam', 'heiß', 'kalt',
    'einfach', 'kompliziert', 'normal', 'seltsam', 'wichtig', 'nutzlos', 'wahr', 'falsch', 'früh', 'spät',
    'oft', 'selten', 'nie', 'immer', 'vor', 'nach', 'heute', 'morgen', 'gestern', 'sofort',
    'dann', 'wenn', 'wo', 'wie', 'warum', 'wie viel', 'welcher', 'wer', 'was', 'also',
    'auch', 'nicht', 'aber', 'jedoch', 'also', 'während', 'bis', 'das heißt', 'außer', 'oder',
    'damit', 'weil', 'obwohl', 'dennoch', 'tatsächlich', 'auch', 'das heißt', 'also', 'nur', 'noch',
    'kaum', 'einfach', 'überhaupt', 'vollständig', 'genug', 'glücklicherweise', 'ausreichend', 'aufrichtig', 'bald', 'derzeit',
    'normalerweise', 'selten', 'wirklich', 'wirklich', 'übermorgen', 'zuvor']

text = []
def eng_text():
    for i in range(13):
        eng_sentence = (random.choice(english) + " ").lower()
        text.append(eng_sentence)
    sentence = "".join(text)
    return sentence 

def ukr_text():
    for i in range(13):
        ukr_sentence = (random.choice(Ukrainian) + " ").lower()
        text.append(ukr_sentence)
    sentence = "".join(text)
    return sentence 

def ital_text():
    for i in range(13):
        ital_sentence = (random.choice(Italian) + " ").lower()
        text.append(ital_sentence)
    sentence = "".join(text)
    return sentence 

def ger_text():
    for i in range(13):
        ger_sentence = (random.choice(German) + " ").lower()
        text.append(ger_sentence)
    sentence = "".join(text)
    return sentence 






#openai.api_key = os.getenv("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")

#response = openai.Completion.create(
  #model="text-davinci-003",
  #prompt="write a random english phrase, 10 words long",
  #temperature=1,
  #max_tokens=256,
  #top_p=1,
  #frequency_penalty=0,
  #presence_penalty=0
#)