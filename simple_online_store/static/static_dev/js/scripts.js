$(document).ready(function(){
    let form = $('#form_buying_product');
    console.log(form);

    function basketUpdating(product_id, nmb, is_delete) {
        let data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
			data["is_delete"] = true;
		}

        let url = form.attr("action");
        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK');
                console.log(data.products_total_nmb);
                if (data.products_total_nmb || data.products_total_nmb == 0) {
                    $('#basket_total_nmb').text('('+data.products_total_nmb+")");
                    console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products, function(k, v) {
                        $('.basket-items ul').append('<li>'+v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + ' '+ v.currency + ' ' +
                            '<a class="delete-item" data-product_id="'+ v.id +'">X</a>'+
                            '<p>Всего: ' + v.total_price + ' ' + v.currency + '</p></li>');
                    });
                }
            },
            error: function () {
                console.log('error')
            }
        });

    }

    form.on('submit', function(e) {
        e.preventDefault(); // отменяем работу функции по умолчанию (в этом случае форма не будет отправляться)
        let nmb = $('#number').val();
        console.log('nmb = ' + nmb);
        let submit_btn = $('#submit_btn');
        let product_id = submit_btn.data('product_id');
        let product_name = submit_btn.data('name');
        let product_price = submit_btn.data("price");
        let product_currency = submit_btn.data("currency");

        // подсчитаем общую цену за один конкретный товар (если берется несколько штук)
        product_price = product_price.replace( /,/g, "." ); // JS обозначает вещественные числа точкой
        let total_price = parseFloat(nmb) * parseFloat(product_price);
        // подготовления числа для отображения в списке корзины
        total_price = total_price.toFixed(2);
        total_price = String(total_price);
        total_price = total_price.replace( ".", "," );
        console.log(total_price);

        basketUpdating(product_id, nmb, is_delete=false);


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

    $('.basket-container').mouseout( function () {
        $('.basket-items').addClass('hidden');
    });

    $(document).on('click', '.delete-item', function(e) {
        e.preventDefault();
        product_id = $(this).data("product_id");
        nmb = 0;
        basketUpdating(product_id, nmb, is_delete=true);
    });

    function calculatingBasketAmount(){
		var total_order_amount = 0;
		$('.total-product-in-basket-amount').each(function() {
			total_order_amount = total_order_amount + parseFloat($(this).text());
		});
		console.log(total_order_amount);
		$('#total_order_amount').text(total_order_amount.toFixed(2));
	};

    $(document).on('change', ".product-in-basket-nmb", function(){
		var current_nmb = $(this).val();
		console.log(current_nmb);

		var current_tr = $(this).closest('tr');
		var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
		console.log(current_price);
		var total_amount = parseFloat(current_nmb*current_price).toFixed(2);
		console.log(total_amount);
		current_tr.find('.total-product-in-basket-amount').text(total_amount);

		calculatingBasketAmount();
	});

    calculatingBasketAmount();

});