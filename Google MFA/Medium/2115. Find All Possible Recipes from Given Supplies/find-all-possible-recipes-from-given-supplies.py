from collections import defaultdict, deque
from typing import List

'''
Input:
recipes = ["bread","sandwich","burger"]
              0       1         2
ingredients = [
    0: ["yeast","flour"],
    1: ["bread","meat"],
    2: ["sandwich","meat","bread"]]

in_degrees = {
    "yeast":
}

supplies = ["yeast","flour","meat"]


Output: ["bread","sandwich","burger"]
'''


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        in_degree = defaultdict(int)
        graph = defaultdict(list)

        for i in range(len(recipes)):
            in_degree[recipes[i]] = len(ingredients[i])
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])

        zero_degrees = deque(supplies)

        output = []
        recipes = set(recipes)

        while zero_degrees:
            node = zero_degrees.popleft()

            if node in recipes:
                output.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_degrees.append(neighbor)

        return output


if __name__ == '__main__':
    sol = Solution()

    recipes = ["bread", "sandwich", "burger"]
    ingredients = [["yeast", "flour"],
                   ["bread", "meat"],
                   ["sandwich", "meat", "bread"]
                   ]

    supplies = ["yeast", "flour", "meat"]

    print(sol.findAllRecipes(recipes, ingredients, supplies))
