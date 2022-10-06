// Получить модальный
var modal = document.getElementById("myModal1");

// Получить кнопку, которая открывает модальный
var btn = document.getElementById("catalog_button_1");

// Получить элемент <span>, который закрывает модальный
var span = document.getElementsByClassName("close")[1];

// Когда пользователь нажимает на кнопку, откройте модальный
btn.onclick = function() {
  modal.style.display = "block";
}

// Когда пользователь нажимает на <span> (x), закройте модальное окно
span.onclick = function() {
  modal.style.display = "none";
}

// Когда пользователь щелкает в любом месте за пределами модального, закройте его
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}