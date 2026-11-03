# A node of the Huffman Tree
class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # Probability/frequency of symbol
        self.prob = prob
        # Symbol
        self.symbol = symbol
        # Left node
        self.left = left
        # Right node
        self.right = right
        # Tree direction (0/1)
        self.code = ''


""" A helper function to calculate the probabilities/frequencies of symbols in given data """
def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) is None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


""" A helper function to calculate the codes of symbols by traversing the tree """
def Calculate_Codes(node, val=''):
    # Huffman code for current node
    new_val = val + str(node.code)

    codes = {}
    if node.left:
        codes.update(Calculate_Codes(node.left, new_val))
    if node.right:
        codes.update(Calculate_Codes(node.right, new_val))

    if not node.left and not node.right:
        codes[node.symbol] = new_val

    return codes


""" A helper function to obtain the encoded output """
def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        print(coding[c], end='')
        encoding_output.append(coding[c])
    string = ''.join([str(item) for item in encoding_output])
    return string


""" A helper function to calculate the space difference between compressed and non-compressed data """
def Total_Gain(data, coding):
    before_compression = len(data) * 8  # Total bit space before compression (8 bits per char)
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol])  # Bits required after compression

    print("\nSpace usage before compression (in bits):", before_compression)
    print("Space usage after compression (in bits):", after_compression)


def Huffman_Encoding(data):
    symbol_with_probs = Calculate_Probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbols: ", symbols)
    print("probabilities: ", probabilities)

    nodes = []

    # Converting symbols and probabilities into Huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))

    # Build the tree using a greedy strategy
    while len(nodes) > 1:
        # Sort all nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)

        # Pick the 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        left.code = 0
        right.code = 1

        # Combine the 2 smallest nodes to create a new internal node
        newNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = Calculate_Codes(nodes[0])
    print("symbols with codes:", huffman_encoding)
    Total_Gain(data, huffman_encoding)
    print("Encoded output: ", end='')
    encoded_output = Output_Encoded(data, huffman_encoding)
    print()

    return encoded_output, nodes[0]


# Driver Code
if __name__ == '__main__':
    data = "AAAAAAABCCCCCCDDEEEEE"
    print(f"Original String: {data}\n")
    Huffman_Encoding(data)
