def linear_search_product(product_list,target_product):
    indices = []
    for intax, product in enumerate(product_list):
        if product == target_product:
            indices.append(intax)
    return indices

# Example usage
Products=["shoes","boot","loafer","shoes","sandle","shoes"]
target="shoes"
target2='apple'
result=linearSearchProducts(products,target2)
Print(result)