# Insert Delete GetRandom O(1)
# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the dict if not already present.
# remove(val): Removes an item val from the dict if present.
# getRandom: Returns a random element from current dict of elements. Each element must have the same probability of being returned.
# Example:

# // Init an empty dict.
# RandomizedSet randomSet = new RandomizedSet();

# // Inserts 1 to the dict. Returns true as 1 was inserted successfully.
# randomSet.insert(1);

# // Returns false as 2 does not exist in the dict.
# randomSet.remove(2);

# // Inserts 2 to the dict, returns true. dict now contains [1,2].
# randomSet.insert(2);

# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();

# // Removes 1 from the dict, returns true. dict now contains [2].
# randomSet.remove(1);

# // 2 was already in the dict, so return false.
# randomSet.insert(2);

# // Since 2 is the only number in the dict, getRandom always return 2.
# randomSet.getRandom();

import random

class RandomizedSet(object):

    def __init__(self):
        self.dict = {}
        self.arr = [] 
        self.count = 0

    def insert(self, val):
        if val in self.dict: return False

        self.arr.append(val)
        self.count += 1
        self.dict[val] = self.count - 1

        return True

    def remove(self, val):
        if not val in self.dict: return False

        index = self.dict[val]
        last_val = self.arr[self.count - 1]

        self.arr[index] = last_val
        self.arr = self.arr[:self.count - 1]
        self.dict[last_val] = index
        self.count -= 1
        
        del self.dict[val]

        return True    

    def getRandom(self):
        return self.arr[random.randint(0, self.count - 1)]