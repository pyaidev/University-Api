**base.html**
```
$('.add-course').on('click', function () {
        let _cid = $(this).data('course')
        let _btn = $(this)

        alert(_cid)

        // Ajax
        $.ajax({
            url: '/course/add-course/',
            data: {
                _cid
            },
            dataType: 'json',
            success: function (res) {
                console.log(res) // 1 === '1'
                if (res.success === true) {
                    // _btn.removeClass('add-wishlist').addClass('disabled');
                    alert(res.product + ' saved');
                } else {
                    alert(res.product + ' removed');
                }
                location.reload();
            }
        });
	```
