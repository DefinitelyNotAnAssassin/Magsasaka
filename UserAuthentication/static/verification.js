const validateForm = (e) => {
    const password = document.getElementById('id_password').value;
    const contact_number = document.getElementById('id_contact_number').value;

    // check if all fields are filled
    var isValid = true;
    const fields = document.querySelectorAll('input');
    for (let i = 0; i < fields.length - 3; i++) {
        if (fields[i].value === '' && fields[i].name != "precinct_number" && fields[i].name != "fb_messenger_account") {
            fields[i].previousElementSibling.style.color = 'red';
            isValid = false;
        } else {
            fields[i].previousElementSibling.style.color = 'black';
        }
    }

    const phoneNumber = document.getElementById('id_contact_number').value;
    const phoneNumberRegex = /^(09|\+639)\d{9}$/;

    if (isValid === false) {
        alert('Please fill in all fields');
        e.preventDefault();
    } else if (!phoneNumberRegex.test(phoneNumber)) {
        alert('Invalid phone number. Please enter a valid 11-digit phone number starting with +63 or 09.');
        contact_number.previousElementSibling.style.color = 'red';
        e.preventDefault();
    } else {
        return true;
    }
}
