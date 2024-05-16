import hashlib

class NeuralCoinBlock:

    def __init__(self,previous_block_hash,transaction_list):
        self.previous_block_hash=previous_block_hash
        self.transaction_list=transaction_list
        self.block_data='-'.join(transaction_list)+'-'+previous_block_hash
        self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()

t1="Adi sends 2.0 NC to Pappi"
t2="Pappi sends 2.2 NC to Gani"
t3="Gani sends 2.8 NC to Siddhu"
t4="Siddhu sends 3.0 NC to Gani"
t5="Gani sends 4.2 NC to Pappi"
t6="Pappi sends 2.5 NC to Adi"

initial_block=NeuralCoinBlock("Block Hash",[t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block=NeuralCoinBlock("initial_block.block_hash",[t3,t4])

print("\n"+second_block.block_data)
print(second_block.block_hash)

third_block=NeuralCoinBlock("second_block.block_hash",[t5,t6])

print("\n"+third_block.block_data)
print(third_block.block_hash)
