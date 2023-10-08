// Получите все гиперссылки в шапке
const links = document.querySelectorAll('.bb');

// Добавьте обработчик события для каждой гиперссылки
links.forEach((link) => {
    link.addEventListener('mouseenter', () => {
        // При наведении на гиперссылку, остановите анимацию у всех гиперссылок
        links.forEach((otherLink) => {
            otherLink.style.animationPlayState = 'paused';
        });
    });

    link.addEventListener('mouseleave', () => {
        // При убирании курсора с гиперссылки, начните анимацию заново у всех гиперссылок
        links.forEach((otherLink) => {
            otherLink.style.animationPlayState = 'running';
        });
    });
});
