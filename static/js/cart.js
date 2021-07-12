window.onload = function () {
    $('.cart_list').on('click', 'input[type="number"]', function (){
        let t_href = event.target;
        // console.log(t_href.name);
        // console.log(t_href.value);

        $.ajax({
            url: '/carts/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data) {
                $('.cart_list').html(data.result);
            }
        });
        event.preventDefault();
    })
}