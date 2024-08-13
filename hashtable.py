def hashletter(letter): #convert a string character to a number for the hashing function
  #a is 1, b is 2... z is 26
  return ord(letter) - ord('A') + 1

class HashTable:#hashtable using quadratic probing
  size = 4*8000+3 #32003, a prime number. this way it works with quadratic probing
  unoccupied = -1

  def __init__(self):
    self.data = [self.unoccupied]*self.size

  def hornerhash(self, string): #create a unique hash for each string using horner's method
    hash = 0
    for i in range(len(string)):
        hash = (hash * 31 + hashletter(string[i])) % self.size #multiplier is 31
    return hash

  def insert(self, key): #insert a key into the table

    #as far as i know, the collision detection isn't really needed. we won't be inserting any values that already exist,
    #as we have to use the search value first to make sure they dont already exist (we dont want duplicates... we want the frequency incremented)
    #oh well. best to just include it. if that code is not running then it is not impacting us to any meaningful degree.

    hash_value = self.hornerhash(key)
    location = hash_value
    probe_attempt = 0

    while True:
      if self.data[location] == self.unoccupied:
        #print(f"Index appears to be unoccupied! Hash is {location}, contents is {self.data[location]}! Tried to insert: {key}")
        break #if the value at the location is -1, break from the loop and immediately insert it
      #print(f"This index already seems to be filled! Hash is {location}, contents is {self.data[location]}! Tried to insert: {key}")
      probe_attempt += 1 #if first condition fails, increment attempt
      location = self.get_probe_location(hash_value, probe_attempt)
      #print(f"Let's probe a new hash!: {location}")

    self.data[location] = key #insert the new element once a valid spot has been found
    #print(f"Data {key} has been inserted into the table! Word hash: {hash_value}, Index Actual: {location}\n")

  def get_probe_location(self, hash_value, i): #if we can't insert the hash at a location, use QP to get the next location to try
    sign = -1 if i % 2 == 0 else 1
    magnitude = ((i + 1) // 2) ** 2
    return (hash_value + sign * magnitude) % self.size

  def search(self, key): #search for a key in the hashtable
        hash_value = self.hornerhash(key)
        location = hash_value
        probe_attempt = 0

        while True:
            if self.data[location] == self.unoccupied:
              #if the first possible hash isn't occupied, then this key could never have been inserted
              #we immediately know it isnt present within the table
              return -1
            if self.data[location] == key:
              return location

            #if the first possible index isn't unoccupied and doesn't contain our key, repeat and check the next possible index (determined with QP)
            probe_attempt += 1
            location = self.get_probe_location(hash_value, probe_attempt)

  def rawprint(self): #print the hashtable, including empty cells
    print(self.data)

  def print(self): #print the hashtable, excluding empty cells
    for i in range(len(self.data)):
      if self.data[i] != self.unoccupied:
        print(f"Index {i}: {self.data[i]}\n")
     