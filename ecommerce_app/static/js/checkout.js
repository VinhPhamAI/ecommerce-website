function changeQuantity(button, amount) {
    let quantityInput = button.parentNode.querySelector('.itemQuantity');
    let currentQuantity = parseInt(quantityInput.value);
    let newQuantity = currentQuantity + amount;

    // Ensure quantity is not less than 1
    if (newQuantity >= 1) {
      quantityInput.value = newQuantity;
    }
  }