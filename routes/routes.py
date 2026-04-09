class Routes:
    #PRODUCTS
    #todo: the "products" strings gets repeated - refactor this so it is only defined once
    BASE_URL:str = "https://fakestoreapi.com"
    PRODUCTS_ENDPOINT_MJ:str = f"{BASE_URL}/products"
    GET_ALL_PRODUCTS:str = "/products"
    GET_PRODUCT_BY_ID:str =  "/products/{id}"
    GET_PRODUCTS_WITH_LIMIT:str = "/products?limit={limit}"
    GET_PRODUCTS_SORTED:str = "/products?sort={order}"
    GET_ALL_CATEGORIES:str = "/products/categories"
    GET_PRODUCTS_BY_CATEGORY:str = "/products/category/{category}"
    CREATE_PRODUCT:str = "/products"
    UPDATE_PRODUCT:str = "/products/{id}"
    DELETE_PRODUCT:str = "/products/{id}"

    GET_ALL_CARTS:str = "/carts"
    GET_CART_BY_ID_ENDPOINT:str = "/carts/{id}"
    GET_CARTS_WITH_LIMIT:str = "/carts?limit={limit}"
    GET_CARTS_SORTED:str = "/carts?sort={order}"

    #todo: remove a product from a cart?delete a cart?


