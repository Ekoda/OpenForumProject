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

// Sign in 
$('#signin').click(function(){
    $('#sign_in_container').css('display', 'flex')
    $('.sign').css('display', 'none')
    $('#main_signin_button').css('display', 'block')    
})

$(document).mouseup(function(e){
    let container = $("#notificationbox");
    if (!container.is(e.target) && container.has(e.target).length === 0) 
    {
        container.hide(); 
    }
});

// Function for notifications
$('#notification-button').click(function(e){
    e.stopPropagation();
    $('#notificationbox').show();
})




//Scales text area with increasing text
$("textarea").keyup(function(e) {
    while($(this).outerHeight() < this.scrollHeight + parseFloat($(this).css("borderTopWidth")) + parseFloat($(this).css("borderBottomWidth"))) {
        $(this).height($(this).height()+1);
    };
});

// Show input field on press and send & hide if containing value
$('#replybuttonIDx').click(function(){
    $('#replyinputIDx').css('display', 'block');
    if($('#replyinputIDx').val()){
        // SEND REPLY HERE
        $('#replyinputIDx').css('display', 'none');
        $('#replyinputIDx').val('')
    }
})

$('.respond').click(function(){
    let commentID = $(this).attr('id');
    $('#replyinputID' + commentID).css('display', 'block');
    if($('#replyinputID' + commentID).val()){
        // SEND REPLY HERE
        $('#replyinputID' + commentID).css('display', 'none');
        $('#replyinputID' + commentID).val('')
    }
})