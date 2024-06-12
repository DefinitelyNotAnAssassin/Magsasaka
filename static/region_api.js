const regionInput = document.getElementById('id_region');

regionInput.addEventListener('change', (e) => {
  const region = regionInput.value;

  fetch(`/auth/getProvinces?region=${region}`)
    .then(response => response.json())
    .then(data => {

    const provinceSelect = document.getElementById('id_province');
    provinceSelect.innerHTML = '';
    // Add selected disabled default option
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.text = 'Select Province';
    defaultOption.disabled = true;
    defaultOption.selected = true;
    provinceSelect.appendChild(defaultOption);
    data.forEach(province => {
      const option = document.createElement('option');
      option.value = province.name;
      option.text = province.name;
      provinceSelect.appendChild(option);
    });
    })
    .catch(error => {
    console.error('Error:', error);
    });
});

const provinceInput = document.getElementById('id_province');
const cityInput = document.getElementById('id_city_municipality');
const barangayInput = document.getElementById('id_barangay');

const usernameInput = document.getElementById('id_username');  // replace 'id_username' with the actual ID of your username field

// debounce the checkUsername function, so it's only called 300ms after the user stops typing
const debouncedCheckUsername = _.debounce(checkUsername, 500);

usernameInput.addEventListener('input', debouncedCheckUsername);

function checkUsername() {
const username = document.getElementById('id_username').value

fetch('/auth/checkUsername', {  // replace '/check_username/' with the actual URL of your check_username view
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': getCookie('csrftoken')  // getCookie is a function to get the CSRF token. See note below.
  },
  body: JSON.stringify({username: username})
})
.then(response => response.json())
.then(data => {
  console.log(data.username_exists)
  if (data.username_exists == "true") {
    // username exists, do something
    alert('Username already exists. Please choose another username.');
    usernameInput.value = '';
  } else {
    // username does not exist, do something else
  }
})
.catch(error => {
  console.error('Error:', error);
});
}

// Function to get a cookie by name. This is used to get the CSRF token.
function getCookie(name) {
let cookieValue = null;
if (document.cookie && document.cookie !== '') {
  const cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.substring(0, name.length + 1) === (name + '=')) {
      cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
      break;
    }
  }
}
return cookieValue;
}


provinceInput.addEventListener('change', (e) => {
  const province = provinceInput.value;

  fetch(`/auth/getCities?province=${province}`)
  .then(response => response.json())
  .then(data => {

    cityInput.innerHTML = '';
    // Add selected disabled default option
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.text = 'Select City/Municipality';
    defaultOption.disabled = true;
    defaultOption.selected = true;
    cityInput.appendChild(defaultOption);
    data.forEach(city => {
    const option = document.createElement('option');
    option.value = city.name;
    option.text = city.name;
    cityInput.appendChild(option);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });
});

cityInput.addEventListener('change', (e) => {
  const city = cityInput.value;

  fetch(`/auth/getBarangays?city=${city}`)
  .then(response => response.json())
  .then(data => {

    barangayInput.innerHTML = '';
    // Add selected disabled default option
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.text = 'Select Barangay';
    defaultOption.disabled = true;
    defaultOption.selected = true;
    barangayInput.appendChild(defaultOption);
    data.forEach(barangay => {
    const option = document.createElement('option');
    option.value = barangay.name;
    option.text = barangay.name;
    barangayInput.appendChild(option);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });
});