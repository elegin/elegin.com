function toggleDiv() {
  const div = document.getElementById('Ai');
  if (div.style.display === 'none' || div.style.display === '') {
    div.style.display = 'block'; // Show the div
  } else {
    div.style.display = 'none'; // Hide the div
  }
}
