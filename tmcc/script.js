document.addEventListener('DOMContentLoaded', e => {})

function add_to_order(data){
    id = parseInt(data)
    fetch(`/api/add/${id}`)
    .then(Response => Response.json())
    .then(data => {
        alert(data.message)
    })
}
function remove_from_order(item) {
    row = item.parentNode.parentNode;
    id = parseInt(item.dataset.item);
    fetch(`/api/remove/${id}`).then(response => response.json()).then(data => {
        alert(data.message);
        row.style.display = "none";
    })
    
}



function submit_apply(username, email, work_experience, questions, newsletter) {
    const csrf_token = Cookies.get('csrftoken');
    const request = new Request(
        '/apply',
        {headers: {'X-CSRFToken': csrf_token}}
    );
    fetch(request, {
        method: 'POST',
        body: JSON.stringify({
            username: username,
            email: email,
            work_experience: work_experience,
            questions: questions,
            newsletter: newsletter
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
}
