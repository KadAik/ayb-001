const headers = ["id", "Age", "Sex", "BP", "Cholesterol", "Na_to_K", "Drug"];
document.addEventListener('DOMContentLoaded', main);
function main(event) {
    table_building(true);
    // Getting the rendered url
    const url = document.getElementById("index-page").value;
    console.log(url + " => Threw from function main");
    // Cause of event bubbling, event delegation will be used to handle header click as
    // in case of table dynamic changing, event binding to each clickable header persists.
    // On each filtering, the table is entirely rebuilt so the event will be attached to the
    // stable table parent : div in this case
    const table_stable_parent = document.querySelector("#table-content");
    // Listening of click on table headers :
    table_stable_parent.addEventListener('click', (event) => {
            if (event.target.nodeName === 'TH') {
                process_header_click(event, event.target, url)
            }
        }
    );
}
    // // Getting clickable headers
    // const head_elements = document.getElementsByClassName("table-header-link");
    // // Binding listener to headers
    // for (let element of head_elements){
    //     element.addEventListener('click', (event) => process_header_click(event, element, url));
    //     }
    // }


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
        .then((data) => table_building(false, data))
        .catch((error) => console.error("Error during fetching : ", error));
}

function table_builder(table, headers){

    //table head building
    // Getting the url value for th columns (index page)
    const url_link = document.getElementById("index-page").value;
    console.log("URL value : " + url_link + " => threw from function table_builder");
    let thead_builder = `<thead id="main-table-head" data-url=${url_link}> <tr>`;
    for (let col of headers){
        thead_builder += `<th class="table-header-link" data-header-col=${col}>` +
            col + "</th>";
    }
    thead_builder += "</thead>";

    //table body building
    let tbody_builder = "<tbody>";
    for (let element of table){
        tbody_builder += "<tr>";
            for (let col of headers){
                tbody_builder += "<td>" + element[col] + "</td>";
            }
        tbody_builder += "</tr>";
    }
    tbody_builder += "</tbody>"
    // Building the table block
    const table_built = "<table>" +
                                thead_builder +
                                tbody_builder +
                                "</table>";
    return table_built;
}

function table_building(initial_building, data){
    let query_result;
    if (initial_building){
        // query_result in an array
        query_result = document.querySelector("#query_result").textContent;
        console.log(query_result);
        console.log(typeof(query_result));
        console.log("Parsing ...")
        query_result = JSON.parse(query_result);
        console.log(query_result);
        console.log(typeof(query_result));
    }else{
        query_result = data["query_result"];
    }

    // Table building
    const built_table = table_builder(query_result, headers);
    // Table rendering
    document.querySelector("#table-content").innerHTML = built_table;
    console.log(built_table);

}