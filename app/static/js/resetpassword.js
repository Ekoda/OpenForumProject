$('#reset_password').click(function(){
    let email = $("#reset_password_email").val()
    let api_url = window.location.origin + "/api/resetpassword";
    let data = {
        "email": email}

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

$('#final_reset_password').click(function(){
    const segments = new URL(href).pathname.split('/');
    const token = segments.pop() || segments.pop();
    let password_one = $("#reset_acc_password").val()
    let password_two = $("#reset_acc_repeat_password").val()
    if (password_one !== password_two){
        return alert("Please make sure your passwords match")
    }
    let api_url = window.location.origin + "/api/create_password";
    let data = {
        "token": token,
        "password": password_one}

    $.ajax({
        type: "POST",
        url: api_url,
        data: JSON.stringify(data),
        contentType : 'application/json',
        success: function(){
            alert("Successfully created new password")
            window.location.href = "/index"
        }
      });
    })