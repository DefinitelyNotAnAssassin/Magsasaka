const regionInput = document.getElementById('id_region');


const provinceInput = document.getElementById('id_province');
const cityInput = document.getElementById('id_city_municipality');
const barangayInput = document.getElementById('id_barangay');


// check if the Region field is filled (for returns from the server with errors)
if (regionInput.value) {

    fetch(`/auth/getProvinces?region=${regionInput.value}`)
      .then(response => response.json())
      .then(data => {
  
      const provinceSelect = document.getElementById('id_province');
      provinceSelect.innerHTML = '';

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
}


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