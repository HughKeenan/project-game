document.addEventListener("DOMContentLoaded", () => {
const editButtons = document.getElementsByClassName("edit-response");
const responseText = document.getElementById("id_content");
const responseForm = document.getElementById("responseForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteResponse"));
const deleteButtons = document.getElementsByClassName("delete-response");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Provides edit function for responses.
 */

  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let responseId = e.target.getAttribute("data-response_id");
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
      let responseId = e.target.getAttribute("data-response_id");
      deleteConfirm.href = `delete_response/${responseId}`;
      deleteModal.show();
    });
  }
});