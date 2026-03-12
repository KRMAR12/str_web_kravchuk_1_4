var input = document.getElementById(".btn");

input.addEventListener("keypress", function(event) {
  // If the user presses the "Enter" key on the keyboard
  if (event.key === "Enter") {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById(".btn").click();
  }
});

document.getElementById("focus").addEventListener("click", () => {
  document.getElementById("search_country").focus();
})