// Show the modal when the 'Send Feedback' button is clicked
document.getElementById('send-feedback-button').addEventListener('click', function() {
    document.getElementById('feedback-method-modal').style.display = 'block';
    document.getElementById('modal-overlay').style.display = 'block';
});

// Close modal when clicking overlay
document.getElementById('modal-overlay').addEventListener('click', function() {
    document.getElementById('feedback-method-modal').style.display = 'none';
    document.getElementById('modal-overlay').style.display = 'none';
});

// Handle the feedback method submission
document.getElementById('proceed-feedback-button').addEventListener('click', function() {
    var selectedMethod = document.querySelector('input[name="send_method"]:checked');
    
    if (!selectedMethod) {
        alert('Please select a feedback method');
        return;
    }

    var sendMethod = selectedMethod.value;

    if (sendMethod === 'email') {
        // Submit the form for email processing
        document.getElementById('feedback-form').submit();
    } else if (sendMethod === 'whatsapp') {
        // Redirect to WhatsApp with a pre-filled message
        var message = "I would like to give feedback: ";
        var phone = "+233557468828";
        var url = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
        window.location.href = url;
    }
});
