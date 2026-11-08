class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        unplaced = 0

        for fruit in fruits:
            placed = False

            for j in range(len(baskets)):
                if baskets[j] >= fruit:
                    baskets[j] = 0
                    placed = True
                    break

            if not placed:
                unplaced += 1

        return unplaced