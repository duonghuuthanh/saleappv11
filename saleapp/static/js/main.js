function addToCart(productId, productName, price) {
    fetch('/api/cart', {
        method: 'POST',
        body: JSON.stringify({
            "id": productId,
            "name": productName,
            "price": price
        }),
        headers: {
            "Content-Type": 'application/json'
        }
    }).then(res => res.json()).then(data => {
        console.info(data)
    })
}