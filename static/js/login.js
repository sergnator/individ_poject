const postData = async (url = '', data = {}) => {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    return response.json(); 
  }

function Onclick() {

    postData('/login', {username: document.getElementById('username').value, passwrod: document.getElementById('password').value}).then((data) =>{
    if (data == -1){
        alert('ошибка неверный пароль или имя пользователя')
        return
    }
    document.cookie = 'id=' + data
    
})
}

if(document.cookie.includes('id='))
{
    window.location = "/view/main"
} 