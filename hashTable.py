class KeyValue:
  def __init__(self, key, value):
    self.key = key
    self.value = value


class HashTable:
  def __init__(self, value):
    self.limit = 8
    self.storage = [0]*8


  def insert(self, key, value):
    # call self.hash(key) to get index
    index = self.hash(key)
    bucket = self.storage.get(index)
    # insert new key-value pair into bucket
    if bucket == None:
      self.storage.set(index, [key, value])
    elif bucket[0] == key and bucket[1] != value:
      self.storage.set(index, [key, value])
    else:
      index += index
      self.storage.set(index, [key, value])



  def retrieve(self, key):
    index = self.hash(key)
    bucket = self.storage.get(index)

    if bucket[0] == key:
      return bucket[1]
    else:
      index += index
      bucket = self.storage.get(index)
      return bucket[1]
    # call self.hash(key) to get index
    # find the correct key at that bucket


  def remove(self, key, value):
    index = self.hash(key)
    temp_value = ''
    bucket = self.storage.get(index)
    if bucket[0] == key:
      temp_value = bucket[1]
      bucket = self.storage.set(index, [k, None])
      return temp_value
    else:
      index += index
      bucket = self.storage.set(index, [k, None])
      temp_value = bucket[1]
      return temp_value


      # call self.hash(key) to get index
      # insert new key-value pair that bucket

  def hash(self, key):
    print(key)
    #loop through the characters of the key
    # return sum(ord(char) - ord('a') + 1 for char in key.lower()) % tablesize
    return sum(ord(char) - ord('a') + 1 for char in key.lower()) % 8
    # for x in len(key):

    # convert the char to a number (use ord(c))
    # add this number to a running total
    # return % size

# class HashInit():
#     def __init__(self,key):
#         self.key = None

def initialize():
    htable = HashTable()
    htable.insert('horse','caballo')
    val = htable.retrieve('horse')

if __name__ == "__main__":
    initialize()
