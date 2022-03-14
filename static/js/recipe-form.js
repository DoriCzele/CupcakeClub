function populateExistingRecipeAttributes(existingValues, attributeType){
	if(existingValues){
		// Split string into array of strings
		existingValues = existingValues.split(",");
		for (const existingValue of existingValues){
			addEntryToList(existingValue, attributeType);
		}
	}
}

function compareEntryToRegex(inputElement, inputPrompt, attributeType){
	const validInputRegex = /^[A-Za-z0-9 ]*[A-Za-z0-9][A-Za-z0-9 ]*$/;
	if (validInputRegex.test(inputElement.value)){
		// Ensure input prompt is not displayed on valid entry
		inputPrompt.style.display = "none";
		addEntryToList(inputElement.value, attributeType)
			// Reset the original input field
		inputElement.value = ""
	} else {
		inputPrompt.style.display = "block";
	}
}

function addInputEventListeners(attributeType){
	const inputField = document.getElementById(`${attributeType}-field`);
	const inputPrompt = document.getElementById(`${attributeType}-input-prompt`);
	const addAttributeButton = document.getElementById(`add-${attributeType}`)
	// On individual entry submit, check if it matches the allowed regex characters
	inputField.addEventListener("keypress", function(event){
		if (event.key == "Enter"){
			event.preventDefault()
			compareEntryToRegex(inputField, inputPrompt, attributeType);
		}
	})
	addAttributeButton.addEventListener("click", function(){
		compareEntryToRegex(inputField, inputPrompt, attributeType);
	})
}

// Wait for DOM content to load before applying event listeners
window.addEventListener("DOMContentLoaded", function(){
	// Populate existing ingredient/instruction fields
	let existingIngredients = document.getElementById("ingredient-input-section").dataset["existingIngredients"];
	populateExistingRecipeAttributes(existingIngredients, "ingredient");
	let existingInstructions = document.getElementById("instruction-input-section").dataset["existingInstructions"];
	populateExistingRecipeAttributes(existingInstructions, "instruction");

	// Allow ingredient to be added either with button or "Enter" key, validated with regex
	addInputEventListeners("ingredient");
	addInputEventListeners("instruction");
});

function addEntryToList(newValue, attributeType){
	const inputSection = document.getElementById(`${attributeType}-input-section`)
	const inputGroups = inputSection.querySelectorAll(".input-group");
	
	// Increment the last input ID value if it exists
	const lastInputGroup = inputGroups[inputGroups.length-1]
	let newInputGroupIncrement = 0;
	if (lastInputGroup){
		newInputGroupIncrement = parseInt(lastInputGroup.querySelector("input").dataset.increment) + 1;
	}

	// Get input group template and clone it
	const htmlTemplate = document.getElementById(`${attributeType}-template`);
	const htmlTemplateClone = htmlTemplate.content.cloneNode(true);
	const htmlTemplateCloneInput = htmlTemplateClone.querySelector("input");
	htmlTemplateCloneInput.name = `${attributeType}${newInputGroupIncrement}`;
	htmlTemplateCloneInput.dataset.increment = newInputGroupIncrement;
	htmlTemplateCloneInput.value = newValue;
	const htmlTemplateCloneButtons = htmlTemplateClone.querySelectorAll("button");
	htmlTemplateCloneButtons[0].id = `edit-${attributeType}-button-${newInputGroupIncrement}`
	htmlTemplateCloneButtons[1].id = `delete-${attributeType}-button-${newInputGroupIncrement}`

	// Add input-group to inputs section in DOM
	inputSection.appendChild(htmlTemplateClone);

	// Add event listeners for the new edit/delete buttons
	const editAttributeButton = document.getElementById(`edit-${attributeType}-button-${newInputGroupIncrement}`)
	editAttributeButton.addEventListener("click", function(event){makeInputFieldWritable(event)})
	const deleteAttributeButton = document.getElementById(`delete-${attributeType}-button-${newInputGroupIncrement}`)
	deleteAttributeButton.addEventListener("click", function(event){removeItemFromList(event)})
}

function removeItemFromList(event){
	// Remove direct parent input group from DOM
	event.target.parentElement.remove()
}

function makeInputFieldWritable(event){
	// Remove the readonly attribute from related input field
	event.target.parentElement.querySelector("input").readOnly = false;
}
