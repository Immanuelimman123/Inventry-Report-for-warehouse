// Example: confirm before submitting forms
document.addEventListener("DOMContentLoaded", function() {
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", function(e) {
            if (!confirm("Are you sure you want to submit this form?")) {
                e.preventDefault();
            }
        });
    });
});

// Example: auto-focus the first input in forms
forms.forEach(form => {
    const firstInput = form.querySelector("input, select, textarea");
    if (firstInput) firstInput.focus();
});

// You can add more JS later, e.g., dynamic table sorting, filtering, etc.
