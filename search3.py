import os

# os.listdir

search_word = input("Enter a search word: ")


class SearchOS:
    def __init__(self):
        self.filedir = []

    def dir_search(self):
        self.filedir = []
        for dirpath, dirnames, files in os.walk(
                '/Users/willi/PycharmProjects/iot22_algorithms_datastructures/Assignments/Assignment 3/'):
            for file in files:
                self.filedir.append(os.path.join(dirpath, file))

        print(self.filedir)
        s.search_for_word()

    def search_for_word(self, ind=0):
        """Loop through a file and search for the word"""
        if ind >= len(self.filedir):
            return
        with open(self.filedir[ind], encoding='utf-8') as f:
            content = f.read()

            if search_word in content:
                print(search_word, "exists in ", self.filedir[ind])
            else:
                print(search_word, "does not exist in ", self.filedir[ind])
            return s.search_for_word(ind + 1)


if __name__ == '__main__':
    s = SearchOS()
    s.dir_search()
