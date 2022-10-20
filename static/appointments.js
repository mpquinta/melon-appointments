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

    // create URL
    const url = `/results?date=${requestedDate}&start_time_hour=${start_time_hour}&start_time_min=${start_time_min}&start_time_am_pm=${start_time_am_pm}&end_time_hour=${end_time_hour}&end_time_min=${end_time_min}&end_time_am_pm=${end_time_am_pm}`

    // make a fetch request to server
    fetch(url)
        .then((response) => response.json())
        .then((availableAppts) => {
            // call back function should update web page with search results

            const apptResultsContainer = document.querySelector("#search-results")
            apptResultsContainer.innerHTML = "";

            // create the form
            let apptSelectionForm = document.createElement("form");
            apptSelectionForm.setAttribute("method", "post")
            apptSelectionForm.setAttribute("action", "/save-appt")
            
            // make a function that makes a radio button for each available appointment
            for (const appts in availableAppts) {
                // create line break element
                const br = document.createElement("br");

                let radioElement = document.createElement("input")
                radioElement.setAttribute("type", "radio")
                radioElement.setAttribute("id", availableAppts[appts]["appt_start"])
                radioElement.setAttribute("name", "book-appt")
                radioElement.setAttribute("value", availableAppts[appts]["appt_start"])

                let endTime = document.createElement("input")
                endTime.setAttribute("type", "hidden")
                endTime.setAttribute("name", "end-time")
                endTime.setAttribute("value", availableAppts[appts]["appt_end"])
                
                apptSelectionForm.appendChild(endTime);                 
                apptSelectionForm.appendChild(radioElement)

                let labelForRadioElement = document.createElement("label")
                labelForRadioElement.setAttribute("for", availableAppts[appts]["appt_start"])
                labelForRadioElement.innerHTML = ` ${availableAppts[appts]["appt_start"]} - ${availableAppts[appts]["appt_end"]}`
                apptSelectionForm.appendChild(labelForRadioElement)
                apptSelectionForm.appendChild(br)


            }

            let scheduledDate = document.createElement("input")
            scheduledDate.setAttribute("type", "hidden")
            scheduledDate.setAttribute("name", "scheduled-date")
            scheduledDate.setAttribute("value", availableAppts[0]["scheduled_day"])
            apptSelectionForm.appendChild(scheduledDate);

            let formBtn = document.createElement("button");
            formBtn.setAttribute("type", "submit");
            formBtn.innerHTML = "Book Appointment";
            apptSelectionForm.appendChild(formBtn);

            apptResultsContainer.appendChild(apptSelectionForm);
        })
}

searchBtn.addEventListener("click", displaySearchResult);

