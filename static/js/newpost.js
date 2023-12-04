if(!document.cookie.includes('id='))
{
    window.location = "/view/login"
} 

const postData = async (url = '', data = {}) => {
    // Формируем запрос
    const response = await fetch(url, {
      method: 'POST',
     
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    return response.text()
}


const postData2 = async (url = '', data) => {
    // Формируем запрос
    const response = await fetch(url, {
      method: 'POST',
     
      headers: {
        'Content-Type': 'text'
      },
      body: data
    });
    return response.text()
}
postData2('/username', document.cookie.split('=')[1]).then((data) => {
    document.getElementById('username').textContent = data
});

function Onclick() {
    data = {content: document.getElementById('content').value, id_of_user: document.cookie.split('=')[1]}
    data
    postData('/newPost', data)
    window.location = "/view/main"
}