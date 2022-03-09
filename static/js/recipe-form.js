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

	// Get input-group template and clone it
	const ingredientTemplate = document.getElementById("ingredient-template");
	const ingredientTemplateClone = ingredientTemplate.content.cloneNode(true);
	ingredientTemplateClone.querySelector("input").value = newIngredientName;

	// Add input-group to ingredients section in DOM
	ingredientsInputSection.appendChild(ingredientTemplateClone);

}