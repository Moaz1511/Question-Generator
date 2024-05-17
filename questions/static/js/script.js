document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("quiz-form");
    const resultDiv = document.getElementById("result");

    if (form) {
        form.addEventListener("submit", function(event) {
            event.preventDefault();
            const formData = new FormData(form);
            const selectedOption = formData.get("answer");

            if (selectedOption === correctAnswer) {
                resultDiv.textContent = "Correct!";
                resultDiv.style.color = "green";
            } else {
                resultDiv.textContent = "Incorrect. Try again.";
                resultDiv.style.color = "red";
            }

            MathJax.typeset();  // Re-render MathJax expressions after form submission
        });
    }
});
