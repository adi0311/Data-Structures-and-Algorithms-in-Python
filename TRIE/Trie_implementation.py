class Trie:
    class Node:
        def __init__(self):
            self.children = dict()
            self.end = False

    def __init__(self):
        self.root = self.new_node()
        self.chars = set()

    def new_node(self):
        return self.Node()

    def insert(self, word):
        r = self.root
        for i in range(len(word)):
            t = word[i]
            if word[i] not in r.children.keys():
                r.children[t] = self.new_node()
            r = r.children[t]
            self.chars.add(t)
        r.end = True

    def search(self, word):
        r = self.root
        for i in range(len(word)):
            t = word[i]
            if t not in r.children.keys():
                return False
            r = r.children[t]
            if i == len(word)-1:
                if r.end:
                    return True
        return False

    def display_content(self, r, string, length):
        if r.end:
            cnt = 0
            for i in string.values():
                print(i, end="")
                cnt += 1
                if cnt >= length:   #dictionary might contain some extra characters. We need only first "length" characters.
                    break
            print()
        for i in self.chars:
            if i in r.children.keys():
                string[length] = i
                self.display_content(r.children[i], string, length+1)


T = Trie()
T.insert("ADITYA")
T.insert("ADAM")
T.insert("HELLO")
T.insert("INDIA")
T.insert("EXAMPLE")
T.insert("This is a sentence")
print("-------------------SEARCHING--------------------------------------")
print(T.search("ADAM"))
print(T.search("ADI"))
print(T.search("This is"))
print("------------------DISPLAYING THE CONTENT OF TRIE------------------")
T.display_content(T.root, dict(), 0)