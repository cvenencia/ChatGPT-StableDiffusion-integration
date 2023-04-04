const form = document.querySelector('form');
const spinner = document.querySelector('.spinner');
const button = document.querySelector('[type="submit"]');
const textarea = document.querySelector('textarea');

form.addEventListener('submit', e => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    spinner.classList.remove('hide');
    button.classList.add('hide');
    textarea.disabled = true;
    fetch('/result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.text())
        .then(html => {
            document.open();
            document.write(html);
            document.close();
        });
});
