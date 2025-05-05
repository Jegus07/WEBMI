document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function () {
        const btn = form.querySelector('button');
        btn.disabled = true;
        btn.innerText = 'Envoi en cours...';
    });
});
