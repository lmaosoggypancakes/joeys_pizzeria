"use strict";

document.addEventListener('DOMContentLoaded', function (e) {});

function add_to_order(data) {
  id = parseInt(data);
  fetch("/api/add/".concat(id)).then(function (Response) {
    return Response.json();
  }).then(function (data) {
    alert(data.message);
  });
}

function remove_from_order(item) {
  row = item.parentNode.parentNode;
  id = parseInt(item.dataset.item);
  fetch("/api/remove/".concat(id)).then(function (response) {
    return response.json();
  }).then(function (data) {
    alert(data.message);
    row.style.display = "none";
  });
}