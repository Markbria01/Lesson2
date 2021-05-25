def discounted(price, discount, max_discount=80):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except(ValueError, TypeError):
        print('no!')

product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,
        'discount': 20}
product['price_discounted'] = discounted(product['price'], product['discount'])
print(product)
    