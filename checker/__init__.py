class Checker:
    def __init__(self):
        self.words = open("/Users/varunthvar1/PycharmProjects/Illegal_Word_Checker/checker/words.txt",
                          'rt').read().lower().split('\n')
        self.words2 = open("/Users/varunthvar1/PycharmProjects/Illegal_Word_Checker/checker/morewords.txt",
                           'rt').read().lower().split('\n')
        self.index = list()

    def check_word_in_file(self, file):
        file = open(file).read().lower().split(' ')
        for word in self.words:
            for item in file:
                if item.startswith(word) or item == word:
                    self.index.append(word)

    def check_phrase_in_file(self, file):
        file1 = open(file).read().lower()
        print(file)
        for word in self.words2:
            if word in file1:
                self.index.append(word)

    def print_words(self):
        self.index = sorted(set(self.index))
        print("Words found:")
        for key in self.index:
            print(f"{key}")

    def check(self, file):
        self.check_word_in_file(file)
        self.check_phrase_in_file(file)
        self.print_words()
