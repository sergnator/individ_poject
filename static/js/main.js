if(!document.cookie.includes('id='))
{
    window.location = "/view/login"
} 

const postData = async (url = '', data) => {
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
postData('/username', document.cookie.split('=')[1]).then((data) => {
    document.getElementById('username').textContent = data
});


let xmr = new XMLHttpRequest()
jsons = []
xmr.open("GET", "/posts")
xmr.onload = () =>{
    
    let lst1 = xmr.response.split('/n')
    console.log(lst1)
    lst1.forEach(element => {
        element = element.replace("'", '"')
        console.log(element)
        if(element.includes('}')){
            console.log(JSON.parse(element))
            console.log(element)
            jsons.push(JSON.parse(element))    
        }
    });
    jsons.forEach(element => {
        let div_container = document.createElement('div')
        div_container.className = 'box-content'
    
        
        let div_content = document.createElement('p')
        div_content.className = 'content'
        div_content.textContent = element.content
    
    
        let div_head = document.createElement('div')
        div_head.className = 'head-of-post'
    
        
        let div_username = document.createElement('div')
        div_username.className = 'username-of-post'
        div_username.textContent = element.username
        
        let label = document.createElement('label')
        label.className = 'date'
        label.textContent = element.date
        
        div_username.append(label)
        div_head.append(div_username)
        div_container.append(div_head)
        div_container.append(div_content)
        
        let main = document.getElementById('main')
        main.prepend(div_container)
        
        
    });

}
xmr.send()


