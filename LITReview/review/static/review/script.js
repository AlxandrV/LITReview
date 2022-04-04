search_bar = document.getElementsByName('search')[0]


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
    
    let search_func = async() => {
        data = new FormData(search_bar)
        // data.append('search', search_bar.value)
        const option = {
            'type': 'POST',
            'header': document.getElementsByName('csrfmiddlewaretoken')[0].value,
            'url': 'search-follows/',
            'data': data
        }
        let xhrJSON = await xhr(option).then(JSON.parse)
        console.log(xhrJSON)
    }

    search_func()
})