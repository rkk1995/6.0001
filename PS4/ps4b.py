
import string
import os

os.chdir('PS4')
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

def get_story_string():

    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):

        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
    
        return self.message_text

    def get_valid_words(self):

        return self.valid_words

    def build_shift_dict(self, shift):
      
        import string
        lowercase = string.ascii_lowercase*2
        uppercase = string.ascii_uppercase*2
        punc = list(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        dict = {}
        for i, let in enumerate(lowercase[0:26]):
            dict[let] = lowercase[i+shift]
        for i, let in enumerate(uppercase[0:26]):
            dict[let]= uppercase[i+shift]
        for pun in punc:
            dict[pun] = pun
        return dict


    def apply_shift(self, shift):
  
        dict = self.build_shift_dict(shift)
        shifted_message = []
        for let in self.message_text:
            shifted_message.append(dict[let])
        return ''.join(shifted_message)

class PlaintextMessage(Message):
    def __init__(self, text, shift):

        Message.__init__(self,text)
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        self.shift = shift

    def get_shift(self):

        return self.shift
    def get_encryption_dict(self):

        return self.encryption_dict

    def get_message_text_encrypted(self):

        return self.message_text_encrypted
    def change_shift(self, shift):

        self.encryption_dict=self.build_shift_dict(shift)
        self.message_text_encrypted= self.apply_shift(shift)
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        
        Message.__init__(self,text)

    def decrypt_message(self):
        
        word_list = self.get_valid_words()
        localtest = []
        globaltest = []
        for s in range(26):
            text = self.apply_shift(s)
            words = text.split()
            for word in words:
                if is_word(word_list,word):
                    localtest.append(1)
                else:
                    localtest.append(0)
            globaltest.append([sum(localtest),s,text])
            del localtest[0:len(localtest)]
        best_shift = max(globaltest)
        answer = best_shift[1:3]
        return answer

if __name__ == '__main__':
    plaintext = PlaintextMessage('hairy balls', 1)
    print('Expected Output: ibjsz cbmmt')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    story = get_story_string()
    ciphertext = CiphertextMessage(story)
    print('Unencypted story:', ciphertext.decrypt_message())
