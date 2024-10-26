const editThreadButtons = document.getElementsByClassName("threadButton");
const threadTitle = document.getElementById("id_title")
const threadText = document.getElementById("id_body");
const threadForm = document.getElementById("threadForm");
const submitThreadButton = document.getElementById("submitThreadButton");

/**
* Provides edit function for buttons on threads.
*/

for (let button of editThreadButtons) {
  button.addEventListener("click", (e) => {
    let titleId = e.target.getAttribute("title_id");
    let threadId = e.target.getAttribute("thread_id");
    let titleContent = document.getElementById(`title`).innerText;
    let threadContent = document.getElementById(`thread${threadId}`).innerText;
    threadTitle.value = titleContent
    threadText.value = threadContent;
    submitThreadButton.innerText = "Update";
    threadForm.setAttribute("action", `edit_thread/${titleId}`);
    threadForm.setAttribute("action", `edit_thread/${threadId}`);
  });
}