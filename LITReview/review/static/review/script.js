search_bar = document.getElementsByName('search')[0]
search_input = document.getElementsByName('search-value')[0]
user_list = document.getElementsByClassName('users-list')[0]


// Ajax
function xhr(option) {
    return new Promise(function(resolve) {
        let xhr = new XMLHttpRequest();
        xhr.open(option.type, option.url);
        xhr.setRequestHeader('X-CSRFToken', option.header)
        xhr.send(option.data);
        xhr.onreadystatechange = function(){
            if (this.readyState == 4 && this.status == 200) {
                let response = xhr.response;
                return resolve(response);
            }
        };
    });
}
search_bar.addEventListener('input', () => {

    if (search_input.value !== "") {
        let search_func = async() => {
            data = new FormData(search_bar)
            // data.append('search', search_bar.value)
            const option = {
                'type': 'POST',
                'header': document.getElementsByName('csrfmiddlewaretoken')[0].value,
                'url': 'search-follows/',
                'data': data
            }
            let xhr_response = await xhr(option)
            console.log(xhr_response)
            user_list.innerHTML = xhr_response
        }
    
        search_func()
    }
})