"use strict";


if (document.getElementById("select-all") !== null) {
  document.getElementById("select-all").onclick = function () {
    var checkboxes = document.getElementsByName("key");
    for (var checkbox of checkboxes) {
      checkbox.checked = this.checked;
    }
  };
}

function success() {
  if (document.getElementById("new_item").value === "") {
    document.getElementById("new_item_btn").disabled = true;
  } else {
    document.getElementById("new_item_btn").disabled = false;
  }
}

const addItems = () => {
  let formElement = document.getElementById('add_form')

  // let ol = document.getElementById("item_list");
  // let li = document.createElement("li");
  // li.appendChild(
  //   document.createTextNode(document.getElementById("new_item").value)
  // );
  // ol.appendChild(li);
  let request = new XMLHttpRequest()
  request.open("POST", '/add')
  request.send(new FormData(formElement))
}

// document.getElementById("new_item").focus();
// document.getElementById("new_item").select();



