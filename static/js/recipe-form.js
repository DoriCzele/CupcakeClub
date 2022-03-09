window.addEventListener("DOMContentLoaded", event => {
	// Allow ingredient to be added either with button or "Enter" key
	const ingredientInputField = document.getElementById("ingredient-field")
	ingredientInputField.addEventListener("keypress", event => {
		if (event.key == "Enter"){
			event.preventDefault()
			if (ingredientInputField.value !== ""){
			addIngredientToList(ingredientInputField.value);
			}
		}
	})
	const addIngredientButton = document.getElementById("add-ingredient")
	addIngredientButton.addEventListener("click", function(){
		if (ingredientInputField.value !== ""){
		addIngredientToList(ingredientInputField.value)}
	})
})

function addIngredientToList(newIngredientName){
	// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template
	const ingredientsInputSection = document.getElementById("ingredients-input");
	const inputGroups = ingredientsInputSection.querySelectorAll(".input-group");
	const lastInputGroup = inputGroups[inputGroups.length-1];
	// Increment the last ingredient ID value if it exists
	let newInputGroupIncrement = 0;
	if (lastInputGroup){
		newInputGroupIncrement = parseInt(lastInputGroup.querySelector("input").dataset.increment) + 1;
	}

	// Get input-group template and clone it
	const ingredientTemplate = document.getElementById("ingredient-template");
	const ingredientTemplateClone = ingredientTemplate.content.cloneNode(true);
	const ingredientTemplateCloneInput = ingredientTemplateClone.querySelector("input");
	ingredientTemplateCloneInput.name = `ingredient${newInputGroupIncrement}`;
	ingredientTemplateCloneInput.dataset.increment = newInputGroupIncrement;
	ingredientTemplateCloneInput.value = newIngredientName;
	const ingredientTemplateCloneButtons = ingredientTemplateClone.querySelectorAll("button");
	ingredientTemplateCloneButtons[0].id = `edit-ingredient-button-${newInputGroupIncrement}`
	ingredientTemplateCloneButtons[1].id = `delete-ingredient-button-${newInputGroupIncrement}`

	// Add input-group to ingredients section in DOM
	ingredientsInputSection.appendChild(ingredientTemplateClone);

	// Add event listeners for the new edit/delete buttons
	addDeleteEventListener(newInputGroupIncrement);
}

function addDeleteEventListener(incrementNumber){
	const deleteIngredientButton = document.getElementById(`delete-ingredient-button-${incrementNumber}`)
	deleteIngredientButton.addEventListener("click", function(event){removeItemFromList(event)})
}

function removeItemFromList(event){
	// Remove parent element (input-group) from DOM
	event.target.parentElement.remove()
}