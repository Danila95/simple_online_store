$(document).ready(function(){
    let form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e) {
        e.preventDefault(); // отменяем работу функции по умолчанию (в этом случае форма не будет отправляться)
        console.log('123');
        let nmb = $('#number').val();
        console.log(nmb);
        let submit_btn = $('#submit_btn');
        let product_id = submit_btn.data('product_id');
        let product_name = submit_btn.data('name');
        let product_price = submit_btn.data("price");
        let product_currency = submit_btn.data("currency");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        $('.basket-items ul').append('<li>'+product_name+', ' + nmb + 'шт. ' + 'по ' + product_price + ' '+ product_currency + ' ' +
            '<a class="delete-item">X</a>'+
            '</li>');
    });

    function showingBasket() {
       $('.basket-items').removeClass('hidden');
    }

    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        showingBasket();
    });

    $('.basket-container').mouseover( function () {
        showingBasket();
    });

    // $('.basket-container').mouseout( function () {
    //     $('.basket-items').addClass('hidden');
    // });

    $(document).on('click', '.delete-item', function(e) {
        e.preventDefault();
        $(this).closest('li').remove();
    });
});