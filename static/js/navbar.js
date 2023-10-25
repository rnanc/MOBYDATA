function collapseNav() {
  document.getElementById("sideBar").classList.toggle('active');
}

function logoutSession(){
  document.cookie = "access_token_cookie=";
  window.location.href = "/";
}
