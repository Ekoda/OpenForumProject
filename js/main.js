// Hide and Show OpenForum
$("#hideopenforum").on("click", function(){
    if ( $('#hideopenforum').attr('class') == 'fas fa-chevron-right' ){
        $('#hideopenforum').removeClass('fa-chevron-right').addClass('fa-chevron-left')
        $('#chat').css('display', 'none')
        $('#web').css('width', '100%')
        $('#web').css('display', 'block')
    } else if ( $('#hideopenforum').attr('class') == 'fas fa-chevron-left' ){
        $('#hideopenforum').removeClass('fa-chevron-left').addClass('fa-chevron-right')
        $('#chat').css('display', 'block')
        $('#web').css('width', '80%')
        
        let screen = $(window)
        if (screen.width() < 500) {
            $('#web').css('display', 'none')
        }
    }
});

/*

// Optional alert message on change of page

setTimeout(function() {
    $('#web').on('load', function() {
        alert('For security reasons Open Forum is not tracking the changing URL, please copy URL to the Open Forum model to enter the Forum of the page entered.');
    });
  }, 3000);
*/
