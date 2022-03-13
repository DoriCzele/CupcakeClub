window.addEventListener("DOMContentLoaded", event => {
	const deleteButton = document.getElementById("delete-recipe-button");
	deleteButton.addEventListener("click", event => {
		const confirmDeleteButton = deleteButton.cloneNode(true)
		confirmDeleteButton.innerText = "Confirm Delete";
		confirmDeleteButton.id = "confirm-delete-recipe-button"
		confirmDeleteButton.href = deleteButton.dataset["deleteLink"];
		deleteButton.parentElement.appendChild(confirmDeleteButton);
		deleteButton.remove()
	})
})