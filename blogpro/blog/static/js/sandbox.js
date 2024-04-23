'use strict';

const navbarCollapse = document.querySelector('.navbar-collapse');
const navbarToggleButton = document.querySelector('.navbar-toggler');

navbarToggleButton.addEventListener('click', ()=>
	{
		navbarCollapse.classList.toggle('show');
		navbarToggleButton.classList.toggle('cross');
	});