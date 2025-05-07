// Wait for the DOM to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function () {

  // Get the elements for options, product image, and quantity input
  const optionSelect = document.getElementById('optionSelect');
  const productImage = document.getElementById('productImage');

  // If options and product image elements exist, set the default image from the first option (if available)
  if (optionSelect && productImage) {
    const firstOption = optionSelect.querySelector('option:first-child');

    // If the first option has a valid image URL, update the product image
    if (firstOption && firstOption.getAttribute('data-image-url')) {
      productImage.src = firstOption.getAttribute('data-image-url');
    }

    // Add event listeners to update both the image and the price whenever the selected option changes
    optionSelect.addEventListener('change', updateImage);
    optionSelect.addEventListener('change', updatePrice);
  }

  // Add an event listener to update the price whenever the quantity is changed
  const quantityInput = document.getElementById('quantity');
  if (quantityInput) {
    quantityInput.addEventListener('input', updatePrice);
  }

  // Initial price and image update on page load
  updatePrice();
  updateImage();
});


// Function to update the displayed product image based on the selected option
function updateImage() {
  // Get the selected option and its associated image URL
  const optionSelect = document.getElementById('optionSelect');
  const selectedOption = optionSelect.options[optionSelect.selectedIndex];
  const imageUrl = selectedOption.getAttribute('data-image-url');
  const productImage = document.getElementById('productImage');
  
  // If product image and image URL exist, update the product image source
  if (productImage && imageUrl) {
    productImage.src = imageUrl;
  }
}


// This function calculates and updates the total price
// on the product page based on the selected options and quantity.
// It supports both products with options and products without options.
//
// Assumptions:
// - Option prices are valid floats.
// - The product form has a `data-base-price` attribute for base pricing.

function updatePrice() {
  // Get the selected quantity, defaulting to 1 if invalid
  const quantity = parseInt(document.getElementById('quantity').value) || 1;

  // Get the option select element and total price element
  const optionSelect = document.getElementById('optionSelect');
  const totalPriceEl = document.getElementById('totalPrice');

  let price = 0;

  // Check if options exist, and use the selected option's price
  if (optionSelect) {
      const selectedOption = optionSelect.options[optionSelect.selectedIndex];
      price = parseFloat(selectedOption.value);
  } else {
      // If no options exist, use the base product price
      price = parseFloat(document.getElementById('productForm').dataset.basePrice);
  }

  // Calculate the total price based on selected quantity
  const total = price * quantity;

  // Update the displayed total price
  totalPriceEl.textContent = total.toFixed(2);
}














  