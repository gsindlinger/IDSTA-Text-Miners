import spacy
from spacy.lang.en.stop_words import STOP_WORDS


# removing stopwords
# removing punctuation
def remove_stopwords_and_punctuation(lyrics: str) -> str:
    nlp = spacy.load("de_core_news_sm", exclude="ner")
    word_list = ""
    for line in lyrics.split("\n"):
        for word_temp in nlp(str(line)):
            if word_temp.lemma_ not in STOP_WORDS and word_temp.has_vector:
                if not word_temp.is_punct:
                    # if word.text != '\n' and word.text != '\n\n'
                    # and word.text != '\n\n\n' and word.text != ',' and word.text !=:
                    word_list += word_temp.text + " "
        if line == "":
            continue
    return word_list


def lemmatize(lyrics: str) -> str:
    lemmatized_lyrics = ""
    nlp = spacy.load("de_core_news_sm", exclude=["parser", "ner", "tagger"])
    # noinspection DuplicatedCode
    for line in lyrics.split("\n"):
        for word_temp in nlp(str(line)):
            if word_temp.lemma_ not in STOP_WORDS and word_temp.has_vector:
                if not word_temp.is_punct:
                    lemmatized_lyrics += word_temp.lemma_ + " "
        if line == "":
            continue

    return lemmatized_lyrics.strip()


# remove trash words
def remove_trash_words(lyrics: str) -> str:
    trash_words = set(
        '''
    the oh uh ohh eh woah mi na ah ahh yeah mh seh mhm uh uhh mh ey 
    huh la na pah geh ha ey mal la ah it ne is your le les pas 
    dans que tu et ai qu ti po se mi ty nuk si ma te mu ik het 
    niet een ben maar op voor dat met la que vie el non ya mi 
    che lo est bu bi bir yok beni bana de hep yine gibi ain jag 
    det vi och som har kan de min om yeah hey huh okay mn mei ka 
    kom ke di pa edhe krejt unë që de un on suis mon pour moi en 
    qui elle ll bo jom për qe sa yo ni por ça tout sur mais une 
    fait fais mes il sen benim ama ve seni ki sana var
    '''.split())

    clean_song = ''
    for word in lyrics.split():
        if not word.lower() in trash_words:
            clean_song += word + " "
        else:
            print(word)
    return clean_song
