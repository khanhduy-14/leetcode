class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)

        # Create a graph mapping each recipe to its list of ingredients
        recipe_graph = {recipe: ingredients[i] for i, recipe in enumerate(recipes)}
        
        # Memoization map: True if recipe can be made, False if not
        visited = {}

        def dfs(recipe: str) -> bool:
            if recipe in visited:
                return visited[recipe]

            # Detect cycle or assume failure until proven otherwise
            visited[recipe] = False

            for ing in recipe_graph[recipe]:
                if ing in recipe_graph:
                    if not dfs(ing):
                        return False
                elif ing not in supplies:
                    return False

            # All ingredients are available
            visited[recipe] = True
            return True

        result = []
        for recipe in recipes:
            if dfs(recipe):
                result.append(recipe)

        return result