document.addEventListener('DOMContentLoaded', e => {
    document.querySelectorAll('.add_to_order').forEach(item => {
        item.addEventListener('click', e => {
            add_to_order("TODO")
        })
    })
})

function add_to_order(data){
    id = parseInt(data)
    fetch(`/api/add/${id}`)
    .then(Response => Response.json())
    .then(data => {
        update_message(data.message)
    })
}

function update_message(message) {
    if(message !== "") {
        var msg = document.querySelector("#message");
        msg.style.display = "block"
        msg.innerHTML = message;
    }
}