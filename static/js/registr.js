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
    
    pas = document.getElementById('password').value
    login = document.getElementById('username').value
    con = document.getElementById('confirm-password').value
    if(pas != con){
      alert('пароли не совпадают')
      return
    }
    postData('/registration', {username: login, passwrod: pas}).then((data) =>{
      if(data == -1){
        alert('имя занято')
        return
      }
      document.cookie = 'id=' + data
      window.location = 'main'
      
    })
    
}

if(document.cookie.includes('id='))
{
    window.location = "/view/main"
} 