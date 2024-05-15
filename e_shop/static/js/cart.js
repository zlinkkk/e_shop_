document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.catalog');

    container.addEventListener('click', function(event) {
        if (event.target.classList.contains('cart-update')) {
            let product_id = event.target.dataset.product;
            let action = event.target.dataset.action;
            console.log(product_id, action);

            updateOrder()
        }
    });
});

function updateOrder(product_id, action){
    let url = '/add_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'product_id': product_id, 'action': action})
    })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data')
        })
}