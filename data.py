import openfoodfacts

def fetch_nutrition_score(item):
    try:
        search_result = openfoodfacts.products.search(item)
        return search_result['products'][0]['nutrition_grades']
    
    
    except: 
        return('No grade found')