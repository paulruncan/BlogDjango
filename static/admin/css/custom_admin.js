// static/admin/js/custom_admin.js

document.addEventListener('DOMContentLoaded', function () {
    console.log('Custom JavaScript loaded in Django Admin!');

    // Example: Highlight all input fields on focus
    const inputs = document.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.style.borderColor = '#4CAF50';
        });
        input.addEventListener('blur', () => {
            input.style.borderColor = '';
        });
    });
});
