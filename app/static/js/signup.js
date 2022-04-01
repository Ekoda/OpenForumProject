$('#create_acc').click(function(){

    let username = $("#create_acc_username").val()
    let email = $("#create_acc_email").val()
    let password_one = $("#create_acc_password").val()
    let password_two = $("#create_acc_repeat_password").val()
    if (password_one !== password_two){
        return alert("Please make sure your passwords match")
    }

    let api_url = window.location.origin + "/api/users";
    let user = {
        "username": username,
        "email": email,
        "password": password_one
    }
    $.ajax({
        type: "POST",
        url: api_url,
        data: JSON.stringify(user),
        contentType : 'application/json',
        success: function(){
            alert("account successfully created")
            window.location.href = "/index"

        }
      });

    })