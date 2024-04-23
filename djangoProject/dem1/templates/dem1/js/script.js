
document.addEventListener('DOMContentLoaded', main);
function main(event){
    // Getting the rendered url
    const url = document.getElementById("main-table-head").dataset.url;
    console.log(url);
    // Getting clickable headers
    const headers = document.getElementsByClassName("table-header-link");
    // Binding listener to headers
    for (let element of headers){
        element.addEventListener('click', (event) => process_header_click(event, element, url));
        }
    }


async function fetch_table_data(url, to_post){
    // Send a post request to the server and return the response
    // url: String
    // post_data: object

    // Promise to get a response
    const response_promise = await fetch(url,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(to_post)
        }
        );
    // response_promise
    return response_promise;
}

function process_header_click(event, element, url){
    // Getting the title of clicked header
    let title_of_clicked_header = element.dataset["headerCol"];
    // Building the data to post
    const to_post = {"headerCol": title_of_clicked_header};
    // Querying
    fetch_table_data(url, to_post)
        .then((resp) => {
            if (!resp.ok){
                throw new Error("Response is not OK");
            }
            return resp.json();
        })
        .then((data) => console.log(data))
        .catch((error) => console.error("Error during fetching : ", error));
}