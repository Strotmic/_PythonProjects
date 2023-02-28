import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
text = "Natural language processing is an exciting area."
sent_tokenize(text)
word_tokenize(text)

worf_quote = "Sir, I protest. I am not a merry man!"
words_in_quote = word_tokenize(worf_quote)
words_in_quote

stop_words = set(stopwords.words("english"))
filtered_list = []

for word in words_in_quote:
   if word.casefold() not in stop_words:
        filtered_list.append(word)

filtered_list = [word for word in words_in_quote if word.casefold() not in stop_words]

print(filtered_list)

#stemming vanaf hier --------------------------------------------------------------------------------------------------------------------------------------------------------
string_for_stemming = """
... The crew of the USS Discovery discovered many discoveries.
... Discovering is what explorers do."""

words = word_tokenize(string_for_stemming)
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)


#Part of speech tagging vanaf hier ----------------------------------------------------------------------------------------------------------------------------------------------
sagan_quote = """If you wish to make an apple pie from scratch, you must first invent the universe."""
words_in_sagan_quote = word_tokenize(sagan_quote)

# #korte samenvatting van de afkortingen die gebruikt worden in de onderstaande methode
#nltk.help.upenn_tagset() 
test = nltk.pos_tag(words_in_sagan_quote)
print(test)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
jabberwocky_excerpt = """'Twas brillig, and the slithy toves did gyre and gimble in the wabe: all mimsy were the borogoves, and the mome raths outgrabe."""
words_in_excerpt = word_tokenize(jabberwocky_excerpt)
nltk.pos_tag(words_in_excerpt)

lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("scarves")
string_for_lemmatizing = "The friends of DeSoto love scarves."
words = word_tokenize(string_for_lemmatizing)
print(words)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print(lemmatized_words)

#Chunking -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(' --------------------------------------------------------')
lotr_quote = "It's a dangerous business, Frodo, going out your door."
words_in_lotr_quote = word_tokenize(lotr_quote)
print(words_in_lotr_quote)

lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
print(lotr_pos_tags)
grammar = "NP: {<DT>?<JJ>*<NN>}"

chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree.draw()