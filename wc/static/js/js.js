  const menuBtn = document.querySelector(".menu-icon span");
  const searchBtn = document.querySelector(".search-icon");
  const cancelBtn = document.querySelector(".cancel-icon");
  const items = document.querySelector(".nav-items");
  const form = document.querySelector("form");
  menuBtn.onclick = ()=>{
    items.classList.add("active");
    menuBtn.classList.add("hide");
    searchBtn.classList.add("hide");
    cancelBtn.classList.add("show");
  }
  cancelBtn.onclick = ()=>{
    items.classList.remove("active");
    menuBtn.classList.remove("hide");
    searchBtn.classList.remove("hide");
    cancelBtn.classList.remove("show");
    form.classList.remove("active");
    cancelBtn.style.color = "#ff3d00";
  }
  searchBtn.onclick = ()=>{
    form.classList.add("active");
    searchBtn.classList.add("hide");
    cancelBtn.classList.add("show");
  }


  function login(){
    window.location.href ="file:///D:/WF-project/login.html";
  }

  function service(){
    window.location.href = "file:///D:/WF-project/mainservices.html";
  }

  function vehical(){
    window.location.href = "file:///D:/WF-project/vehical.html";
  }

  function technician(){
    window.location.href ="file:///D:/WF-project/technician.html";
  }