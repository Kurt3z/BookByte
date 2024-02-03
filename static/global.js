'use strict';

const btnMenu = document.querySelector('#hamburger-icon');
const btnCloseMenu = document.querySelector('#close-mobile-nav');
const responsiveMenu = document.querySelector('.mobile-nav');

btnMenu.addEventListener('click', function () {
  responsiveMenu.classList.add('show');
});

btnCloseMenu.addEventListener('click', function () {
  responsiveMenu.classList.remove('show');
});