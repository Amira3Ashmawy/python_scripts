import datetime
import hashlib
import json 

class Block:
    block_indx = 0 
    transactions = None
    nonce = 0
    previous_hash = 0x0
    timestamp = str(datetime.datetime.now())

    def __init__(self,transactions):
        self.transactions = transactions
        self.timestamp = str(datetime.datetime.now())
    
    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.transactions).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.block_indx).encode('utf-8')
        )
        return h.hexdigest()
    # def __str__(self):
    #     #print out the value of a block
    #     return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.block_indx) + "\nBlock\
    #     Data: " + str(self.transactions) + "\nHashes: " + str(self.nonce) + "\ntime  \
    #     Stamp" + str(self.timestamp)+"\n--------------"
        
class Blockchain:
    diff = 20
    max_nonce = 2**32
    transactions = "Genesis"
    block = Block(transactions)
    chain = [block]
    target = 2 ** (256-diff)

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.block_indx = self.block.block_indx+1
        self.chain.append(block)
    
    def mine(self,block):
        for n in range(self.max_nonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                # print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

#mine 10 blocks
blockchain.mine(Block({'TransactionIndex': '0', 
                            'SenderAddress': '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9',
                            'RecipientAddress': '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', 
                            'Amount': 0.8040153822020336, 
                            'Message': 'testmessage'}))
    
#print out each block in the blockchain
    # print(blockchain.head)

# js = json.dumps(blockchain.head.__dict__, sort_keys=True)
# dic = []
  
#     dic.append({'BlockIndex':blockchain.head.block_indx,
#         'TimeStamp':blockchain.head.timestamp,
#         'Nonce': blockchain.head.nonce,
#         'PreviouseHash': blockchain.head.previous_hash,
#         'Transactions': blockchain.head.transactions})  
#     print(dic)
#     if blockchain.head.next():
#         blockchain.head = blockchain.head.next
    # for block in blockchain.chain:
    #     print(block.__dict__)
with open('result.json', 'w') as fp:
    for block in blockchain.chain:  
        dic = block.__dict__
        json.dump(dic, fp)