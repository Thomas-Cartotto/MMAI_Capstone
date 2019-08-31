import re
import unidecode
from textblob import TextBlob

class cannjoin_nlp:

    def __init__(self):
        print('Created')
    # Here were going to add the preprocessing functions that gave best results

    def remove_html_tags(self, sentence):
        return re.sub(re.compile('<.*?>'), '', str(sentence))

    def remove_URLS(self, sentence):
        return re.sub(re.compile('http\S+|www\.\S+'), '', str(sentence))

    def remove_breaks(self, sentence):
        return re.sub(re.compile('\n|\r|\t'), '', str(sentence))

    def remove_unicode(self, sentence):
        return unidecode.unidecode(str(sentence))

    def remove_numbers(self, sentence):
        return re.sub(re.compile('\d+'), '', str(sentence))

    def lower_case(self, sentence):
        return str(sentence).lower()

    def remove_punctuation(self, sentence):
        return re.sub(re.compile('[^\w\s]'), '', str(sentence))

    # Put it all together (Order is important)
    def apply_basic_cleaning(self, sentence):
        iteration_one = self.remove_html_tags(sentence)
        iteration_two = self.remove_URLS(iteration_one)
        iteration_three = self.remove_breaks(iteration_two)
        iteration_four = self.remove_numbers(iteration_three)
        iteration_five = self.lower_case(iteration_four)
        
        return self.remove_punctuation(iteration_five)

    def getNLPFeatures(self, raw_comment):

        clean_comment = self.apply_basic_cleaning(raw_comment)
    
        sentiment = TextBlob(clean_comment).sentiment
    
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity
    
        data = {
            "polarity": polarity,
            "subjectivity": subjectivity,
            "raw_comment": raw_comment,
            "clean_comment": clean_comment
        }
    
        return data



