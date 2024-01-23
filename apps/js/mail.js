const button=document.getElementById("btn");

button.addEventListener("click",(e)=>{
    const email=document.getElementById("email").value;
    const subject=document.getElementById("subject").value;
    const message=document.getElementById("message").value;
    const data={
        sent_mail:email,
        subject:subject,
        body:message
    }
    fetch('https://portfolio-api.utsavchatterjee.me/api/v1/mail',{
        method:"POST",
        headers: {
            "Content-Type": "application/json",
          },
        body:JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        alert(data?.message)
    })
    .catch(err=>{
        alert('failed!')
    })
})