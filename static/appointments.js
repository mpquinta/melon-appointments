'use strict';

// [Getting search results]
// get information from the form - trigger response
const searchBtn = document.querySelector("#search-btn");

function displaySearchResult(evt) {
    evt.preventDefault(); 

    // save user inputs from form
    const requestedDate = document.querySelector("#date").value;
    const start_time_hour = document.querySelector("#start-time-hour").value;
    const start_time_min = document.querySelector("#start-time-minute").value;
    const start_time_am_pm = document.querySelector("#start-am-pm").value;
    const end_time_hour = document.querySelector("#end-time-hour").value;
    const end_time_min = document.querySelector("#end-time-minute").value;
    const end_time_am_pm = document.querySelector("#end-am-pm").value;

    console.log(start_time_min, start_time_am_pm)

    // create URL
    const url = `/results?date=${requestedDate}&start_time_hour=${start_time_hour}&start_time_min=${start_time_min}&start_time_am_pm=${start_time_am_pm}&end_time_hour=${end_time_hour}&end_time_min=${end_time_min}&end_time_am_pm=${end_time_am_pm}`

    // make a fetch request to server
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            // call back function should update web page with search results
            console.log(data)
        })
}

searchBtn.addEventListener("click", displaySearchResult);

