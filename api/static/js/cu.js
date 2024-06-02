 function postData(url = '', data = {}) {
      fetch(url, {
  method: "POST",
  headers: {'Content-Type': 'application/json'}, 
  body: JSON.stringify(data)
}).then(response=>response.json())
.then(bo=>{ 
 alert(bo["age"]);
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
    $('#Validate_phone_number').modal('show');


  }