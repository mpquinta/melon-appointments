'use strict';

// [Getting search results]
// get information from the form - trigger response
const searchBtn = document.querySelector("#search-btn");

function displaySearchResult(evt) {
    evt.preventDefault(); 

    const url = `/results?date=${date}?&start-time-hour=${start-time-hour}&start-time-minute=${start-time-minute}&start-am-pm=${start-am-pm}&end-time-hour=${end-time-hour}&end-time-minute=${end-time-minute}&end-am-pm=${end-am-pm}`

    // make a fetch request to server
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            // call back function should update web page with search results
            
        })
}

