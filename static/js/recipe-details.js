window.addEventListener("DOMContentLoaded", function(){
	const deleteButton = document.getElementById("delete-recipe-button");
	deleteButton.addEventListener("click", function(){
		// Replace delete button with "Confirm Delete" version
		const confirmDeleteButton = deleteButton.cloneNode(true);
		confirmDeleteButton.innerText = "Confirm Delete";
		confirmDeleteButton.id = "confirm-delete-recipe-button";
		// Get the route to delete the specific recipe
		confirmDeleteButton.href = deleteButton.dataset["deleteLink"];
		deleteButton.parentElement.appendChild(confirmDeleteButton);
		deleteButton.remove();
	});
});