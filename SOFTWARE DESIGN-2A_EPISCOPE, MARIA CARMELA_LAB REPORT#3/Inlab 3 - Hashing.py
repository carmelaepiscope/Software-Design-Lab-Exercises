# hashing using separate chaining. 
def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
  
HashTable = [[] for _ in range(10)]
  
def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
      
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
  
insert(HashTable, 10, 'MARIA')
insert(HashTable, 15, 'CARMELA')
insert(HashTable, 20, 'PERALTA')
insert(HashTable, 9, 'EPISCOPE')
insert(HashTable, 16, 'FUTURE')
insert(HashTable, 17, 'ENGINEER')
  
display_hash (HashTable)