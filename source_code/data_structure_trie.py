class Node:
    # A node that consists of a trie
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

    def __str__(self):
        return f"self.key : {self.key} \nself.data : {self.data} \n" \
               f"self.children : {self.children}\n\n"


class Trie:
    # whenever generating object
    def __init__(self):
        self.head = Node(None)

    # insert string in trie
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)


            # insert key in this code
            curr_node = curr_node.children[char]

            # if it is end of string,
            # store the entire string you want to save in the data field of the node

        curr_node.data = string

    def search(self, string):
        curr_node = self.head
        print(curr_node.children["J"].children["o"])
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]

            else:
                return False

        # string의 마지막 글자에 다달았을 때,
        # curr_node 에 data 가 있다면 string이 트라이에 존재하는 것!
        if curr_node.data is not None:
            return True

    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None

        queue = list(subtrie.children.values())
        while queue:
            curr = queue.pop()
            if curr.data is not None:
                result.append(curr.data)

            queue += list(curr.children.values())
        return result



trie_test = Trie()
names = ['Joe', 'John', 'Johnny', 'Jane', 'Jack', "Bill", "Carry"]

trie_test.insert(names[0])
trie_test.insert(names[1])
trie_test.insert(names[5])
print(trie_test.search('Joe'))
trie_test.starts_with('Jo')