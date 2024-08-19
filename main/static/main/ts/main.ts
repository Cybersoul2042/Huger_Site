document.addEventListener("DOMContentLoaded", function(){
    document.querySelector("#project")?.addEventListener("click", () => ChangePage("project"));
    document.querySelector("#submit")?.addEventListener("click", () => ChangePage("submit"));
    ChangePage('home');
})

function ChangePage(page:string){

    const bodyPages = document.querySelector('.body-container')?.children;

    // @ts-ignore
    for(const child:HTMLElement of bodyPages!){
        if((child.className) == `${page}-page`){
            child.style.display = "block"
        }
        else{
            child.style.display = "none"
        }
    }
}