// Hide and Show OpenForum
$("#hideopenforum").on("click", function(){
    if ( $('#hideopenforum').attr('class') == 'fas fa-chevron-right' ){
        $('#hideopenforum').removeClass('fa-chevron-right').addClass('fa-chevron-left')
        $('#chat').css('display', 'none')
        $('#web').css('width', '100%')
    } else if ( $('#hideopenforum').attr('class') == 'fas fa-chevron-left' ){
        $('#hideopenforum').removeClass('fa-chevron-left').addClass('fa-chevron-right')
        $('#chat').css('display', 'block')
        $('#web').css('width', '80%')
    }
});
