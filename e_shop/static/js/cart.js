document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.catalog');

    container.addEventListener('click', function(event) {
        if (event.target.classList.contains('cart-update')) {
            let product_id = event.target.dataset.product;
            let action = event.target.dataset.action;
            console.log(product_id, action);

            updateOrder(product_id, action)
        }
    });
});

function updateOrder(product_id, action) {
    // Prepend the base URL to the relative URL
    let baseUrl = window.location.protocol + "//" + window.location.host;
    let url = baseUrl + '/cart/add_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken // Ensure csrftoken is defined somewhere in your script
        },
        body: JSON.stringify({'product_id': product_id, 'action': action})
    })
   .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)
    })
}