document.addEventListener('DOMContentLoaded', function () {
  // Set the default image to the first available option
  const firstOption = document.querySelector('#optionSelect option:first-child');
  const defaultImageUrl = firstOption.getAttribute('data-image-url');
  const productImage = document.getElementById('productImage');
  
  if (productImage) {
    productImage.src = defaultImageUrl;
  }

  // Add event listener to the option select dropdown
  const optionSelect = document.getElementById('optionSelect');
  optionSelect.addEventListener('change', updateImage);
});

function updateImage() {
  // Get the selected option's image URL
  const optionSelect = document.getElementById('optionSelect');
  const selectedOption = optionSelect.options[optionSelect.selectedIndex];
  const imageUrl = selectedOption.getAttribute('data-image-url');
  
  // Update the product image src
  const productImage = document.getElementById('productImage');
  if (productImage) {
    productImage.src = imageUrl;
  }
}


// JavaScript for price update
function updatePrice() {
  // Get the base price from Django context
  const basePrice = parseFloat("{{ product.price }}");  // Parse to float for arithmetic
  
  // Get the selected option and its price
  const optionSelect = document.getElementById('optionSelect');
  const selectedOption = optionSelect.options[optionSelect.selectedIndex];
  const selectedOptionPrice = parseFloat(selectedOption.value);  // Price of selected option
  
  // Get the selected quantity
  const quantity = parseInt(document.getElementById('quantity').value);
  
  // Calculate final price (base price + selected option price)
  const finalPrice = basePrice + selectedOptionPrice;
  
  // Update the price display (multiply final price by quantity)
  const totalPriceElement = document.getElementById('totalPrice');
  totalPriceElement.textContent = `£${(finalPrice * quantity).toFixed(2)}`;  // Format as currency

// Call updatePrice when the page loads to show the correct price
window.onload = function() {
  updatePrice();  // Update price on page load
};
}



