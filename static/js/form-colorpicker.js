// The original colour picker is made by Sjoerd de Boer and available at https://codepen.io/sjoerddeboer/pen/xxZqBQW
window.addEventListener('DOMContentLoaded', function(event){
	const colorPicker = document.getElementById("color-picker");
	const cupcakeLogo = document.getElementById("cupcake");
	// Get color in database from HTML attribute
	const existingColor = colorPicker.dataset["existingColor"];
	const colorInputs = colorPicker.querySelectorAll("input");
	for (const colorInput of colorInputs){
		// On colour selection input change, change cupcake topping colour to match
		colorInput.addEventListener("change", function(){
			if (this.checked){
				cupcakeLogo.querySelector("#flotty .st0").style.fill = colorInput.value
			}
		})
		// Use queryselector to find that color element and make checked attribute (if match exists)
		if (colorInput.value == `#${existingColor}`){
			colorInput.checked = true;
			cupcakeLogo.querySelector("#flotty .st0").style.fill = colorInput.value
		}
	}

	const colorSelects = document.getElementsByClassName("color-picker-option");
	for (let colorSelect of colorSelects) {
		// Style color select radio inputs based on color attributes
		const colorValue = colorSelect.children[0].value;
		colorSelect.children[1].style.backgroundColor = colorValue;
	};
	})