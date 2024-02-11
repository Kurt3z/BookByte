'use strict';

const updateBtns = document.getElementsByClassName('update-cart');

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        const contentId = this.dataset.content;
        const action = this.dataset.action;
        console.log(contentId, action);

        console.log('USER: ', user);

        if (user === 'AnonymousUser') {
            console.log('Not logged in.');
        }
        else {
            updateUserRequisition(contentId, action);
        }
        
    })
}


function updateUserRequisition(contentId, action) {
    console.log('User is logged in. Sending data...');

    const url = '/requisitions/update-content/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({
            'contentId': contentId,
            'action': action
        })
    }).then((response) => {
        return response.json()
    }).then((data) => {
        console.log(data);

        if (data.error) {
            alert(data.error)
        }
    })
}

function updateNavbarItemCount() {
    const requisitionItemCountElement = document.getElementById('navbar-item-count');

    const requisitionItemCountUrl = requisitionItemCountElement.dataset.requisitionItemCountUrl;

    fetch(requisitionItemCountUrl).then(response => {
        if (!response.ok) {
            throw new Error('Erro de rede');
        }
        return response.json();
    }).then(data => {
        document.getElementById('navbar-item-count').innerText = data.item_count;
    }).catch(error => {
        console.error('There was a problem with the fetch operation.');
    })
}

document.addEventListener('DOMContentLoaded', function() {
    updateNavbarItemCount();
})