search_bar = document.getElementsByName('search')[0]
search_input = document.getElementsByName('search-value')[0]
user_list = document.getElementsByClassName('users-list')[0]
users_followed = document.getElementById('followed')
token = document.getElementsByName('csrfmiddlewaretoken')[0].value

console.log(users_followed)

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
                btn.classList.add('btn')
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
                        users_followed.insertAdjacentHTML('afterbegin', xhr_follow)
                        btn.parentNode.remove()
                    }
                    add_follow()
                })
            });
        }
    
        search_func()
    }
})

unfollow_btn = Array.from(users_followed.getElementsByTagName('BUTTON'))
unfollow_btn.forEach(btn => {
    btn.addEventListener('click', () => {
        let unfollow = async() => {
            form = new FormData()
            form.append('id-user', btn.value)
            const option = {
                'type': 'POST',
                'header': token,
                'url': 'unfollow/',
                'data': form
            }
            let xhr_unfollow = await xhr(option)
            JSON_res = JSON.parse(xhr_unfollow)
            if (btn.value == JSON_res.delete) {
                btn.parentNode.remove()
            }
        }
        unfollow()
    })
});
