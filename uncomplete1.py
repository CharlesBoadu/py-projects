class Wordplay:

    def __init__(self, words):
        self.words = []
        for i in range(5):
            words = input("Enter the words: ")
            self.words.append(words)

    def words_with_length(self, length):
        length_list = []
        for word in self.words:
            if len(word) == length:
                length_list.append(word)
        print(length_list)


    def starts_with(self, s):
        starts_with_list = []
        for word in self.words:
            if word[:1] == s:
                starts_with_list.append(word)
        print(starts_with_list)

        
    def ends_with(self, s):
        ends_with_list = []
        for word in self.words:
            if word[-1:] == s:
                ends_with_list.append(word)
        print(ends_with_list)
        
    def palindromes(self):
        palindromes_list = []
        for word in self.words:
             if word[:] == word[::-1]:
                 palindromes_list.append(word)
        print(palindromes_list)
        
    def only(self, L):
        for word in self.words:
            for char in word:
                if char not in L:
                    break
                    
            else:
                print(word)

    def avoids(self, L):
        for word in self.words:
            for char in word:
                if char in L:
                    break
            else:
                print(word)


play = Wordplay('words')
print("Words that starts with c are:")
play.starts_with('c')
print("words of length 5 are:")
play.words_with_length(5)
print("Words that ends with n are:")
play.ends_with('n')
print("A list of palindromes are:")
play.palindromes()
print("Words with only 'aeiou' are:")
play.only('aeiou')
print("Words with none of the letters in 'aeiou' are:")
play.avoids('aeiou')
