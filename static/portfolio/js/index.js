const viewProjectsAnchor = document.getElementById("view-work-anchor");
const contactAnchor = document.getElementById("contact-me-anchor");
const heroAnchors = [ viewProjectsAnchor , contactAnchor ];

function redirectPage(pageName){
    let url = `${window.origin}/${pageName}`;
    document.location.href = url;
}

for( const anchor of heroAnchors ){
    anchor.addEventListener("click",()=>{
        redirectPage( `${anchor.name}` ); 
    });
}