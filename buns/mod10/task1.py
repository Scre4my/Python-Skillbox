import nltk
from nltk.stem import SnowballStemmer
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem.wordnet import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
tokenizer = nltk.RegexpTokenizer(r"\w+")
stemmer = SnowballStemmer("english")


# Стемминг
def stem_texts(texts):
    preprocessed = []
    for i in texts:
        tokenized_words = tokenizer.tokenize(i) # токенизизуем каждый отзыв
        temp=[]
        for j in tokenized_words:
            if not j in stop_words:
                stemmed_word = stemmer.stem(j) # проходим стемером по каждому токену
                temp.append(stemmed_word)
        preprocessed.append(temp) # записываем в общий список токены после стеминга
    return preprocessed

def lem_texts(list_of_texts, return_tokens=True):
    processed = []
    for doc in tqdm(list_of_texts):
        lower = doc.lower().replace('\n', ' ')

        extra_chars = [',', '.', ':', ';', '(', ')', '[', ']', '/', ';', '!' '- ', '& ', '�', '‘', '’', '“', '”', '´',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                       '*', '±', '%', '>', '<', '\n', '|', '^', '=', ' – ', '_',
                       '\xa0', '\\', '↓', '↑', '•', ' l ', '@', '  ', '  ', '\u2009', '×']

        for char in extra_chars:
            lower = lower.replace(char, ' ')

        lower = lower.replace('  ', ' ')
        lower = lower.replace('  ', ' ')
        lower = lower.replace('  ', ' ')
        lower = lower.replace('  ', ' ')


        processed.append(lower)

    # tokinezation and lemmatization
    clean_tokens = []
    for text in tqdm(processed):
        words = word_tokenize(text)
        words = pos_tag(words)
        len(words)

        def get_wordnet_pos(tag):
            if tag == 'J':
                return wordnet.ADJ
            elif tag == 'V':
                return wordnet.VERB
            elif tag == 'R':
                return wordnet.ADV
            else:
                return wordnet.NOUN

        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(tag[0])) for word, tag in words]
        clean = [word for word in lemmatized_words if word not in stop_words and len(word)>=1]
        clean_tokens.append(clean)

    if return_tokens == True:
        return clean_tokens
    else:
        return [' '.join(i) for i in clean_tokens]



#preprocessed = stem_texts(df.reviewText)
preprocessed = lem_texts(df.reviewText)
print(len(preprocessed))