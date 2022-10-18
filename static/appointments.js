'use strict';

// [Getting search results

// makea function that creates radio selections
function radioOptions(apptTime) {
    const radioElement = `
        <input type="radio" value="test" value="test">
        <label for="test">Test</label>
    `
    return radioElement
}

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
        .then((availableAppts) => {
            // call back function should update web page with search results
            console.log(typeof(availableAppts))

            const apptResultsContainer = document.querySelector("#search-results")
            apptResultsContainer.innerHTML = "";

            // create divs for the form
            const apptSelectionForm = document.createElement("form");
            apptSelectionForm.setAttribute("id", "select-appt-form")

            // make a function that makes a radio button for each available appointment
            for (const appts in availableAppts) {
                // console.log(availableAppts[appts])

                const radioElement = document.createElement("input")
                radioElement.setAttribute("type", "radio")
                radioElement.setAttribute("id", availableAppts[appts]["appt_start"])
                radioElement.setAttribute("name", "book-appt")
                radioElement.setAttribute("value", availableAppts[appts]["appt_start"])                 
                apptSelectionForm.insertAdjacentElement("beforeend", radioElement)

                const labelForRadioElement = document.createElement("label")
                labelForRadioElement.setAttribute("for", availableAppts[appts]["appt_start"])
                labelForRadioElement.innerHTML = `${availableAppts["appt_start"]} - ${availableAppts["appt_end"]}`
                apptSelectionForm.insertAdjacentElement("beforeend", labelForRadioElement)
            }

            const formBtn = document.createElement("button");
            formBtn.setAttribute("type", "submit");
            formBtn.innerHTML = "Book Appointment";
            apptSelectionForm.insertAdjacentElement("beforeend", formBtn);

            apptResultsContainer.innerHTML = apptSelectionForm;
        })
}

searchBtn.addEventListener("click", displaySearchResult);

