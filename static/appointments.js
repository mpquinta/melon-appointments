'use strict';

// [Getting search results]
// get information from the form - trigger response
const searchBtn = document.querySelector("#search-btn");

function displaySearchResult(evt) {
    evt.preventDefault(); 

    const url = `/results?date=${date}?&start-time=${start-time}&end-time=${end-time}`

    // make a fetch request to server
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            // call back function should update web page with search results
            
        })
}

