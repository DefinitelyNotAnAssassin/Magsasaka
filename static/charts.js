
  const ctx = document.getElementById("myChart")

  fetch("/api/barangay_data")
    .then((response) => response.json())
    .then((data) => {
      const jsonData = JSON.parse(data)
      const labels = Object.keys(jsonData)
      const counts = Object.values(jsonData)
      console.log(data)

      new Chart(ctx, {
        type: "bar",
        data: {
          labels: labels,

          datasets: [
            {
              label: "# of Registered Members",
              data: counts,
              borderWidth: 1,
            },
          ],
        },
        options: {
          resonsive: true,
          maintainAspectRatio: false,
          plugins: {
            title: {
              display: true,
              text: "Registered BH Members",
            },
          },
        },
      })
    })

  // Age Chart

  const ageChart = document.getElementById("ageChart")

  fetch("/api/age_data")
    .then((response) => response.json())
    .then((data) => {
      const jsonData = JSON.parse(data)
      const labels = Object.keys(jsonData)
      const counts = Object.values(jsonData)
      console.log(data)

      new Chart(ageChart, {
        type: "pie",
        data: {
          labels: labels,

          datasets: [
            {
              label: "Age Group",
              data: counts,
              borderWidth: 1,
            },
          ],
        },
        options: {
          resonsive: true,
          maintainAspectRatio: false,
          plugins: {
            title: {
              display: true,
              text: "Demographics of Registered BH Members by Age",
            },
          },
        },
      })
    })





    
  const familyVotersChart = document.getElementById("familyVotersChart")

  fetch("/api/family_voters_data")
    .then((response) => response.json())
    .then((data) => {
      const jsonData = JSON.parse(data)
      const labels = Object.keys(jsonData)
      const counts = Object.values(jsonData)
      console.log(data)

      new Chart(ageChart, {
        type: "pie",
        data: {
          labels: labels,

          datasets: [
            {
              label: "Age Group",
              data: counts,
              borderWidth: 1,
            },
          ],
        },
        options: {
          resonsive: true,
          maintainAspectRatio: false,
          plugins: {
            title: {
              display: true,
              text: "Family Voters Count of Registered BH Members",
            },
          },
        },
      })
    })
