const editButtons = document.getElementsByClassName("btn-edit");
const responseText = document.getElementById("id_content");
const responseForm = document.getElementById("responseForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteResponse"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Provides edit function for responses.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let responseId = e.target.getAttribute("response_id");
    let responseContent = document.getElementById(`response${responseId}`).innerText;
    responseText.value = responseContent;
    submitButton.innerText = "Update";
    responseForm.setAttribute("action", `edit_response/${responseId}`);
  });
}

/**
* Provides delete function for responses.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let responseId = e.target.getAttribute("response_id");
      deleteConfirm.href = `delete_response/${responseId}`;
      deleteModal.show();
    });
  }