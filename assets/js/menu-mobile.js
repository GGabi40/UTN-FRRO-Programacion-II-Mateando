function menu() {
  const menuBtn = document.querySelector(".menu-btn");
  const containMenuMobile = document.querySelector(".mobile");
  const menuItems = document.querySelectorAll(".menu-list-mob li a");

  menuBtn.addEventListener("change", () => {
    if (menuBtn.checked) {
      containMenuMobile.style.display = "block";
    } else {
      containMenuMobile.style.display = "none";
    }
  });

  menuItems.forEach((item) => {
    item.addEventListener("click", () => {
      menuBtn.checked = false;
      containMenuMobile.style.display = "none";
    });
  });
}

menu();
