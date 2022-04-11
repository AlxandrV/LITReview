search_bar = document.getElementsByName('search')[0]
search_input = document.getElementsByName('search-value')[0]
user_list = document.getElementsByClassName('users-list')[0]
token = document.getElementsByName('csrfmiddlewaretoken')[0].value


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
                'header': token,
                'url': 'search-follows/',
                'data': data
            }
            let xhr_response = await xhr(option)
            // console.log(xhr_response)
            user_list.innerHTML = xhr_response

            user_btn = Array.from(user_list.getElementsByTagName('BUTTON'))
            user_btn.forEach(btn => {
                btn.addEventListener('click', () => {
                    let add_follow = async() => {
                        form = new FormData()
                        form.append('id-user', btn.value)
                        const option = {
                            'type': 'POST',
                            'header': token,
                            'url': 'add-follow/',
                            'data': form
                        }
                        let xhr_follow = await xhr(option)
                    }
                    add_follow()
                })
            });
        }
    
        search_func()
    }
})