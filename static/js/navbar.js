function collapseNav() {
  document.getElementById("sideBar").classList.toggle('active');
}

function collapseConfig() {
  document.getElementById("setor").classList.toggle('ativarMenu');
  document.getElementById("camera").classList.toggle('ativarMenu');
}

function logoutSession(){
  document.cookie = "access_token_cookie=";
  window.location.reload(true);
}