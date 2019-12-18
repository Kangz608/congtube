
document.addEventListener('DOMContentLoaded',function(){
    document.getElementById('top').addEventListener('click',function(){
        window.scrollTo({
            top:0,
            left:0,
            behavior:'smooth'
        });
    });
});

document.addEventListener('scroll',function(){
    
    if(window.innerWidth<992){
        if(window.scrollY===0){
        document.getElementById('top').style.display='none'
        }else{
        document.getElementById('top').style.display='block'
        }
    }else{
        document.getElementById('top').style.display='none'
    }
})
