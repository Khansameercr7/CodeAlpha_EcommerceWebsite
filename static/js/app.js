/* ==============================================
   E-commerce Store - JavaScript
   ============================================== */

// Update cart quantity
function updateQuantity(cartId, change) {
    const input = document.getElementById(`quantity-${cartId}`);
    let newValue = parseInt(input.value) + change;
    
    if (newValue < 1) {
        newValue = 1;
    }
    
    input.value = newValue;
    updateCartTotal();
}

// Update cart total when quantity changes
function updateCartTotal() {
    const quantities = document.querySelectorAll('[id^="quantity-"]');
    const prices = document.querySelectorAll('[id^="price-"]');
    
    let total = 0;
    
    quantities.forEach((qty, index) => {
        const quantity = parseInt(qty.value);
        const price = parseFloat(prices[index].getAttribute('data-price'));
        total += quantity * price;
    });
    
    const totalElement = document.getElementById('cart-total');
    if (totalElement) {
        totalElement.textContent = '$' + total.toFixed(2);
    }
}

// Show alert message
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.setAttribute('role', 'alert');
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="close" data-dismiss="alert">
            <span>&times;</span>
        </button>
    `;
    
    const container = document.querySelector('.container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);
        
        // Auto-dismiss after 3 seconds
        setTimeout(() => {
            alertDiv.remove();
        }, 3000);
    }
}

// Confirm delete action
function confirmDelete(message = 'Are you sure?') {
    return confirm(message);
}

// Search form validation
function validateSearch() {
    const searchInput = document.getElementById('search-input');
    if (searchInput && searchInput.value.trim() === '') {
        alert('Please enter a search term');
        return false;
    }
    return true;
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('E-commerce store loaded');
    
    // Auto-dismiss django messages
    setTimeout(() => {
        const messages = document.querySelectorAll('.alert');
        messages.forEach(msg => {
            msg.style.transition = 'opacity 0.5s';
            msg.style.opacity = '0';
            setTimeout(() => msg.remove(), 500);
        });
    }, 3000);
});