class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        # n diff recipes

        # given a string array recipes and a 2d string array ingredients
        # ith recipe has the name recipes[i] and you can create it


        # output recipes we can create
        # topological sort
        # start with supplies
        # create a graph from ingredient to recipe
        # and hmap of recipe: ingredient count

        graph_ing_to_recipe = defaultdict(list)
        ing_count_hmap = {}

        for ingredient_list, recipe in zip(ingredients, recipes):
            for ingredient in ingredient_list:
                graph_ing_to_recipe[ingredient].append(recipe)
            
            ing_count_hmap[recipe] = len(ingredient_list)
        
        queue = deque()
        visited = set()

        for ing in supplies:
            queue.append(ing)
            visited.add(ing)
        
        answer = []
        while queue:
            ing = queue.popleft()

            for recipe in graph_ing_to_recipe[ing]:
                # if ing_count_hmap.get(recipe, 0) == 0:
                if recipe not in visited:
                    ing_count_hmap[recipe] -= 1

                    if ing_count_hmap[recipe] == 0:
                        visited.add(recipe)
                        queue.append(recipe)
                        answer.append(recipe)
        
        return answer
        




