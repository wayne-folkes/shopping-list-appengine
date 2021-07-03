"use strict";

window.addEventListener("load", function () {
  console.log("Hello World!");
});


document.getElementById("select-all").onclick = function () {
  var checkboxes = document.getElementsByName("key");
  for (var checkbox of checkboxes) {
    checkbox.checked = this.checked;
  }
};
