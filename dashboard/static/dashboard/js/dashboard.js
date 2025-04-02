document.addEventListener("DOMContentLoaded", function () {
  // Dummy data for book counts
  let bookCount = 100;
  let borrowedCount = 25;
  let returnedCount = 75;

  // Display initial counts
  function updateCounts() {
      document.getElementById("book-count").textContent = bookCount;
      document.getElementById("borrowed-count").textContent = borrowedCount;
      document.getElementById("returned-count").textContent = returnedCount;
  }

  updateCounts();

  // Handle Issue Book button click
  document.querySelector(".issue-btn").addEventListener("click", function () {
      if (bookCount > 0) {
          bookCount--;
          borrowedCount++;
          updateCounts();
          alert("A book has been issued successfully!");
      } else {
          alert("No more books available to issue.");
      }
  });

  // Logout button functionality
  document.querySelector(".logout-btn").addEventListener("click", function () {
      if (confirm("Are you sure you want to log out?")) {
          window.location.href = "login.html"; // Redirect to login page
      }
  });

  // Home button functionality (reload dashboard)
  document.querySelector(".home-btn").addEventListener("click", function () {
      location.reload(); // Refreshes the page to show the dashboard again
  });
});
