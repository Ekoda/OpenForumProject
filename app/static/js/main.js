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

// Temporary Sign in 
$('#signin').on("click", function(){
    $('.sign').css('display', 'none')
    $('#info').css('display', 'flex')
    $('#picture').css('display', 'block')

})

// Notification box 

// To stop event from firing when clicking on child 
$("#notificationbox").click(function(e){
    e.stopPropagation();
})

// Toggle notifications
$('#notification-button').on("click", function(){
    if($('#notificationbox').css('display') == 'none'){
        $('#notificationbox').css('display', 'block')
    } else if ($('#notificationbox').css('display') == 'block'){
        $('#notificationbox').css('display', 'none')
    }
})

//Hide notification box on click outside
$(document).mouseup(function(e) 
{
    let container = $("#notificationbox");
    
    if (!container.is(e.target) && container.has(e.target).length === 0) 
    {
        container.css('display', 'none');
    }
    $('#notification-button').on("click", function(){
        if($('#notificationbox').css('display') == 'none'){
            $('#notificationbox').css('display', 'block')
        } else if ($('#notificationbox').css('display') == 'block'){
            $('#notificationbox').toggle()
        }
    })
});

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