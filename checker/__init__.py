class Checker:
    def __init__(self):
        self.words = open("/Users/varunthvar1/PycharmProjects/Illegal_Word_Checker/checker/words.txt",
                          'rt').read().lower().split('\n')
        self.words2 = open("/Users/varunthvar1/PycharmProjects/Illegal_Word_Checker/checker/morewords.txt",
                           'rt').read().lower().split('\n')
        self.index = list()

    def checkfile(self, file):
        file = open(file).read().lower().split(' ')
        for word in self.words:
            for item in file:
                if item.startswith(word):
                    self.index.append(word)

    def checkfile2(self, file):
        file1 = open(file).read().lower()
        print(file)
        for word in self.words2:
            if word in file1:
                self.index.append(word)

    def print_words(self):
        print("Words found:")
        for key in sorted(set(self.index)):
            print(f"{key}")

    def check(self, file):
        self.checkfile(file)
        self.checkfile2(file)
        self.print_words()
