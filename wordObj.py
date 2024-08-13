class wordObj:
    def __init__(self, spelling):
        self.frequency = 1
        self.spelling = spelling
        self.followingWords = [] #list of words that follow this word in the corpus

  #fancy string method for when it is called in print
    def __str__(self):
        return f"Lexicon Object: {self.spelling} (Frequency: {self.frequency}) (List of Following Words: {self.followingWords})"

    def __repr__(self):
        return f"Lexicon Object: {self.spelling} (Frequency: {self.frequency}) (List of Following Words: {self.followingWords})"

  #COMPARISON OPERATORS
  #these will let us do our sorting later!
  #as these word objects arent numbers, it is not immediately obvious
  #to the interpreter how to compare them when we try to do comparison
  #we use the following methods to instruct the interpreter that
  #this object should be compared based on the value of spelling

  #equality
    def __eq__(self,other):
        if isinstance(other, int):
            return False #this is required for the hashtable implementation when we want to compare it against empty table positions containing "-1"
        else:
            return self.spelling == other.spelling

  #less than
    def __lt__(self,other):
        if isinstance(other, int):
            return True
        return self.spelling < other.spelling

  #greater than
    def __gt__(self,other):
        if isinstance(other, int):
            return False
        return self.spelling > other.spelling

  #less than or equal to
    def __le__(self,other):
        if isinstance(other, int):
            return False
        return self < other or self == other

  ##NEW THINGS TO MAKE QP WORK

  #length
    def __len__(self):
    #correctly return length of the object (its spelling)
	    return len(self.spelling)

  #subscripting (accessing string chars like a list) (i.e. string[3])
    def __getitem__(self, item):
        return self.spelling[item]