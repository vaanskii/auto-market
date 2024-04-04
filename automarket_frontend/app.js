document.addEventListener('DOMContentLoaded', () => {
    // dropdown menu
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle')
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const dropdownMenu = toggle.nextElementSibling

            if(dropdownMenu.classList.contains('hidden')){
                document.querySelectorAll('.dropdown-menu').forEach(menu => {
                    menu.classList.add('hidden')
                })
                dropdownMenu.classList.remove('hidden')
            }else {
                dropdownMenu.classList.add('hidden')
            }
        })
    })
    // clicking outside to close opened dropdown menu
    window.addEventListener('click', (event) => {
        if(!event.target.matches('.dropdown-toggle')) {
            document.querySelectorAll('.dropdown-menu').forEach(menu => {
                if(!menu.contains(event.target)) {
                    menu.classList.add('hidden')
                }
            })
        }
    })

    // mobile menu toggle 
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('.navigation-menu');

    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden')
    })
})