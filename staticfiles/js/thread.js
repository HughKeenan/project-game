const editThreadButtons = document.getElementsByClassName("threadButton");
const threadText = document.getElementById("id_body");
const threadForm = document.getElementById("threadForm");
const submitThreadButton = document.getElementById("submitButton");

/**
* Provides edit function for buttons on threads.
*/

for (let button of editThreadButtons) {
  button.addEventListener("click", (e) => {
    let threadId = e.target.getAttribute("thread_id");
    let threadContent = document.getElementById(`thread${threadId}`).innerHTML;
    threadText.value = threadContent;
    submitThreadButton.innerHTML = "Update";
    threadForm.setAttribute("action", `edit_thread/${threadId}`);
  });
}