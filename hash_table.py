class KeyValue:
  def __init__(self, key, value):
    self.key = key
    self.value = value

class HashTable:
  def __init__(self, value):
    self.limit = 8
    self.storage = []

  def insert(self, key, value):
    # hash the key and set it as the index
    index = self.hash(key)
    # create a tuple storage bucket
    bucket = self.storage.get(index)

    if bucket == None:
      self.storage.set(index, [key, value])
    else:
      index += 1
      self.storage.set(index, [key, value])

  def retrieve(key):
    index = self.hash(key)
    temp
    bucket = self.storage.get(index)
    if (bucket[0] == key):
      return bucket[1]
    else:
      index += 1
      bucket = self.storage.get(index)
      return bucket[1]

  def remove(key):
    index = self.hash(key)
    temp
    bucket = self.storage.get(index)

    if bucket[0] == key:
      temp = bucket[1]
      bucket = self.storage.set(index, [key, value])
      return temp
    else:
      index += 1
      bucket = self.storage.set(index, [key, value])
      temp = bucket[1]
      return temp