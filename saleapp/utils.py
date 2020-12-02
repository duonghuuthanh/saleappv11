import json, hashlib
from saleapp import db
from saleapp.models import User, Product, Receipt, ReceiptDetail


def read_data(path='data/categories.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def read_products(kw=None, cate_id=None,
                  from_price=None, to_price=None):
    products = Product.query

    if cate_id:
        products = products.filter(Product.category_id==cate_id)

    if kw:
        products = products.filter(Product.name.contains(kw))

    if from_price and to_price:
        products = products.filter(Product.price.__gt__(from_price),
                                   Product.price.__lt__(to_price))

    return products.all()
    # products = read_data(path='data/products.json')
    #
    # if cate_id:
    #     cate_id = int(cate_id)
    #     products = [p for p in products if (p['category_id'] == cate_id)]
    #
    # if kw:
    #     products = [p for p in products if p['name'].find(kw) >= 0]
    #
    # if from_price and to_price:
    #     from_price = float(from_price)
    #     to_price = float(to_price)
    #
    #     products = [p for p in products if p['price'] >= from_price and p['price'] <= to_price]
    #
    # return products


def get_product_by_id(product_id):
    return Product.query.get(product_id)
    # products = read_data('data/products.json')
    # for p in products:
    #     if p["id"] == product_id:
    #         return p


def add_user(name, email, username, password, avatar):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    u = User(name=name,
             email=email,
             username=username,
             password=password,
             avatar=avatar)
    try:
        db.session.add(u)
        db.session.commit()

        return True
    except Exception as ex:
        print(ex)
        return False


def cart_stats(cart):
    if cart is None:
        return 0, 0

    products = cart.values()

    quantity = sum([p['quantity'] for p in products])
    price = sum([p['price']*p['quantity'] for p in products])

    return quantity, price


def add_receipt(cart):
    if cart:
        try:
            receipt = Receipt(customer_id=1)
            db.session.add(receipt)

            for p in list(cart.values()):
                detail = ReceiptDetail(product_id=int(p["id"]),
                                       receipt_id=receipt.id,
                                       price=float(p["price"]),
                                       quantity=p["quantity"])
                db.session.add(detail)

            db.session.commit()

            return True
        except :
            pass

    return False