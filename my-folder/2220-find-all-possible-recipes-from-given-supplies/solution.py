from collections import defaultdict
class Solution:
    def get_dish_order(self, recipes, ingredients):
        dish_order = defaultdict(int)
        for recipe, ing in zip(recipes, ingredients):
            dish_order[recipe] = len(ing)
        return dish_order
    
    def get_prereq_dish_map(self, recipes, ingredients):
        prereq_dish_map = defaultdict(list)
        for recipe, ing in zip(recipes, ingredients):
            for i in ing:
                prereq_dish_map[i].append(recipe)
        return prereq_dish_map
    
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        # indegree dict
        dish_order = self.get_dish_order(recipes, 
                                         ingredients)
        # graph
        prereq_dish_map = self.get_prereq_dish_map(recipes, ingredients)
        
        queue = supplies.copy()
        
        res = []
        while queue:
            curr_dish = queue.pop(0)
            if curr_dish in recipes:
                res.append(curr_dish)
            # prereq -> dish
            for dish in prereq_dish_map[curr_dish]:
                dish_order[dish] -= 1
                if dish_order[dish] == 0:
                    queue.append(dish)
        
        return res
                        
            
