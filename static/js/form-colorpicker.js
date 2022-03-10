// The original colour picker is made by Sjoerd de Boer and available at https://codepen.io/sjoerddeboer/pen/xxZqBQW
window.addEventListener('DOMContentLoaded', event => {
	const colorSelects = document.getElementsByClassName("color-picker-option");
	for (let colorSelect of colorSelects) {
		const colorValue = colorSelect.children[0].value;
		colorSelect.children[1].style.backgroundColor = colorValue;
	};
	})