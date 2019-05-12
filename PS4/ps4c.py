
import string
import os

os.chdir('PS4')
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):

    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):

        return self.message_text

    def get_valid_words(self):

        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):

        dict = {}
        punc = list(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        for i, let in enumerate(vowels_permutation.lower()):
            dict[VOWELS_LOWER[i]] = let
        for i, let in enumerate(vowels_permutation.upper()):
            dict[VOWELS_UPPER[i]]= let
        for let in CONSONANTS_LOWER:
            dict[let] = let
        for let in CONSONANTS_UPPER:
            dict[let] = let
        for pun in punc:
            dict[pun]=pun
        return dict

    
    def apply_transpose(self, transpose_dict):
  
        encrypted = []
        for let in self.message_text:
            encrypted.append(transpose_dict[let])
        return ''.join(encrypted)


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
   
        SubMessage.__init__(self,text)

    def decrypt_message(self):
     
        transpose_dict_list = []
        message_list = []
        perm_list = get_permutations('aeiou')
        
        for perm in perm_list:
            transpose_dict_list.append(self.build_transpose_dict(perm))
        for dic in transpose_dict_list:
            testmessage=self.apply_transpose(dic)
            message_list.append(testmessage)

        localtest = []
        globaltest = []
        word_list = self.get_valid_words()

        for mes in message_list:
            words = mes.split()
            for word in words:
                if is_word(word_list,word):
                    localtest.append(1)
                else:
                    localtest.append(0)
            globaltest.append([sum(localtest),mes])    
            del localtest[0:len(localtest)]    
        best = max(globaltest)
        answer = best[1:2]
        return answer


    

if __name__ == '__main__':


    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
 
