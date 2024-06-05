 function postData(url = '', data = {}) {
      fetch(url, {
  method: "POST",
  headers: {'Content-Type': 'application/json'}, 
  body: JSON.stringify(data)
}).then(response=>response.json())
.then(bo=>{ 
  if (bo["msg"]!="")
 alert(bo["msg"]);
  if (url=="/register" && bo["msg"]!="")
    $('#Validate_phone_number').modal('show');
})
}

    function send(){
      let inp =  document.getElementById("input");
      postData('/post', {input: inp.value });
  }

  function register(){
    $('#Register').modal('hide');

    let email =  document.getElementById("Editbox2").value;
    let pwd =  document.getElementById("Editbox1").value; 
    let phone =  document.getElementById("Editbox3").value; 
     postData('/register', {email: email,pwd:pwd,phone:phone });
    
  }

  function activate(){
    $('#Validate_phone_number').modal('hide');


    let email =  document.getElementById("Editbox2").value;
    let pwd =  document.getElementById("Editbox1").value; 
    let phone =  document.getElementById("Editbox3").value;
    let smsdigits =  document.getElementById("Editbox5").value; 

     postData('/activate', {email: email,pwd:pwd,phone:phone, smsdigits:smsdigits});
    $('#Validate_phone_number').modal('show');
  }

    function AddService(){
    $('#Register').modal('hide');

    let email =  document.getElementById("Editbox2").value;
    let pwd =  document.getElementById("Editbox1").value; 
    let phone =  document.getElementById("Editbox3").value; 
     postData('/sms-service', {email: email,pwd:pwd,phone:phone });
    $('#Validate_phone_number').modal('show');
  }