function validateForm() {
    var purchasePrice = parseFloat(document.getElementById('purchase_price').value);
    var salePrice = parseFloat(document.getElementById('sale_price').value);
  
    if (salePrice < purchasePrice) {
      alert('O valor de venda deve ser maior ou igual ao valor de compra.');
      return false; // Impede o envio do formulário
    }
  
    return true; // Permite o envio do formulário
  }
  