const localStorage = window.localStorage
if(localStorage.length > 0){
    for (let i = 0; i < localStorage.length; i++){
        const findEl = document.getElementById(localStorage.key(i))
        if(findEl){
            findEl.children[0].textContent = '-'
            const check = localStorage.getItem(localStorage.key(i))
            if(check === 'true'){
                const itemList = findEl.parentNode.children[1].children
                for(item of itemList){
                    if(window.location.href == item.children[0].href){
                        item.classList.add('active')
                    }
                    item.classList.remove('hidden')
                }
            }
        }
    }
};
function showItems(el){
    const itemList = el.parentNode.parentNode.children[1].children
    if(el.textContent == '+'){
        for(item of itemList){
            item.classList.remove('hidden')
        }
        el.textContent = '-'
        window.localStorage.setItem(el.dataset.name, true)
    }
    else{
        for(item of itemList){
            item.classList.add('hidden')
        }
        el.textContent = '+'
        window.localStorage.removeItem(el.dataset.name)
        window.location.replace('/')
    }
};