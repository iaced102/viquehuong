

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


