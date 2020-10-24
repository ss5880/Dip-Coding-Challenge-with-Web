// IIFE; function is called as soon as the file is loaded
(function(){

    // print to the console (in the browser)
    console.log("hi");

    // get a reference to the 'Send!' button
    let sendBtn = document.querySelector("#sendFile");

    // get a reference to the file selector
    let fileInput = document.querySelector("#fileSelect");

    // add an onclick event to the send button
    sendBtn.onclick = (e) => {

        // get the file from the file selector
        let file = fileInput.files[0];

        // create a data table that can be sent to the server
        let formData = new FormData();
    
        // add the file to the data table
        formData.append("file", file);
    
        // send a HTTP POST request to the server
        //    v URL v  v Request Type v v Data To Send v
        fetch('/send', {method:'post', body: formData}).then(res=>{
            // .then() is basically a callback function (it's called a "promise")

            // convert the data received from the server to json (using another promise)
            // (data doesn't have to be json, it could be a string or a file depending on what you want to do with it)
            res.json().then(data=>{

                // print the data to the console (to see if everything worked)
                console.log(data);

                // get a reference to the "Results" section on the webpage
                let result = document.querySelector("#result");

                // add the data inside the json file to "Results"
                for(let i = 0; i < data.data.length; i++){
                    
                    // creates a "p" (paragraph) element
                    let child = document.createElement('p');

                    // add the text to the child
                    child.innerText = data.data[i];

                    // add the child to the "Results" section
                    result.appendChild(child);
                }

                // make a download button
                let dlBtn = document.createElement('button');

                // set the text on the button
                dlBtn.innerText = "Download!"

                // add button to the webpage
                result.appendChild(dlBtn);

                // add event for clicking the button, downloads the file
                dlBtn.onclick = (e) => {
                    let hiddenElement = document.createElement('a');
                    hiddenElement.href = 'data:text/json;charset=utf-8,' + encodeURI(JSON.stringify(data));
                    hiddenElement.target = '_blank';
                    hiddenElement.download = 'result.json';
                    hiddenElement.click();
                }
            });
        });
    };
    
})();