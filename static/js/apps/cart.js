var cart_buy =[]

function total(id)
    {
        $(`#total_${id}`).html($(`#count_${id}`).html() * $(`#price_${id}`).html())
    }

function reduce(id)
    {
        $(`#count_${id}`).html(parseInt($(`#count_${id}`).html())-1)
            if($(`#count_${id}`).html()==1)
                {
                    $(`#reduce_${id}`).attr('disabled', true);
                }
            else
                {
                    $(`#reduce_${id}`).attr('disabled', false);
                }
            total(id)
            if($(`#count_${id}`).html()==1)
                {
                    $(`#reduce_${id}`).attr('onclick', '');
                    $(`#reduce_${id}`).attr('style', 'cursor: not-allowed;border-right: rgb(92, 92, 92) solid 1px;');
                }
            footer_button()
    }

function add(id)
    {            
        $(`#count_${id}`).html(parseInt($(`#count_${id}`).html())+1)
            if($(`#count_${id}`).html()==1)
                {
                    $(`#reduce_${id}`).attr('disabled', true);
                }
            else
                {
                    $(`#reduce_${id}`).attr('disabled', false);
                }
            total(id)
            if($(`#count_${id}`).html()==1)
                {
                    $(`#reduce_${id}`).attr('onclick', '');
                    $(`#reduce_${id}`).attr('style', 'cursor: not-allowed;border-right: rgb(92, 92, 92) solid 1px;');
                }
            else
                {
                    $(`#reduce_${id}`).attr('onclick', `reduce(${id})`);
                    $(`#reduce_${id}`).attr('style', 'border-right: rgb(92, 92, 92) solid 1px;');
                }
            footer_button()
    }



function footer_button()
    {
        let count =0
        for(let item in cart_amount)
            {
                if(cart_amount[item][0] != $(`#count_${cart_amount[item][1]}`).html())
                    {
                        count ++
                    }
            }
        if(count !=0)
            {
                $("#save_cart").attr("style", '')
            }
        else
            {
                $("#save_cart").attr("style", 'display: none')
            }


        if(cart_buy.length === 0)
            {
                $("#buy_cart").attr("style", 'display: none')
            }
        else
            {
                $("#buy_cart").attr("style", '')
            }
        if($("#buy_cart").attr('style') != '' && $("#save_cart").attr('style'))
            {
                $(".footer-fixed").attr('style', 'display: none')
            }
        else
            {
                $(".footer-fixed").attr('style', '')
            }
    }

function check_checkbox(item)
    {
        if(cart_buy.indexOf(item.value) == -1)
            {
                cart_buy.push(item.value)
            }
        else
            {
                cart_buy.splice(cart_buy.indexOf(item.value), 1)
            }
        footer_button()
    }