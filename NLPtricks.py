import nltk
from nltk.tokenize import wordpunct_tokenize
import re

class TextProcess: 
    def __init__(data):
        pass

    def ReadLoveLetters():
      LoveLetters = []
      for i in range(0,88):
        with open('loveletters/'+ str(i) + '.txt') as f:
          LetterLines = f.readlines()
          Letter = ''
          for i in range(len(LetterLines)):
            Letter = Letter + LetterLines[i]
          LoveLetters.append(Letter)
      return LoveLetters
    
    def ReadStopWords():
      with open('stopwords.txt') as f:
        StopWords = f.read().splitlines()
      return StopWords
    
    def remove_regex(data, regex_pattern):
        """
        remove um dado padrão regex
        """

        import re
        ls = []
        words = ''
        
        for line in data:
            matches = re.finditer(regex_pattern, line)
            
            for m in matches: 
                line = re.sub(m.group().strip(), '', line)

            ls.append(line)

        return ls

    def tokenize_text(data):
        """
        tokeniza
        """
        ls = []

        for line in data:
            tokens = wordpunct_tokenize(line)
            ls.append(tokens)

        return ls

    def apply_standardization(tokens, std_list):
        """
        padroniza

        exemplo de std_list : std_list = {'eh': 'é', 'vc': 'você' ... etc}
        """
        ls = []

        for tk_line in tokens:
            new_tokens = []
            
            for word in tk_line:
                if word.lower() in std_list:
                    word = std_list[word.lower()]
                    
                new_tokens.append(word) 
                
            ls.append(new_tokens)

        return ls

    def remove_stopwords(tokens, stopword_list):
        """
        remove palavras de passagem
        """
        ls = []

        marks = ["'", "“","'","!","(",")","-","[","]","{","}",";","?","@","#","$","%",":","'",'"',"\\",",",".","/","^","&","*","_","—","–","’","…"]

        for tk_line in tokens:
            new_tokens = []
            
            for word in tk_line:
                if word.lower() not in stopword_list:
                  if word.lower() not in marks:
                    new_tokens.append(word) 
            ls.append(new_tokens)
            
        return ls

    def apply_stemmer(tokens):
        """
        Aplica o stemmer aos tokes
        """ 
        ls = []
        stemmer = nltk.stem.RSLPStemmer()

        for tk_line in tokens:
            new_tokens = []
            
            for word in tk_line:
                word = str(stemmer.stem(word))
                new_tokens.append(word) 
                
            ls.append(new_tokens)
            
        return ls

    def untokenize_text(tokens):
        """
        destokeniza
        """
        ls = []

        for tk_line in tokens:
            new_line = ''
            
            for word in tk_line:
                new_line += word + ' '
                
            ls.append(new_line)
            
        return ls

    def get_text_cloud(tokens):
        """
        faz a nuvem
        """
        text = ''

        for tk_line in tokens:
            new_tokens = []
            
            for word in tk_line:
                text += word + ' '
            
        return text

    def get_freq_dist_list(tokens):
        """
        fprepara os tokens para obter a lista de frequencia das palavras usando FreqDist
        from nltk.probability import FreqDist (nao curto muito essa abordagem aqui)
        """
        ls = []

        for tk_line in tokens:
            for word in tk_line:
                ls.append(word)

        return ls

  #  def get_accuracy(matrix):
  #      acc = 0
  #      n = 0
  #      total = 0
        
  #      for i in range(0, len(matrix)):
  #          for j in range(0, len(matrix)):
  #              if(i == j): 
  #                  n += matrix[i,j]
                
  #              total += matrix[i,j]
                
  #      acc = n / total
  #      return acc

