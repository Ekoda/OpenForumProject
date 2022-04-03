$('#reset_password').click(function(){
    let email = $("#reset_password_email").val()
    let api_url = window.location.origin + "/api/resetpassword";
    let data = {"email": email}

    $.ajax({
        type: "POST",
        url: api_url,
        data: JSON.stringify(data),
        contentType : 'application/json',
        success: function(){
            alert("Successfully reset password, check email for instructions")
            window.location.href = "/index"
        }
      });
    })