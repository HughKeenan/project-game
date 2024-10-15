const editButtons = document.getElementsByClassName("btn-edit");
const responseText = document.getElementById("id_body");
const responseForm = document.getElementById("responseForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated response's ID upon click.
* - Fetches the content of the corresponding response.
* - Populates the `responseText` input/textarea with the response's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_response/{responseId}` endpoint.
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
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let responseId = e.target.getAttribute("response_id");
      deleteConfirm.href = `delete_response/${responseId}`;
      deleteModal.show();
    });
  }