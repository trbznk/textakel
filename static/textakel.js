LORE = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
ENDPOINT = window.location.href + "api/v1/";
ENDPOINT_FUNCTIONS = window.location.href + "api"
REQUEST = new XMLHttpRequest();

function get_textarea(){
  return document.getElementById("input");
}

function set_textarea(){
  response = REQUEST.response["text"]
  textarea = get_textarea();
  textarea.value = response;
}

function api(function_name, text) {
  url = ENDPOINT + function_name + "/" + text;
  REQUEST.open("GET", url);
  REQUEST.responseType = "json";
  REQUEST.send();
  REQUEST.onload = set_textarea;
}

function functions_change(ev){

  text = get_textarea().value;
  name = ev.srcElement.value;

  if (text.length > 0 && name != "0"){
    api(name, text);
  }
}

function api_functions(){
  REQUEST.open("GET", ENDPOINT_FUNCTIONS);
  REQUEST.responseType = "json";
  REQUEST.send();
  REQUEST.onload = create_buttons;
}

function create_buttons(){
  function_names = REQUEST.response["functions"];
  functions = document.getElementById('functions');
  for(function_name of function_names){
    link = document.createElement("option");
    link.setAttribute("value", function_name);
    link.innerHTML = function_name;
    functions.appendChild(link);
  }
  functions.addEventListener("change", functions_change);
}

function btn_lore_click() {
  get_textarea().value = LORE;
}

function btn_copy_click() {
  input = get_textarea();
  input.select()
  document.execCommand("copy");
}

function btn_trash_click() {
  get_textarea().value = "";
}

function init(){
  api_functions();

  btn_lore = document.getElementById("btn_lore");
  btn_copy = document.getElementById("btn_copy");
  btn_trash = document.getElementById("btn_trash");
  btn_lore.addEventListener("click", btn_lore_click);
  btn_copy.addEventListener("click", btn_copy_click);
  btn_trash.addEventListener("click", btn_trash_click);
}

init();
