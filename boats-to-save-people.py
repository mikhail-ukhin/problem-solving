# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        p1, p2 = 0, len(people) - 1
        boats = 0

        while p1 <= p2:
            if p1 == p2:
                boats += 1
                break

            if people[p2] + people[p1] <= limit: p1 += 1
            
            p2 -= 1
            boats += 1    

        return boats              