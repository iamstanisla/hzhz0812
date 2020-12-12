var countDiv = 1;
let idDivTemplateTest = "divTemplate";

function addField() {
  let newIdDiv = "newDiv_" + countDiv;
  let newIdNameChild = "name_" + (countDiv + 1);

  let newDiv = document.getElementById(idDivTemplateTest).cloneNode(true);
  newDiv.id = newIdDiv;
  let childInput = newDiv.querySelector('input');
  childInput.id = newIdNameChild;
  childInput.name = newIdNameChild;
  

  let divButtons = document.getElementById("divButtons");
  divButtons.before(newDiv);

  countDiv++;
}

function delField() {
  if (countDiv != 1) {
  let IdDiv = "newDiv_" + (countDiv - 1);
  document.getElementById(IdDiv).remove();
  countDiv--;
 }
}


add.addEventListener("click",  addField);
del.addEventListener("click", delField);
