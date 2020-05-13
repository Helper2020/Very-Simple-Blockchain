import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash=0):
        self.timestamp = timestamp
        if data == '' or data is None:
            raise ValueError()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next_block = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def get_time(self):
        """
        Returns: datetime object
        """
        return self.timestamp

    def set_next_block(self, block):
        self.next_block = block

    def get_next_block(self):
        return self.next_block

    def __str__(self):
        return f'Hash: {self.hash}, Date: {self.timestamp}'


class BlockChain():
    """
    A block chain implemented as link list
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.time_created = datetime.now()

    def add_block(self, data):
        timestamp = datetime.now()
        # First block in the chain
        if self.head is None:
            new_block = Block(timestamp, data)
            self.head = new_block
            self.tail = new_block
            return

        # setting the new block as a tail and setting the old tail to point to
        # new block.
        prev_hash = self.tail.get_hash()
        new_block = Block(timestamp, data, prev_hash)
        self.tail.set_next_block(new_block)
        self.tail = new_block

    def search_chain(self, block_hash):
        curr_block = self.head

        while curr_block:
            if curr_block.get_hash() == block_hash:
                return curr_block

            curr_block = curr_block.get_next_block()

    def print_chain(self):
        curr_node = self.head

        while curr_node:
            print(curr_node)
            curr_node = curr_node.get_next_block()


chain1 = BlockChain()
chain1.add_block(5645)
chain1.add_block(5635)
chain1.add_block(3442)

print('------------------ Test Case 1 ------------------')
# Make sure the link is properly built
chain1.print_chain()
# Should print three blocks

print('------------------ Test Case 2 ------------------')
chain2 = BlockChain()
chain2.add_block(9645)
chain2.add_block(5445)
chain2.add_block(5645)
chain2.add_block(5635)
chain2.add_block(3442)

block = chain2.search_chain('82bd3b63e2f8767c07670f6dd062aa27d01fd09819cfcfbea5f5b8c4c27323b0')
print(block)
# Should find then print the above block

print('------------------ Test Case 3 ------------------')
# Value of None is passed
# chain.add_block(None)
# Should raise a ValueError

print('------------------ Test Case 4 ------------------')
# Invalid data is passed to the chain, empty
# chain.add_block('')
# Raise a ValueError
