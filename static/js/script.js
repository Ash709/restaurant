// Mobile menu toggle
const bar = document.querySelector('.bar');
const navList = document.querySelector('nav ul');

if (bar && navList) {
  bar.addEventListener('click', () => {
    navList.classList.toggle('show');
  });
}
// placeholder 
