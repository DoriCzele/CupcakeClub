window.addEventListener("DOMContentLoaded", event => {
	// Populate existing ingredient/instruction fields
	let existingIngredients = document.getElementById("ingredients-input").dataset["existingIngredients"];
	existingIngredients = existingIngredients.split(",")
	for (const ingredient of existingIngredients){
		addIngredientToList(ingredient);
	}
	let existingInstructions = document.getElementById("instructions-input").dataset["existingInstructions"];
	existingInstructions = existingInstructions.split(",")
	for (const instruction of existingInstructions){
		addInstructionToList(instruction);
	}

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
	const instructionInputField = document.getElementById("instruction-field")
	const addInstructionButton = document.getElementById("add-instruction")
	instructionInputField.addEventListener("keypress", event => {
		if (event.key == "Enter"){
			event.preventDefault()
			if (instructionInputField.value !== ""){
			addInstructionToList(instructionInputField.value);
			}
		}
	})
	addInstructionButton.addEventListener("click", function(){
		if (instructionInputField.value !== ""){
			addInstructionToList(instructionInputField.value)
		}
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
	addDeleteIngredientEventListener(newInputGroupIncrement);
	addEditIngredientEventListener(newInputGroupIncrement);
}

function addDeleteIngredientEventListener(incrementNumber){
	const deleteIngredientButton = document.getElementById(`delete-ingredient-button-${incrementNumber}`)
	deleteIngredientButton.addEventListener("click", function(event){removeItemFromList(event)})
}

function removeItemFromList(event){
	// Remove parent element (input-group) from DOM
	event.target.parentElement.remove()
}

function addEditIngredientEventListener(incrementNumber){
	const editIngredientButton = document.getElementById(`edit-ingredient-button-${incrementNumber}`)
	editIngredientButton.addEventListener("click", function(event){makeInputFieldWritable(event)})
}

function makeInputFieldWritable(event){
	// Remove the readonly attribute from related input field
	event.target.parentElement.querySelector("input").readOnly = false;
}

function addInstructionToList(newInstructionName){
	// https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template
	const instructionsInputSection = document.getElementById("instructions-input");
	const inputGroups = instructionsInputSection.querySelectorAll(".input-group");
	const lastInputGroup = inputGroups[inputGroups.length-1];
	// Increment the last instruction ID value if it exists
	let newInputGroupIncrement = 0;
	if (lastInputGroup){
		newInputGroupIncrement = parseInt(lastInputGroup.querySelector("input").dataset.increment) + 1;
	}

	// Get input-group template and clone it
	const instructionTemplate = document.getElementById("instruction-template");
	const instructionTemplateClone = instructionTemplate.content.cloneNode(true);
	const instructionTemplateCloneInput = instructionTemplateClone.querySelector("input");
	instructionTemplateCloneInput.name = `instruction${newInputGroupIncrement}`;
	instructionTemplateCloneInput.dataset.increment = newInputGroupIncrement;
	instructionTemplateCloneInput.value = newInstructionName;
	const instructionTemplateCloneButtons = instructionTemplateClone.querySelectorAll("button");
	instructionTemplateCloneButtons[0].id = `edit-instruction-button-${newInputGroupIncrement}`
	instructionTemplateCloneButtons[1].id = `delete-instruction-button-${newInputGroupIncrement}`

	// Add input-group to instructions section in DOM
	instructionsInputSection.appendChild(instructionTemplateClone);

	// Add event listeners for the new edit/delete buttons
	addDeleteInstructionEventListener(newInputGroupIncrement);
	addEditInstructionEventListener(newInputGroupIncrement);
}

function addDeleteInstructionEventListener(incrementNumber){
	const deleteInstructionButton = document.getElementById(`delete-instruction-button-${incrementNumber}`)
	deleteInstructionButton.addEventListener("click", function(event){removeItemFromList(event)})
}

function addEditInstructionEventListener(incrementNumber){
	const editInstructionButton = document.getElementById(`edit-instruction-button-${incrementNumber}`)
	editInstructionButton.addEventListener("click", function(event){makeInputFieldWritable(event)})
}