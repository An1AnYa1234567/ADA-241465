''' write a program to build a Huf fmanCoder class with build_tree(frequencies: Dict[str, int]) -> Node and
generate_codes() -> Dict[str, str] methods accepting character frequencies and returning
binary encoding mappings.'''

# Huffman Coding
import heapq
# Node class
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    # Compare nodes according to frequency
    def __lt__(self, other):
        return self.freq < other.freq
# Huffman Coding class
class Huffman:
    def __init__(self):
        self.root = None
    # Build Huffman Tree
    def build_tree(self, frequencies):
        heap = []

        for char, freq in frequencies.items():
            node = Node(char, freq)
            heapq.heappush(heap, (freq, char, node))

        while len(heap) > 1:
            freq1, char1, left = heapq.heappop(heap)
            freq2, char2, right = heapq.heappop(heap)

            new_node = Node(None, freq1 + freq2)

            new_node.left = left
            new_node.right = right

            heapq.heappush(
                heap,
                (new_node.freq, min(char1, char2), new_node)
            )

        self.root = heap[0][2]
    # Generate Huffman Codes
    def generate_codes(self):
        codes = {}

        def traverse(node, code):
            if node is None:
                return

            # Leaf node
            if node.char is not None:
                codes[node.char] = code if code else "0"
                return

            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(self.root, "")

        return codes
# Main Program
frequencies = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}
h = Huffman()
h.build_tree(frequencies)
codes = h.generate_codes()
print("Huffman Codes:")
for char, code in sorted(codes.items()):
    print(char, ":", code)
