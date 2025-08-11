

<!DOCTYPE html>
<html>
<head>
  <title>Eligibility Check</title>
</head>
<body>
  <h2>Eligibility Result:</h2>
  <p id="result"></p>

  <script>
    function checkEligibility(name, age) {
      let message = "";

      if (age >= 18) {
        message = `${name} is eligible to vote`;
      } else {
        message = `${name} is not eligible to vote`;
      }

      // Show message on the page
      document.getElementById("result").textContent = message;
    }

    // Call the function
    checkEligibility("Ravi", 20);
  </script>
</body>
</html>

