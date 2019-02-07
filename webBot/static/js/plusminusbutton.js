$(document).ready(function () {
    //onchange of rooms-count
    $(document).on('change', '#rooms', function () {
        var roomsSelected = $('#rooms option:selected').val();
        var roomsDisplayed = $('[id^="room-"]:visible').length;
        var roomsRendered = $('[id^="room-"]').length;
        var orig = $('#peoplerooms').find(roomsSelected);

        //if room count is greater than number displayed - add or show accordingly
        if (roomsSelected > roomsDisplayed) {

            for (var i = 1; i <= roomsSelected; i++) {
                var r = $('#room-' + i);
                if (r.length == 0) {

                    var clone = $('#room-1').clone(); //clone
                    clone.children(':first').text("Room " + i);
                    //change ids appropriately
                    setNewID(clone, i);
                    clone.children('div').children('select').each(function () {
                        setNewID($(this), i);
                    });
                    $(clone).insertAfter($('#room-' + roomsRendered));

                } else {
                    //if the room exists and is hidden 
                    $(r).show();
                }
            }

        } else {
            //else if less than room count selected - hide
            for (var i = ++roomsSelected; i <= roomsRendered; i++) {
                $('#room-' + i).hide();
            }
        }

    });

});


// TOP CONTROLS
$('.plus').click(function (e) {
    e.preventDefault();
    var sp = parseFloat($(this).prev('span').text());
    if(sp<100){
        $(this).prev('span').text(sp + 1);
    }else{
        $(this).next('span').text(100);
    }
});

$('.minus').click(function (e) {
    e.preventDefault();
    var sp = parseFloat($(this).next('span').text());
    $(this).next('span').text(sp - 1);
    if (!isNaN(sp) && sp > 0) {
        $(this).next('span').text(sp - 1);
    } else {
        $(this).next('span').text(0);
    }
});