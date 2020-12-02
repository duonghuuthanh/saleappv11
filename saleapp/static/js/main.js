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
        var cart = document.getElementById('cart-info');
        cart.innerText = `${data.total_quantity} - ${data.total_amount} VNĐ`
    })
}

function pay() {
    fetch('/payment', {
        method: 'POST',
        headers: {
            "Content-Type": 'application/json'
        }
    }).then(res => res.json()).then(data => {
        alert(data.message);
    })
}