const homeAnchor = document.getElementById("home-anchor");
const servicesAnchor =  document.getElementById("services-anchor");
const projectAnchor =  document.getElementById("projects-anchor");
const resumeAnchor = document.getElementById("resume-anchor");

function redirectPage(pageName){
    let url = "";
    if( pageName.toLowerCase() === "home" ){
        url = `${window.origin}`;
    }
    else{
     url = `${window.origin}/${pageName}`;
    }
    document.location.href = url ;
}

const headerAnchors = [ homeAnchor , servicesAnchor , projectAnchor ]

for( const anchor of headerAnchors ){
    anchor.addEventListener("click",()=>{
        redirectPage(anchor.textContent.toLowerCase());
    });
    anchor.addEventListener("mouseover",()=>{
        anchor.style.textDecoration = "underline"; 
        anchor.style.cursor = "pointer";
        anchor.addEventListener("mouseout",()=>{
            anchor.style.textDecoration = "none";
        })
    });
}

/* FOOTER SECTION */
//Quick Links
const projectsItem = document.getElementById("projects-item");
const faqsItem = document.getElementById("faqs-item");
const quickLinks = [ projectsItem , faqsItem ]

for( const item of quickLinks ){
  item.addEventListener("click",()=>{
    redirectPage(`${item.textContent.toLocaleLowerCase()}`);
  });
  item.addEventListener("mouseover",()=>{
    item.style.cursor = "pointer";
    item.style.textDecoration = "underline";
    item.addEventListener("mouseout",()=>{
        item.style.textDecoration = "none";
    });
  });
}
