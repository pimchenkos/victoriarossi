//Dropdown menu-------------------------------------
/* Когда пользователь нажимает на кнопку,
переключение между скрытием и отображением раскрывающегося содержимого */
function DropdownFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}
// Закройте раскрывающийся список, если пользователь щелкает за его пределами
window.onclick = function (event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
  if (event.target == modal) {
    modal.style.display = "none";
    htmlStyle.style.overflow = "auto";
    btn.style.visibility = "visible";
  }
}

// Get the modal
var modal = document.getElementById("modalAppointment");

// Get the button that opens the modal
var btn = document.getElementById("btnAppointment");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close-appointment")[0];

// Get the <html> element
var htmlStyle = document.documentElement;

// When the user clicks the button, open the modal
btn.onclick = function () {
  modal.style.display = "block";
  htmlStyle.style.overflow = "hidden";
  btn.style.visibility = "hidden";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
  htmlStyle.style.overflow = "auto";
  btn.style.visibility = "visible";
}